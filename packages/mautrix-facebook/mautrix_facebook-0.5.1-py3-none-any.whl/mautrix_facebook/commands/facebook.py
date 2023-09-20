# mautrix-facebook - A Matrix-Facebook Messenger puppeting bridge.
# Copyright (C) 2022 Tulir Asokan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from __future__ import annotations

import asyncio

from maufbapi.types import graphql
from mautrix.bridge.commands import HelpSection, command_handler

from .. import portal as po, puppet as pu, user as u
from .typehint import CommandEvent

SECTION_MISC = HelpSection("Miscellaneous", 40, "")


async def _get_search_result_puppet(source: u.User, node: graphql.Participant) -> pu.Puppet:
    puppet = await pu.Puppet.get_by_fbid(node.id)
    if not puppet.name_set:
        await puppet.update_info(source, node)
    return puppet


@command_handler(
    needs_auth=True,
    management_only=False,
    help_section=SECTION_MISC,
    help_text="Search for a Facebook user",
    help_args="<_search query_>",
)
async def search(evt: CommandEvent) -> None:
    resp = await evt.sender.client.search(" ".join(evt.args))
    puppets = await asyncio.gather(
        *[
            _get_search_result_puppet(evt.sender, edge.node)
            for edge in resp.search_results.edges
            if isinstance(edge.node, graphql.Participant)
        ]
    )
    results = "".join(
        f"* [{puppet.name}](https://matrix.to/#/{puppet.default_mxid})\n" for puppet in puppets
    )
    if results:
        await evt.reply(f"Search results:\n\n{results}")
    else:
        await evt.reply("No results :(")


@command_handler(
    needs_auth=True,
    management_only=False,
    help_section=SECTION_MISC,
    help_text="Backfill the current chat",
)
async def backfill(evt: CommandEvent) -> None:
    if not evt.config["bridge.backfill.msc2716"]:
        await evt.reply("MSC2716 backfill is not enabled on this bridge")
        return
    portal: po.Portal = await po.Portal.get_by_mxid(evt.room_id)
    await portal.enqueue_immediate_backfill(evt.sender, 0)
    await evt.reply("Enqueued backfill for portal")

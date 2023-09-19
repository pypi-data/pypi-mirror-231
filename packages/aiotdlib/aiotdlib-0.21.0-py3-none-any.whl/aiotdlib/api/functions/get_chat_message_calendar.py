# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    SearchMessagesFilter,
)


class GetChatMessageCalendar(BaseObject):
    """
    Returns information about the next messages of the specified type in the chat split by days. Returns the results in reverse chronological order. Can return partial result for the last returned day. Behavior of this method depends on the value of the option "utc_time_offset"

    :param chat_id: Identifier of the chat in which to return information about messages
    :type chat_id: :class:`Int53`
    :param filter_: Filter for message content. Filters searchMessagesFilterEmpty, searchMessagesFilterMention, searchMessagesFilterUnreadMention, and searchMessagesFilterUnreadReaction are unsupported in this function
    :type filter_: :class:`SearchMessagesFilter`
    :param from_message_id: The message identifier from which to return information about messages; use 0 to get results from the last message
    :type from_message_id: :class:`Int53`
    """

    ID: typing.Literal["getChatMessageCalendar"] = "getChatMessageCalendar"
    chat_id: Int53
    filter_: SearchMessagesFilter = Field(..., alias="filter")
    from_message_id: Int53

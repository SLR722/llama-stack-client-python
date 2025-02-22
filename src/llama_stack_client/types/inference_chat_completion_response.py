# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .token_log_probs import TokenLogProbs
from .shared.content_delta import ContentDelta
from .shared.completion_message import CompletionMessage

__all__ = [
    "InferenceChatCompletionResponse",
    "ChatCompletionResponse",
    "ChatCompletionResponseStreamChunk",
    "ChatCompletionResponseStreamChunkEvent",
]


class ChatCompletionResponse(BaseModel):
    completion_message: CompletionMessage

    logprobs: Optional[List[TokenLogProbs]] = None


class ChatCompletionResponseStreamChunkEvent(BaseModel):
    delta: ContentDelta

    event_type: Literal["start", "complete", "progress"]

    logprobs: Optional[List[TokenLogProbs]] = None

    stop_reason: Optional[Literal["end_of_turn", "end_of_message", "out_of_tokens"]] = None


class ChatCompletionResponseStreamChunk(BaseModel):
    event: ChatCompletionResponseStreamChunkEvent


InferenceChatCompletionResponse: TypeAlias = Union[ChatCompletionResponse, ChatCompletionResponseStreamChunk]

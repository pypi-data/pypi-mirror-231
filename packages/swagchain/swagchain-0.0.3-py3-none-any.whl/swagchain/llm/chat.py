import functools
from typing import Callable, Coroutine, Dict, List, Literal, TypeAlias, TypeVar

import openai  # pylint-disable=E0401
from aiofauna import *  # type: ignore
from jinja2 import Template
from pydantic import BaseModel, Field  # pylint: disable=no-name-in-module
from typing_extensions import ParamSpec

T = TypeVar("T")
P = ParamSpec("P")

Role: TypeAlias = Literal["assistant", "user", "system", "function"]
Model: TypeAlias = Literal["gpt-4-0613", "gpt-3.5-turbo-16k-0613"]
Size: TypeAlias = Literal["256x256", "512x512", "1024x1024"]
Format: TypeAlias = Literal["url", "base64"]


class Message(Document):
    """
    A message in a chat

    Args:
        role (Role): The role of the message (assistant, user, system, function)
        content (str): The content of the message
    """
    role: Role = Field(..., description="The role of the message")
    content: str = Field(..., description="The content of the message")


class ChatCompletionRequest(Document):
    """

    Chat completion request

    Args:

        model (Model): The model to use for the completion (gpt-4-0613, gpt-3.5-turbo-16k-0613)
        messages (List[Message]): The messages to use for the completion
        temperature (float): The temperature of the completion
        max_tokens (int): The maximum number of tokens to generate
        stream (bool): Whether to stream the completion or not
    """
    model: Model = Field(..., description="The model to use for the completion")
    messages: List[Message] = Field(
        ..., description="The messages to use for the completion"
    )
    temperature: float = Field(
        default=0.5, description="The temperature of the completion"
    )
    max_tokens: int = Field(
        1024, description="The maximum number of tokens to generate"
    )
    stream: bool = Field(False, description="Whether to stream the completion or not")


class ChatCompletionUssage(Document):
    """

    Chat completion usage

    Args:

        prompt_tokens (int): The number of tokens in the prompt

        completion_tokens (int): The number of tokens in the completion

        total_tokens (int): The total number of tokens

    """
        
    prompt_tokens: int = Field(..., description="The number of tokens in the prompt")
    completion_tokens: int = Field(
        ..., description="The number of tokens in the completion"
    )
    total_tokens: int = Field(..., description="The total number of tokens")


class ChatCompletionChoice(Document):
    """

    Chat completion choice

    Args:

        index (int): The index of the choice

        message (Message): The message of the choice

        finish_reason (str): The reason the choice was finished

    """ 
    
    index: int = Field(..., description="The index of the choice")
    message: Message = Field(..., description="The message of the choice")
    finish_reason: str = Field(..., description="The reason the choice was finished")


class ChatCompletionResponse(Document):
    """

    Chat completion response

    Args:

        id (str): The id of the completion

        object (str): The object of the completion

        created (int): The creation time of the completion

        model (Model): The model used for the completion

        choices (List[ChatCompletionChoice]): The choices of the completion

        usage (ChatCompletionUssage): The usage of the completion

        stream (bool): Whether the completion was streamed or not

    """

    id: str = Field(..., description="The id of the completion")
    object: str = Field(..., description="The object of the completion")
    created: int = Field(..., description="The creation time of the completion")
    model: Model = Field(..., description="The model used for the completion")
    choices: List[ChatCompletionChoice] = Field(
        ..., description="The choices of the completion"
    )
    usage: ChatCompletionUssage = Field(..., description="The usage of the completion")
    stream: bool = Field(..., description="Whether the completion was streamed or not")


class VectorResponse(Document):
    """

    Vector response

    Args:

        id (str): The id of the vector

        object (str): The object of the vector

        created (int): The creation time of the vector

        model (Model): The model used for the vector

        data (List[float]): The data of the vector

    """  
    
    text: str = Field(..., description="The text of the completion")
    score: float = Field(..., description="The score of the completion")


class CreateImageResponse(Document):
    """

    Create image response

    Args:

        id (str): The id of the image

        object (str): The object of the image

        created (float): The creation time of the image

        data (List[Dict[Format, str]]): The data of the image

    """
    
    created: float = Field(...)
    data: List[Dict[Format, str]] = Field(...)


class CreateImageRequest(Document):
    """

    Create image request

    Args:

        prompt (str): The prompt of the image

        n (int): The number of images to generate

        size (Size): The size of the image

        response_format (Format): The format of the response

    """   
    
    prompt: str = Field(...)
    n: int = Field(default=1)
    size: Size = Field(default="1024x1024")
    response_format: Format = Field(default="url")


class LanguageModel(BaseModel):
    """

    ChatGPT: A GPT-3 chatbot

    This class is a wrapper around the OpenAI Chat API

    Args:

        model (Model): The model to use for the completion (gpt-4-0613, gpt-3.5-turbo-16k-0613)

        temperature (float): The temperature of the completion

        max_tokens (int): The maximum number of tokens to generate

    """  
    
    
    model: Model = Field(default="gpt-4-0613")
    temperature: float = Field(default=0.2)
    max_tokens: int = Field(default=1024)

    async def chat(
        self, messages: List[Message]
    ) -> str:
        """

        Chat with the bot

        Args:

            messages (List[Message]): The messages to use for the completion

        Returns:

            str: The response of the bot

        """
       
        response = await openai.ChatCompletion.acreate(  # type: ignore
            model=self.model,
            messages=[message.dict() for message in messages],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            stream=False
        )
        
        return response.choices[0].message.content  # type: ignore

    def __call__(self, func: Callable[P,Coroutine[T,Any,Any]]) -> Callable[P,Coroutine[T,Any,Any]]:
        """

        Call the bot with a function that features a jinja2 docstring as a template for the system message, and the user message as the first argument, prompt engineering is done automatically

        Args:

            func (Callable[P,Coroutine[T,Any,Any]]): The function to call

        Returns:

            Callable[P,Coroutine[T,Any,Any]]: The wrapped function

        """
        if func.__doc__ is None:
            raise ValueError("Function must have a docstring")
        _template = func.__doc__	
        @handle_errors
        @functools.wraps(func)
        async def wrapper(*args:P.args, **kwargs:P.kwargs) -> T:
            template = Template(_template)
            ctx = template.render(**kwargs)
            kwargs["context"] = ctx
            return await func(*args, **kwargs)
        return wrapper
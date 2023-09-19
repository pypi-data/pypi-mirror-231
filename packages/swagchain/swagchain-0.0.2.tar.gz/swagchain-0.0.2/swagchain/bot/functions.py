import inspect
import json
from abc import ABC, abstractmethod
from typing import Any, Callable, Coroutine, List, Optional, Set, Type, TypeVar

import openai
from pydantic import BaseModel  # pylint: disable=no-name-in-module
from pydantic import create_model  # pylint: disable=no-name-in-module
from typing_extensions import ParamSpec

from ..utils import Caser

F = TypeVar("F", bound="OpenAIFunction")
T = TypeVar("T")
P = ParamSpec("P")
c = Caser()

class FunctionCall(BaseModel):
    name: str
    data: Any

class OpenAIFunction(BaseModel, ABC):
    """Base class for OpenAI Functions"""
    class Metadata:
        subclasses: Set[Type[F]] = set()

    @classmethod
    def __init_subclass__(cls, **kwargs: Any):
        super().__init_subclass__(**kwargs)
        _schema = cls.schema()
        if cls.__doc__ is None:
            cls.__doc__ = ""
        cls.openaischema = {
            "name": cls.__name__,
            "description": cls.__doc__,
            "parameters": {
                "type": "object",
                "properties": {
                    k: v for k, v in _schema["properties"].items() if k != "self"
                },
                "required": _schema.get("required", []),
            },
        }
        cls.Metadata.subclasses.add(cls)

    @classmethod
    def from_function(cls, func: Callable[P, Coroutine[Any,Any,Any]]) -> Type["OpenAIFunction"]:
        kwargs = inspect.signature(func).parameters
        
        klass = create_model(
           c(func.__name__,"pascal"),
            __base__=cls,
            **{
                k: (v.annotation, ...) for k, v in kwargs.items() if k != "self"
            },
        )

        klass.__doc__ = func.__doc__
        
        
        async def run(self, **kwargs: Any) -> Any:
            return await func(self, **kwargs)
        
        setattr(klass, "run", run)
        klass.__init_subclass__()
        
        return klass
    
    async def __call__(self, **kwargs: Any) -> FunctionCall:
        response = await self.run(**kwargs)
        return FunctionCall(name=self.__class__.__name__, data=response)

    async def run(self, **kwargs: Any) -> Any:
        ...

async def parse_openai_function(
    response: dict[str, Any],
    functions: List[Type[F]] = OpenAIFunction.Metadata.subclasses,
    **kwargs: Any,
) -> FunctionCall:
    choice = response["choices"][0]["message"]
    if "function_call" in choice:
        function_call_ = choice["function_call"]
        name = function_call_["name"]
        arguments = function_call_["arguments"]
        print(name, arguments)
        for i in functions:
            if i.__name__ == name:
                result = await i(**json.loads(arguments))(**kwargs)
                break
        else:
            raise ValueError(f"Function {name} not found")
        return result
    return FunctionCall(name="chat", data=choice["content"])


async def function_call(
    text: str,
    model: str = "gpt-3.5-turbo-16k-0613",
    functions: List[Type[F]] = OpenAIFunction.Metadata.subclasses,
    **kwargs: Any,
) -> FunctionCall:
    """Default function call"""
    messages = [
        {"role": "user", "content": text},
        {"role": "system", "content": "You are a function Orchestrator"},
    ]
    response = await openai.ChatCompletion.acreate( 
        model=model,
        messages=messages,
        functions=[i.openaischema for i in functions],
    ) 
    return await parse_openai_function(response, functions=functions, **kwargs)


async def chat_completion(text: str, context: Optional[str] = None):
    if context is not None:
        messages = [
            {"role": "user", "content": text},
            {"role": "system", "content": context},
        ]
    else:
        messages = [{"role": "user", "content": text}]
    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo-16k-0613", messages=messages
    )
    return response["choices"][0]["message"]["content"]

from pydantic import BaseConfig

from .memory import *
from .tools import *


class Agent(ABC):
	
	
	llm:LanguageModel
	memory:Memory
	namespace:str
	n:int
	

	@abstractmethod
	async def __call__(self, text:str)->str:
		"""
		Chain a text
		"""
		...

class Swagchain(Agent):

	def __init__(self, llm:LanguageModel=LanguageModel(), memory:Memory=Memory(), namespace:str="main", n:int=5):
		self.llm = llm
		self.memory = memory
		self.namespace = namespace
		self.n = n

	async def __call__(self, text:str):
		"""
		Chain a text
		"""
		matches = await self.memory.search(text=text, namespace=self.namespace, top_k=self.n)
		if matches:
			context = "Suggestions:\n"+"\n".join(matches)
			return await self.llm.chat(messages=[Message(role="user",content=text), Message(role="system",content=context)])
		else:
			return await self.llm.chat(messages=[Message(role="user",content=text)])
	

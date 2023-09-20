import re
from typing import Literal, TypeAlias

Case: TypeAlias = Literal["snake", "pascal", "camel", "constant", "human"]

class Caser:
	@staticmethod
	def snake_case(text:str):
		return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()

	@staticmethod
	def pascal_case(text:str):
		return ''.join(word.capitalize() for word in text.split('_'))

	@staticmethod
	def camel_case(text:str):
		words = text.split('_')
		return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

	@staticmethod
	def constant_case(text:str):
		return re.sub(r'(?<!^)(?=[A-Z])', '_', text).upper()

	@staticmethod
	def human_case(text:str):
		return ' '.join(word.capitalize() for word in text.split('_'))
	
	def __call__(self, text:str, case:Case):
		return getattr(self, f"{case}_case")(text)

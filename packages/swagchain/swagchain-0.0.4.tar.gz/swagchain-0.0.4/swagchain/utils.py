import re
from typing import Literal, TypeAlias

Case: TypeAlias = Literal["snake", "pascal", "camel", "constant", "human"]

class Caser:
	@staticmethod
	def snake_case(text:str):
		"""

		Args:

			text (str): The text to convert

		Returns:

			str: The converted text

		Converts a text to snake_case

		"""
		return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()

	@staticmethod
	def pascal_case(text:str):
		"""

		Args:

			text (str): The text to convert

		Returns:

			str: The converted text

		Converts a text to PascalCase

		"""		
		
		
		return ''.join(word.capitalize() for word in text.split('_'))

	@staticmethod
	def camel_case(text:str):
		"""

		Args:

			text (str): The text to convert

		Returns:

			str: The converted text

		Converts a text to camelCase

		"""
		
		
		words = text.split('_')
		return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

	@staticmethod
	def constant_case(text:str):
		"""

		Args:

			text (str): The text to convert

		Returns:

			str: The converted text

		Converts a text to CONSTANT_CASE

		"""
		
		return re.sub(r'(?<!^)(?=[A-Z])', '_', text).upper()

	@staticmethod
	def human_case(text:str):
		"""

		Args:

			text (str): The text to convert

		Returns:

			str: The converted text

		Converts a text to Human Case

		"""
		return ' '.join(word.capitalize() for word in text.split('_'))
	
	def __call__(self, text:str, case:Case):
		"""

		Args:

			text (str): The text to convert

			case (Case): The case to convert to

		Returns:


			str: The converted text

		Converts a text to a case

		"""
		return getattr(self, f"{case}_case")(text)

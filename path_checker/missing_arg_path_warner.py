from .arg_path_checker import ArgPathChecker
from .path_checker import PathChecker


class MissingArgPathWarner:

	def __init__(self, arg_name, suffixes):
		self._arg_name = arg_name
		self._extension = suffixes

	def make_arg_path_checker(self, path):
		return ArgPathChecker(path, self._extension, self._arg_name)

	def make_missing_arg_msg(self):
		"""
		The message created by this method tells that the argument named
		<argument name>, the path to a file with extension
		<expected extension>, is needed. It is relevant if the argument is
		missing.

		Returns:
			str: a message telling that the argument is needed
		"""
		return self._arg_name + ": the path to a file with extension '"\
			+ "".join(self._extension) + "' must be provided."

	def make_path_checker(self, path):
		return PathChecker(path, self._extension)

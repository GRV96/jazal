from path_checker import PathChecker


class ArgPathChecker(PathChecker):

	def __init__(self, a_path, suffixes, arg_name):
		PathChecker.__init__(self, a_path, suffixes)
		self.arg_name = arg_name

	@property
	def arg_name(self):
		return self._arg_name

	@arg_name.setter
	def arg_name(self, name):
		self._arg_name = name

	def check_path_exists(self):
		if not self.path_exists():
			raise FileNotFoundError(self.arg_name + ": "
				+ str(self.path) + " does not exist.")

	def check_extension_correct(self):
		if not self.extension_is_correct():
			raise ValueError(self.arg_name
				+ " must be the path to a file with the extension '"
				+ self.extension_to_str() + "'.")

	def make_missing_arg_msg(self):
		return self.arg_name + ": the path to a file with extension '"\
			+ self.extension_to_str() + "' must be provided."

	def _set_path(self, a_path):
		if a_path is None:
			self._path = a_path

		else:
			PathChecker._set_path(self, a_path)

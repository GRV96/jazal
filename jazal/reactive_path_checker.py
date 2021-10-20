from .path_checker import PathChecker


class ReactivePathChecker(PathChecker):
	"""
	In this subclass of PathChecker, the path is considered as an argument
	given to a fucntion or a script. The class provides methods to react to
	invalid paths by warning the user or making a correct path.
	"""

	def __init__(self, a_path, extension, arg_name):
		"""
		The constructor needs a file path, the expected extension and the name
		of the argument whose value is the checked path. If a_path is a string,
		it will be converted to a pathlib.Path object. If it is of type
		pathlib.Path, the instance will store a copy of it.

		Args:
			a_path (pathlib.Path or str): the path that this instance will
				check.
			extension (str): the extension that the path is supposed to have.
				It must start with a '.'. If the path is not supposed to have
				an extension, set this argument to an empty string.
			arg_name (str): the name of the argument whose value is the
				checked path

		Raises:
			TypeError: if a_path is not an instance of str or pathlib.Path or
				if suffixes is not None, nor a list or a tuple
		"""
		PathChecker.__init__(self, a_path, extension)
		self._arg_name = arg_name

	def __eq__(self, other):
		return PathChecker.__eq__(self, other)\
			and self._arg_name == other._arg_name

	def __repr__(self):
		return self.__class__.__name__ + "('" + str(self._path) + "', '"\
			+ self._extension + "', '" + self._arg_name + "')"

	@property
	def arg_name(self):
		"""
		This read-only property is the name (str) of the function or script
		argument whose value is property path.
		"""
		return self._arg_name

	def check_extension_correct(self):
		"""
		If path's extension does not match property extension, this method
		raises a ValueError. The error message contains property arg_name.

		Raises:
			ValueError: if self.extension_is_correct() returns False
		"""
		if not self.extension_is_correct():
			raise ValueError(self.arg_name
				+ " must be the path to a file with the extension '"
				+ self._extension + "'.")

	def check_path_exists(self):
		"""
		If path does not exist, this method raises a FileNotFoundError. The
		error message contains property arg_name.

		Raises:
			FileNotFoundError: if self.path_exists() returns False
		"""
		if not self.path_exists():
			raise FileNotFoundError(self.arg_name + ": "
				+ str(self._path) + " does not exist.")

	def name_with_correct_exten(self):
		"""
		Creates a file name by appending the expected extension to path's stem.

		Returns:
			str: path's file name with the expected extension
		"""
		return self.get_file_stem() + self._extension

	def path_with_correct_exten(self):
		"""
		Creates a file path by replacing path's extension with property
		extension.

		Returns:
			pathlib.Path: a path identical to property path, but with the
				expected extension
		"""
		return self._path.parents[0]/self.name_with_correct_exten()

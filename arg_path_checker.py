from path_checker import PathChecker


class ArgPathChecker(PathChecker):
	"""
	In this subclass of PathChecker, the path is considered as an argument
	given to a fucntion or a script. The class provides methods to warn the
	user that path is invalid and others to make a correct path. Property path
	can be set to None.
	"""

	def __init__(self, a_path, suffixes, arg_name):
		"""
		The constructor needs a path, a list of suffixes that will make the
		expected extension and the name of the argument whose value is the
		checked path. In order to know which values are accepted, see the
		documentation of PathChecker's properties path and extension.

		Args:
			a_path (pathlib.Path): the path that this instance will check
			suffixes (list or tuple): the extension that path is supposed to
				have.
			arg_name (str): the name of the argument whose value is the
				checked path

		Raises:
			TypeError: if a_path is not None and not an instance of str or
				pathlib.Path
		"""
		PathChecker.__init__(self, a_path, suffixes)
		self.arg_name = arg_name

	@property
	def arg_name(self):
		"""
		Property path is the value of a function's or script's argument. This
		property is the name of that argument.
		"""
		return self._arg_name

	@arg_name.setter
	def arg_name(self, name):
		self._arg_name = name

	def check_path_exists(self):
		"""
		If path does not exist, this method raises a FileNotFoundError. The
		error message contains property arg_name.

		Raises:
			FileNotFoundError: if self.path_exists() returns False
		"""
		if not self.path_exists():
			raise FileNotFoundError(self.arg_name + ": "
				+ str(self.path) + " does not exist.")

	def check_extension_correct(self):
		"""
		If path's extension does not match property extension, this method
		raises a ValueError. The error message contains property arg_name.

		Raises:
			ValueError: if self.extension_is_correct() return False
		"""
		if not self.extension_is_correct():
			raise ValueError(self.arg_name
				+ " must be the path to a file with the extension '"
				+ self.extension_to_str() + "'.")

	def make_missing_arg_msg(self):
		"""
		The message created by this method tells that argument self.arg_name,
		the path to a file with extension self.extension, is needed. It is
		relevant if the argument is missing.

		Returns:
			str: a message telling that the argument is needed
		"""
		return self.arg_name + ": the path to a file with extension '"\
			+ self.extension_to_str() + "' must be provided."

	def path_with_correct_exten(self):
		"""
		Creates a copy of path and replaces its extension with self.extension.
		It only works if the checked path points to a file.

		Returns:
			pathlib.Path: a copy of path with the correct extension or None if
				path does not point to a file.
		"""
		stem = self.get_file_name(False)

		if stem is None:
			# path does not point to a file.
			return None

		return self.path.parents[0]/(stem + self.extension_to_str())

	def _set_path(self, a_path):
		"""
		Sets the path checked by this instance. The path must be an instance
		of pathlib.Path. If the given path is a string, it will be converted
		to a pathlib.Path object. The path can be set to None.

		Args:
			a_path (str or pathlib.Path): the path that this object must check

		Raises:
			TypeError: if a_path is not None and not an instance of str or
				pathlib.Path
		"""
		if a_path is None:
			self._path = a_path

		else:
			PathChecker._set_path(self, a_path)

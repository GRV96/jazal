from pathlib import Path


class PathChecker:
	"""
	This class contains a Pathlib Path object (property path) and a list of
	suffixes (property extension) that the path is supposed to have.
	PathChecker can verify whether the path has the right extension, whether
	it exists and whether it is a directory or a file.

	In this class, a file's stem is defined as its file name without the
	extension. However, in Pathlib, the stem is the file name without its last
	suffix.
	"""

	def __init__(self, a_path, suffixes):
		"""
		The constructor needs a path and a list of suffixes that will make the
		extension. In order to know which values are accepted, see the
		documentation of properties path and extension.

		Args:
			a_path (pathlib.Path): the path that this instance will check
			suffixes (list): the extension that the path is supposed to have.
		"""
		self.path = a_path
		self.extension = suffixes

	def __eq__(self, other):
		if not isinstance(other, self.__class__):
			return False

		return self.path == other.path and self.extension == other.extension

	def __repr__(self):
		return self.__class__.__name__ + "('" + str(self.path) + "', "\
			+ str(self.extension) + ")"

	def add_suffix(self, suffix):
		"""
		Adds a suffix to the end of property extension.

		Args:
			suffix (str): the suffix to add
		"""
		self.extension.append(suffix)

	@property
	def extension(self):
		"""
		The extension that the checked path is supposed to have, stored as a
		list of suffixes, which are strings. For example, a PDF file's suffix
		list is ['.pdf']; a Linux archive's suffix list can be
		['.tar', '.gz']. Every extension must start with '.'. The suffixes can
		be given in a tuple. If this property is set to None, it will be an
		empty list.
		"""
		return self._extension

	@extension.setter
	def extension(self, suffixes):
		if suffixes is None:
			self._extension = []

		else:
			self._extension = list(suffixes)

	def extension_is_correct(self):
		"""
		Indicates whether the path's extension matches the expected extension.

		Returns:
			bool: True if the path has the right extension, False otherwise
		"""
		return self._path.suffixes == self.extension

	def extension_to_str(self):
		"""
		Concatenates the suffixes that make property extension.

		Returns:
			str: extension as one string
		"""
		return "".join(self.extension)

	def get_file_name(self, with_ext=True):
		"""
		Provides the name of the file pointed to by path. The returned name
		includes the extension if and only if with_ext is True. If path does
		not point to a file, an empty string is returned.

		Args:
			with_ext (bool): if True, the returned file name will contain the
				extension. Defaults to True.

		Returns:
			str: the name of the file pointed to by path. If path does not
			point to a file, an empty string is returned.
		"""
		if not self.path_is_file():
			return ""

		file_name = self.path.name

		if not with_ext:
			ext_index = file_name.index(self.path.suffixes[0])
			file_name = file_name[:ext_index]

		return file_name

	def make_file_stem(self, before_stem=None, after_stem=None):
		"""
		Creates a file stem by adding a string to the beginning and/or the end
		of path's stem. If before_stem and after_stem are None, path's stem is
		returned. This method does not change path.

		Args:
			before_stem (str): the string to add to the beginning of path's
				stem. If it is None, nothing is added to the stem's beginning.
				Defaults to None.
			after_stem (str): the string to add to the end of path's stem. If
				it is None, nothing is added to the stem's end. Defaults to
				None.

		Returns:
			str: a new stem with the specified additions
		"""
		stem = self.get_file_name(False)

		if before_stem is not None:
			stem = before_stem + stem

		if after_stem is not None:
			stem += after_stem

		return stem

	@property
	def path(self):
		"""
		The path that this object checks. It must be an instance of Pathlib's
		class Path. If it is set to a string, that string is converted to a
		Path object.
		"""
		return self._path

	@path.setter
	def path(self, a_path):
		if isinstance(a_path, Path):
			self._path = a_path

		elif isinstance(a_path, str):
			self._path = Path(a_path)

		else:
			raise TypeError("The given path must be an instance "
				+ "of str or Pathlib's class Path.")

	def path_exists(self):
		"""
		Indicates whether path points to an existent directory of file.

		Returns:
			bool: True if the path exists, False otherwise
		"""
		return self.path.exists()

	def path_is_dir(self):
		"""
		Indicates whether path points to a directory.

		Returns:
			bool: True if the path is a directory, False otherwise
		"""
		return self.path.is_dir()

	def path_is_file(self):
		"""
		Indicates whether path points to a file.

		Returns:
			bool: True if the path is a file, False otherwise
		"""
		return self.path.is_file()

	def remove_suffix(self, suffix):
		"""
		Removes a suffix from extension. If extension does not contain suffix,
		nothing happens.

		Args:
			suffix (str): the suffix to remove from extension

		Returns:
			bool: True if extension contained suffix, False otherwise
		"""
		try:
			self.extension.remove(suffix)
			return True

		except ValueError:
			return False

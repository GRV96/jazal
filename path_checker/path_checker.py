from pathlib import Path


class PathChecker:
	"""
	This class contains a pathlib.Path object (property path) and a list of
	suffixes (property extension) that the path is supposed to have.
	PathChecker can verify whether the path has the right extension, whether
	it exists and whether it is a directory or a file.

	In this class, a file's stem is defined as its name without the extension.
	In Pathlib, however, the stem is the file name without the last suffix.
	"""

	def __init__(self, a_path, suffixes):
		"""
		The constructor needs a path and a list of suffixes that will make the
		expected extension. In order to know which values are accepted, see
		the documentation of properties path and extension.

		Args:
			a_path (pathlib.Path or str): the path that this instance will check
			suffixes (list or tuple): the extension that the path is supposed
				to have

		Raises:
			TypeError: if a_path is not an instance of str or pathlib.Path
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
		['.tar', '.gz']. Every suffix must start with '.'. The suffixes can be
		given in a tuple. If this property is set to None, it will be an empty
		list.
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
		Indicates whether path's extension matches the expected extension,
		stored in property extension.

		Returns:
			bool: True if path has the right extension, False otherwise
		"""
		return self.path.suffixes == self.extension

	def extension_to_str(self):
		"""
		Concatenates the suffixes that make property extension.

		Returns:
			str: extension as one string
		"""
		return "".join(self.extension)

	def get_file_name(self, with_exten=True):
		"""
		Provides the name of the file that path points to. The returned name
		includes the extension if with_exten is True.

		Args:
			with_exten (bool): if True, the returned file name will contain
				the extension. Defaults to True.

		Returns:
			str: the name of the file that path points to
		"""
		file_name = self.path.name

		actual_suffixes = self.path.suffixes
		if not with_exten and len(actual_suffixes) > 0:
			exten_index = file_name.index(actual_suffixes[0])
			file_name = file_name[:exten_index]

		return file_name

	def make_altered_name(self, before_stem=None,
			after_stem=None, extension=None):
		"""
		Creates a file name by adding a string to the beginning and/or the end
		of path's stem and appending an extension to the new stem. If
		before_stem and after_stem are None, the new stem is identical to
		path's stem. This method does not change path. Use make_altered_stem
		instead if you do not want to append an extension.

		Args:
			before_stem (str): the string to add to the beginning of path's
				stem. If it is None, nothing is added to the stem's beginning.
				Defaults to None.
			after_stem (str): the string to add to the end of path's stem. If
				it is None, nothing is added to the stem's end. Defaults to
				None.
			extension (str): the extension to append to the new stem in order
				to make the name. Each suffix must comply with the
				specification of property extension. If None, extension is
				appended. Defaults to None.

		Returns:
			str: a new file name with the specified additions
		"""
		stem = self.make_altered_stem(before_stem, after_stem)

		if extension is None:
			name = stem + self.extension
		else:
			name = stem + extension

		return name

	def make_altered_stem(self, before_stem=None, after_stem=None):
		"""
		Creates a file stem by adding a string to the beginning and/or the end
		of path's stem. If before_stem and after_stem are None, path's stem is
		returned. This method does not change path. Use make_altered_name
		instead to append an extension.

		Args:
			before_stem (str): the string to add to the beginning of path's
				stem. If it is None, nothing is added to the stem's beginning.
				Defaults to None.
			after_stem (str): the string to add to the end of path's stem. If
				it is None, nothing is added to the stem's end. Defaults to
				None.

		Returns:
			str: a new file stem with the specified additions
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
		The path that this object checks. It must be an instance of
		pathlib.Path. If it is set to a string, that string will be converted
		to a pathlib.Path object.
		"""
		return self._path

	@path.setter
	def path(self, a_path):
		self._set_path(a_path)

	def path_exists(self):
		"""
		Indicates whether path points to an existent directory or file.

		Returns:
			bool: True if path exists, False otherwise
		"""
		return self.path.exists()

	def path_is_dir(self):
		"""
		Indicates whether path points to a directory.

		Returns:
			bool: True if path exists and is a directory, False otherwise
		"""
		return self.path.is_dir()

	def path_is_file(self):
		"""
		Indicates whether path points to a file.

		Returns:
			bool: True if path exists and is a file, False otherwise
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

	def _set_path(self, a_path):
		"""
		Sets the path checked by this instance. The path must be an instance
		of pathlib.Path. If the given path is a string, it will be converted
		to a pathlib.Path object.

		Args:
			a_path (pathlib.Path or str): the path that this object must check

		Raises:
			TypeError: if a_path is not an instance of pathlib.Path or str
		"""
		if isinstance(a_path, Path):
			self._path = a_path

		elif isinstance(a_path, str):
			self._path = Path(a_path)

		else:
			raise TypeError(
				"The given path must be an instance of pathlib.Path or str.")

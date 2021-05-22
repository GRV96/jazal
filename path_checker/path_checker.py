from pathlib import Path
from .path_util import get_file_stem


_PATH_STR_TYPES = (Path, str)


class PathChecker:
	"""
	This class contains a pathlib.Path object (property path) and a tuple of
	suffixes (property extension) that the path is supposed to have.
	PathChecker can verify whether the path has the right extension, whether
	it exists and whether it is a directory or a file.

	In this class, a file's stem is defined as its name without the extension.
	In Pathlib, however, the stem is the file name without the last suffix.
	"""

	def __init__(self, a_path, suffixes):
		"""
		The constructor needs a path and a list or tuple of suffixes that will
		make the expected extension. In order to know which values are
		accepted, see the documentation of properties path and extension.

		Args:
			a_path (pathlib.Path or str): the path that this instance will
				check
			suffixes (list or tuple): the extension that the path is supposed
				to have. If None, the extension will be an empty tuple.

		Raises:
			TypeError: if a_path is not an instance of str or pathlib.Path
		"""
		self.path = a_path
		self._set_extension(suffixes)

	def __eq__(self, other):
		if not isinstance(other, self.__class__):
			return False

		return self.path == other.path and self.extension == other.extension

	def __repr__(self):
		return self.__class__.__name__ + "('" + str(self.path) + "', "\
			+ str(self.extension) + ")"

	@property
	def extension(self):
		"""
		This read-only property is the extension that the checked path is
		supposed to have, stored as a tuple of suffixes, which are strings.
		For example, a PDF file's suffix tuple is ('.pdf',); a Linux archive's
		suffix tuple can be ('.tar', '.gz'). Every suffix starts with '.'.
		"""
		return self._extension

	def extension_is_correct(self):
		"""
		Indicates whether path's extension matches the expected extension,
		stored in property extension.

		Returns:
			bool: True if path has the right extension, False otherwise
		"""
		# pathlib.Path objects store their extension in a list.
		return tuple(self.path.suffixes) == self.extension

	def extension_to_str(self):
		"""
		Concatenates the suffixes that make property extension.

		Returns:
			str: extension as one string
		"""
		return "".join(self.extension)

	def get_file_name(self):
		"""
		Provides the name of the file that path points to.

		Returns:
			str: the name of the file that path points to
		"""
		return self.path.name

	def get_file_stem(self):
		"""
		Provides the stem of the file that path points to.

		Returns:
			str: the stem of the file that path points to
		"""
		return get_file_stem(self.path)


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

	def _set_extension(self, suffixes):
		"""
		Sets the extension that the path checked by this instance is supposed
		to have. See the documentation of property extension. If the extension
		is set to None, it will be an empty tuple.

		Args:
			suffixes (list or tuple): the extension that path is supposed to
				have. If it is a list, it will be converted to a tuple.
		"""
		if suffixes is None:
			self._extension = ()

		elif isinstance(suffixes, tuple):
			self._extension = suffixes

		else:
			self._extension = tuple(suffixes)

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
		if isinstance(a_path, _PATH_STR_TYPES):
			self._path = Path(a_path)

		else:
			raise TypeError(
				"The given path must be an instance of pathlib.Path or str.")

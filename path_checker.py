from pathlib import Path


class PathChecker:

	def __init__(self, a_path, suffixes):
		self.path = a_path
		self.extension = suffixes

	def add_suffix(self, suffix):
		self.extension.append(suffix)

	@property
	def extension(self):
		"""
		The extension that the checked path is supposed to have, stored as a
		list of suffixes. For example, a PDF file's suffix list is ['.pdf']; a
		Linux archive file's suffix list can be ['.tar', '.gz']. Every
		extension must start with a '.'. The suffixes can be given in a tuple.
		If this property is set to None, it will be and empty list.
		"""
		return self._extension

	@extension.setter
	def extension(self, suffixes):
		if suffixes is None:
			self._extension = []
		else:
			self._extension = list(suffixes)

	def extension_is_correct(self):
		return self._path.suffixes == self.extension

	def extension_to_str(self):
		return "".join(self.extension)

	def get_file_name(self, with_ext):
		if not self.path_is_file():
			return ""

		file_name = self.path.name

		if not with_ext:
			ext_index = file_name.index(self.path.suffixes[0])
			file_name = file_name[:ext_index]

		return file_name

	def make_file_stem(self, before_stem=None, after_stem=None):
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
			raise ValueError(
				"a_path must be an instance of str or Pathlib's class Path.")

	def path_exists(self):
		return self.path.exists()

	def path_is_dir(self):
		return self.path.is_dir()

	def path_is_file(self):
		return self.path.is_file()

	def remove_suffix(self, suffix):
		try:
			self.extension.remove(suffix)
			return True
		except ValueError:
			return False

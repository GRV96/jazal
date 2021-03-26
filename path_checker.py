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
		Linux archive file's suffix list is ['.tar', '.gz']. Every extension
		must start with a '.'. The suffixes can be given in a tuple. If this
		property is set to None, it will be and empty list.
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
		ext_str = ""

		for suffix in self.extension:
			ext_str += suffix

		return ext_str

	def get_file_name(self, with_ext):
		if not path.is_file():
			return ""

		file_name = self.path.name

		if not with_ext:
			ext_index = file_name.index(path.suffixes[0])
			file_name = file_name[:ext_index]

		return file_name

	@property
	def path(self):
		"""
		The path that this object checks, stored as a Pathlib Path object
		"""
		return self._path

	@path.setter
	def path(self, a_path):
		self._path = a_path

	def path_exists(self):
		return self._path.exists()

	def path_is_dir(self):
		return self._path.is_dir()

	def path_is_file(self):
		return self._path.is_file()

	def remove_suffix(self, suffix):
		try:
			self.extension.remove(suffix)
		except ValueError:
			pass

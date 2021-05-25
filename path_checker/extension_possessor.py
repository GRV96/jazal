class ExtensionPossessor:
	"""
	This class's sole purpose is to contain a file extension as a tuple of
	strings called suffixes. All suffixes must be such as those returned by
	pathlib.Path's property suffixes. For example, a PDF file's suffix tuple
	is ('.pdf',); a Linux archive's suffix tuple can be ('.tar', '.gz'). Every
	suffix starts with '.'. This class is meant to be inherited from rather
	than instantiated.
	"""

	def __init__(self, suffixes):
		"""
		The constructor only requires the suffixes that make the extension.
		Make sure that each suffix conforms to the description from the class
		documentation.

		Args:
			suffixes (list or tuple): They must make a file name extension. If
			None, the extension will be an empty tuple.

		Raises:
			TypeError: if argument suffixes is not None, nor a list or a tuple
		"""
		self._set_extension(suffixes)

	@property
	def extension(self):
		"""
		This read-only property is the file extension that this object
		contains.
		"""
		return self._extension

	def extension_to_str(self):
		"""
		Concatenates the suffixes that make property extension.

		Returns:
			str: extension as one string
		"""
		return "".join(self.extension)

	def _set_extension(self, suffixes):
		"""
		Sets the extension that this object contains. If it is set to None,
		the extension will be an empty tuple.

		Args:
			suffixes (list or tuple): They must make a file name extension.

		Raises:
			TypeError: if argument suffixes is not None, nor a list or a tuple
		"""
		if suffixes is None:
			self._extension = ()

		elif isinstance(suffixes, tuple):
			self._extension = suffixes

		elif isinstance(suffixes, list):
			self._extension = tuple(suffixes)

		else:
			raise TypeError(
				"The extension must be None or a list or tuple of suffixes.")

"""
If a script or a function requires a path as an argument, it probably needs to
cope with missing and invalid paths. The functions in this module allow to
make default values for this purpose.
"""


def make_default_file_name(stem_source, exten_source,
		before_stem=None, after_stem=None):
	"""
	Creates a file name by adding a string at the beginning and/or the end of
	a given file stem and appending the given extension to the new stem. This
	function allows to create a file name from two PathCheckers. The returned
	file name can be used as a default value if a path is missing or invalid.

	Args:
		stem_source (PathChecker): contains the file stem.
		exten_source (PathChecker): contains the file extension.
		before_stem (str): the string to add to the file stem's beginning. If
			it is None, nothing is added to the stem's beginning. Defaults to
			None.
		after_stem (str): the string to add to the file stem's end. If it is
			None, nothing is added to the stem's end. Defaults to None.

	Returns:
		str: the file name described above
	"""
	extension = exten_source.extension_to_str()
	return stem_source.make_altered_name(before_stem, after_stem, extension)


def make_default_path(stem_source, exten_source,
		before_stem=None, after_stem=None):
	"""
	Creates a path by adding a string at the beginning and/or the end of a
	given file stem and appending the given extension to the new stem. This
	function allows to create a path from two PathCheckers. The returned path
	can be used as a default value if a path is missing or invalid.

	Args:
		stem_source (PathChecker): contains the file stem.
		exten_source (PathChecker): contains the file extension.
		before_stem (str): the string to add to the file stem's beginning. If
			it is None, nothing is added to the stem's beginning. Defaults to
			None.
		after_stem (str): the string to add to the file stem's end. If it is
			None, nothing is added to the stem's end. Defaults to None.

	Returns:
		pathlib.Path: the path described above
	"""
	name = make_default_file_name(stem_source, exten_source,
		before_stem, after_stem)

	return stem_source.path.parents[0]/name

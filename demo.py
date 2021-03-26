from path_checker import PathChecker
from pathlib import Path
from sys import argv, exit


_PDF_EXTENSION = ".pdf"
_PDF_EXTENSION_IN_LIST = [_PDF_EXTENSION]
_TXT_EXTENSION = ".txt"
_TXT_EXTENSION_IN_LIST = [_TXT_EXTENSION]


def _make_default_output_file_name(input_path):
	return _make_default_output_file_stem(input_path) + _TXT_EXTENSION


def _make_default_output_file_stem(input_path):
	return input_path.stem + "_file_name"


if __name__ == "__main__":

	# Input path checks
	try:
		input_path = Path(argv[1])
		input_chekcer = PathChecker(input_path, [_PDF_EXTENSION])

	except IndexError:
		print("ERROR! The path to a " + _PDF_EXTENSION
			+ " file must be provided as the first argument.")
		exit()

	if not input_chekcer.path_exists():
		print("ERROR! " + str(input_path) + " does not exist.")
		exit()

	if not input_chekcer.extension_is_correct(): # False if not a file
		print("ERROR! The first argument must be the path to a "
			+ _PDF_EXTENSION + " file.")
		exit()

	# Output path checks
	try:
		output_path = Path(argv[2])
		output_checker = PathChecker(output_path, [_TXT_EXTENSION])

		if output_checker.path_is_dir():
			output_path = output_path/_make_default_output_file_name(input_path)

		elif not output_checker.extension_is_correct():
			output_path = output_path.with_suffix(_TXT_EXTENSION)

	except IndexError:
		output_path = input_path.with_name(
			_make_default_output_file_name(input_path))

	# Real work
	input_file_name = input_path.name
	with output_path.open(mode="w") as output_stream:
		output_stream.write("File name is " + input_file_name + ".")

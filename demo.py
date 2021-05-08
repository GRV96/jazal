from path_checker import PathChecker
from pathlib import Path
from sys import argv, exit


_PDF_EXTENSION = ".pdf"
_TXT_EXTENSION = ".txt"


if __name__ == "__main__":
	# Input path checks
	try:
		input_path = Path(argv[1])
		input_checker = PathChecker(input_path, [_PDF_EXTENSION])

	except IndexError:
		print("ERROR! The path to a file with the extension " + _PDF_EXTENSION
			+ " must be provided as the first argument.")
		exit()

	if not input_checker.path_exists():
		print("ERROR! " + str(input_path) + " does not exist.")
		exit()

	if not input_checker.extension_is_correct(): # False if not a file
		print("ERROR! The first argument must be the "
			+ "path to a file with the extension "
			+ input_checker.extension_to_str() + ".")
		exit()

	# Output path checks
	try:
		output_path = Path(argv[2])
		output_checker = PathChecker(output_path, [_TXT_EXTENSION])

		if output_checker.path_is_dir():
			output_path = output_path/(
				input_checker.make_file_stem(after_stem="_file_name")
				+ output_checker.extension_to_str())

		elif not output_checker.extension_is_correct():
			output_path = output_path.with_suffix(_TXT_EXTENSION)

	except IndexError:
		output_path = input_path.with_name(
			input_checker.make_file_stem(after_stem="_file_name")
			+ _TXT_EXTENSION)

	# Real work
	input_file_name = input_path.name
	with output_path.open(mode="w") as output_stream:
		output_stream.write("File name is " + input_file_name + ".")

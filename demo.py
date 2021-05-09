from arg_output_path_checker import ArgOutputPathChecker
from arg_path_checker import ArgPathChecker
from path_checker import PathChecker
from pathlib import Path

from sys import argv, exit


if __name__ == "__main__":
	ERROR_INTRO = "ERROR! "
	TXT_EXTENSION = ".txt"

	# Input path checks
	try:
		input_checker = ArgPathChecker(None, [".pdf"], "Argument 1")
		input_path = Path(argv[1])
		input_checker.path = input_path

		input_checker.check_path_exists()
		input_checker.check_extension_correct()

	except IndexError:
		print(ERROR_INTRO + input_checker.make_missing_arg_msg())
		exit()

	except Exception as e:
		print(ERROR_INTRO + str(e))
		exit()

	# Output path checks
	try:
		output_path = Path(argv[2])
		output_checker = PathChecker(output_path, [TXT_EXTENSION])

		if output_checker.path_is_dir():
			output_path = output_path/(
				input_checker.make_file_stem(after_stem="_file_name")
				+ output_checker.extension_to_str())

		elif not output_checker.extension_is_correct():
			output_path = output_path.with_suffix(TXT_EXTENSION)

	except IndexError:
		output_path = input_path.with_name(
			input_checker.make_file_stem(after_stem="_file_name")
			+ TXT_EXTENSION)

	# Real work
	input_file_name = input_path.name
	with output_path.open(mode="w") as output_stream:
		output_stream.write("File name is " + input_file_name + ".")

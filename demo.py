from path_checker import\
	ArgPathChecker,\
	make_default_file_name,\
	make_default_path
from pathlib import Path
from sys import argv, exit


if __name__ == "__main__":
	AFTER_DFLT_STEM = "_file_name"
	ERROR_INTRO = "ERROR! "

	# Input path checks
	try:
		input_checker = ArgPathChecker(None, (".pdf",), "Argument 1")
		input_path = Path(argv[1]) # Can raise IndexError.
		# ArgPathChecker cannot work if the path is not set.
		input_checker.path = input_path

		input_checker.check_path_exists() # Can raise FileNotFoundError.
		input_checker.check_extension_correct() # Can raise ValueError.

	except IndexError:
		# Argument 1 not given
		print(ERROR_INTRO + input_checker.make_missing_arg_msg())
		exit()

	except Exception as e:
		print(ERROR_INTRO + str(e))
		exit()

	# Output path checks
	try:
		output_checker = ArgPathChecker(None, (".txt",), "Argument 2")
		output_path = Path(argv[2]) # Can raise IndexError.
		# ArgPathChecker cannot work if the path is not set.
		output_checker.path = output_path

		if output_checker.path_is_dir():
			output_path = output_path/make_default_file_name(
				input_checker, output_checker, after_stem=AFTER_DFLT_STEM)

		elif not output_checker.extension_is_correct():
			output_path = output_checker.path_with_correct_exten()

	except IndexError:
		# Argument 2 not given
		output_path = make_default_path(
			input_checker, output_checker, after_stem=AFTER_DFLT_STEM)

	# Real work
	input_file_name = input_path.name
	with output_path.open(mode="w") as output_stream:
		output_stream.write("File name is " + input_file_name + ".")

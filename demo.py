from path_checker import\
	ArgPathChecker,\
	MissingArgPathWarner,\
	make_altered_name,\
	make_altered_path
from pathlib import Path
from sys import argv, exit


if __name__ == "__main__":
	AFTER_DFLT_STEM = "_file_name"
	ERROR_INTRO = "ERROR! "

	# Input path checks
	missing_in_warner = MissingArgPathWarner("Argument 1", (".pdf",))
	try:
		input_path = Path(argv[1]) # Can raise an IndexError.
		input_checker = missing_in_warner.make_arg_path_checker(input_path)

		input_checker.check_path_exists() # Can raise a FileNotFoundError.
		input_checker.check_extension_correct() # Can raise a ValueError.

	except IndexError:
		# Argument 1 not given
		print(ERROR_INTRO + missing_in_warner.make_missing_arg_msg())
		exit()

	except Exception as e:
		print(ERROR_INTRO + str(e))
		exit()

	# Output path checks
	missing_out_warner = MissingArgPathWarner("Argument 2", (".txt",))
	try:
		output_path = Path(argv[2]) # Can raise an IndexError.
		output_checker = missing_out_warner.make_arg_path_checker(output_path)

		if output_checker.path_is_dir():
			output_path = output_path/make_altered_name(
				input_path, after_stem=AFTER_DFLT_STEM,
				extension=output_checker.extension_to_str())

		elif not output_checker.extension_is_correct():
			output_path = output_checker.path_with_correct_exten()

	except IndexError:
		# Argument 2 not given
		output_path = make_altered_path(input_path, after_stem=AFTER_DFLT_STEM,
			extension=missing_out_warner.extension_to_str())

	# Real work
	input_file_name = input_path.name
	with output_path.open(mode="w") as output_stream:
		output_stream.write("File name is " + input_file_name + ".")

from jazal import\
	MissingPathArgWarner,\
	make_altered_name,\
	make_altered_path
from pathlib import Path
from sys import argv, exit


if __name__ == "__main__":
	AFTER_DFLT_STEM = "_file_name"
	ERROR_INTRO = "ERROR! "

	# Argument 1: a .pdf file
	# Argument 2: a .txt file that will contain the result

	# INPUT PATH CHECKS

	# This object warns the user if the path is not given.
	missing_in_warner = MissingPathArgWarner("Argument 1", ".pdf")
	try:
		input_path = Path(argv[1]) # Can raise an IndexError.

		# A checker is created with the path and the data stored in the warner.
		input_checker =\
			missing_in_warner.make_reactive_path_checker(input_path)

		# If necessary, the checker raises an
		# exeption with an explicit message.
		input_checker.check_path_exists() # Can raise a FileNotFoundError.
		input_checker.check_extension_correct() # Can raise a ValueError.

	except IndexError:
		# The warner makes an explicit message if argument 1 was not given.
		print(ERROR_INTRO + missing_in_warner.make_missing_arg_msg())
		exit()

	except Exception as e:
		print(ERROR_INTRO + str(e))
		exit()

	# OUTPUT PATH CHECKS

	# If no output path is given, the warner can serve another purpose.
	missing_out_warner = MissingPathArgWarner("Argument 2", ".txt")
	try:
		output_path = Path(argv[2]) # Can raise an IndexError.

		# A checker is created with the path and the data stored in the warner.
		output_checker =\
			missing_out_warner.make_reactive_path_checker(output_path)

		if output_checker.path_is_dir():
			# A default file name is appended to the de directory's path.
			output_path = output_path/make_altered_name(
				input_path, after_stem=AFTER_DFLT_STEM,
				extension=output_checker.extension_to_str())

		elif not output_checker.extension_is_correct():
			# The invalid extension is replaced by a valid one.
			output_path = output_checker.path_with_correct_exten()

	except IndexError:
		# The warner provides the needed extension to make the output path.
		output_path = make_altered_path(input_path, after_stem=AFTER_DFLT_STEM,
			extension=missing_out_warner.extension_to_str())

	# REAL WORK
	input_file_name = input_path.name
	with output_path.open(mode="w") as output_stream:
		output_stream.write("The file name is " + input_file_name + ".")

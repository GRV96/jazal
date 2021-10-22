from jazal import\
	MissingPathArgWarner,\
	make_altered_name,\
	make_altered_path
from pathlib import Path
from sys import argv, exit


def make_file_count_msg(explored_dir, file_count):
	msg_end = " files." if abs(file_count) >= 2 else " file."

	return "Directory " + str(explored_dir) + " contains "\
		+ str(file_count) + msg_end


if __name__ == "__main__":
	AFTER_DFLT_STEM = "_file_count"
	ERROR_INTRO = "ERROR! "

	# This script counts the files contained in the directory specified by the
	# first argument. The number is written in a text file generated in the
	# directory specified by the second argument.
	# Argument 1: the explored directory
	# Argument 2: the directory that will contain the result

	# INPUT PATH CHECKS

	# This object warns the user if the path is not given.
	missing_in_warner = MissingPathArgWarner("Argument 1", "")
	try:
		input_path = Path(argv[1]) # Can raise an IndexError.

		# A checker is created with the path and the data stored in the warner.
		input_checker =\
			missing_in_warner.make_reactive_path_checker(input_path)

		if not input_checker.path_is_dir():
			print(ERROR_INTRO
				+ input_checker.arg_name + " must be a directory.")
			exit(1)

		# If necessary, the checker raises an
		# exeption with an explicit message.
		input_checker.check_path_exists() # Can raise a FileNotFoundError.
		input_checker.check_extension_correct() # Can raise a ValueError.

	except IndexError:
		# The warner makes an explicit message if argument 1 was not given.
		print(ERROR_INTRO + missing_in_warner.make_missing_arg_msg())
		exit(1)

	except Exception as e:
		print(ERROR_INTRO + str(e))
		exit(1)

	# OUTPUT PATH CHECKS

	# If no output path is given, the warner can serve another purpose.
	missing_out_warner = MissingPathArgWarner("Argument 2", "")
	try:
		output_path = Path(argv[2]) # Can raise an IndexError.

		# A checker is created with the path and the data stored in the warner.
		output_checker =\
			missing_out_warner.make_reactive_path_checker(output_path)

		if not output_checker.extension_is_correct():
			# The invalid extension is replaced by a valid one.
			output_path = output_checker.path_with_correct_exten()

	except IndexError:
		# The warner provides the needed extension to make the output path.
		output_path = make_altered_path(input_path, after_stem=AFTER_DFLT_STEM,
			extension=missing_out_warner.extension)

	# REAL WORK
	file_count = len(list(input_path.glob("*")))

	if not output_path.exists():
		output_path.mkdir(exist_ok=True)

	output_file_name = input_path.name + AFTER_DFLT_STEM + ".txt"
	with (output_path/output_file_name).open(mode="w") as output_stream:
		output_stream.write(make_file_count_msg(input_path, file_count))

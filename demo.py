from pathlib import Path
from sys import argv, exit


_PDF_EXTENSION = ".pdf"
_PDF_EXTENSION_IN_LIST = [_PDF_EXTENSION]
_TXT_EXTENSION = ".txt"
_TXT_EXTENSION_IN_LIST = [_TXT_EXTENSION]


class PdfField:
	def __init__(self, name, val_type, value):
		self.name = name
		self.val_type = val_type
		self.value = value

	def __str__(self):
		return self.name + " (" + str(self.val_type) + "): " + str(self.value)


def get_pdf_field_list(pdf_reader):
	pdf_fields = pdf_reader.getFields()
	if pdf_fields is None:
		return None

	field_list = list()
	for mapping_name, field in pdf_fields.items():
		field_list.append(PdfField(mapping_name, field.fieldType, field.value))

	return field_list


def _make_default_output_file_name(input_path):
	return _make_default_output_file_stem(input_path) + _TXT_EXTENSION


def _make_default_output_file_stem(input_path):
	return input_path.stem + "_file_name"


if __name__ == "__main__":

	# Input path checks
	try:
		input_path = Path(argv[1])
	except IndexError:
		print("ERROR! The path to a " + _PDF_EXTENSION
			+ " file must be provided as the first argument.")
		exit()

	if not input_path.exists():
		print("ERROR! " + str(input_path) + " does not exist.")
		exit()

	if input_path.suffixes != _PDF_EXTENSION_IN_LIST: # False if not a file
		print("ERROR! The first argument must be the path to a "
			+ _PDF_EXTENSION + " file.")
		exit()

	# Output path checks
	try:
		output_path = Path(argv[2])

		if output_path.is_dir():
			output_path = output_path/_make_default_output_file_name(input_path)

		elif output_path.suffixes != _TXT_EXTENSION_IN_LIST:
			output_path = output_path.with_suffix(_TXT_EXTENSION)

	except IndexError:
		output_path = input_path.with_name(
			_make_default_output_file_name(input_path))

	# Real work
	input_file_name = input_path.name
	with output_path.open(mode="w") as output_stream:
		output_stream.write("File name is " + input_file_name + ".")

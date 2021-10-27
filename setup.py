# References
# https://packaging.python.org/tutorials/packaging-projects/
# https://www.geeksforgeeks.org/how-to-publish-python-package-at-pypi-using-twine-module/
# https://stackoverflow.com/questions/45168408/creating-tar-gz-in-dist-folder-with-python-setup-py-install
# https://docs.python.org/3/distutils/sourcedist.html
# https://github.com/conda-incubator/grayskull


import setuptools


with open("README.md", "r", encoding="utf-8") as readme_stream:
	long_description = readme_stream.read()

setuptools.setup(
	name = "jazal",
	version = "2.0.0",
	author = "Guyllaume Rousseau",
	description = "Jazal performs certain verifications on file paths before a function or a script uses them.",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	url = "https://github.com/GRV96/jazal",
	classifiers = [
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Topic :: Utilities"
	],
	packages = setuptools.find_packages(),
	license = "MIT",
	license_files = ("LICENSE",)
)

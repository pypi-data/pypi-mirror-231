# References
# https://packaging.python.org/tutorials/packaging-projects/
# https://www.geeksforgeeks.org/how-to-publish-python-package-at-pypi-using-twine-module/
# https://stackoverflow.com/questions/45168408/creating-tar-gz-in-dist-folder-with-python-setup-py-install
# https://docs.python.org/3/distutils/sourcedist.html
# https://github.com/conda-incubator/grayskull
# https://setuptools.pypa.io/en/latest/userguide/datafiles.html
# https://packaging.python.org/en/latest/guides/using-manifest-in/


import setuptools


_ENCODING_UTF8 = "utf-8"
_MODE_R = "r"

_README = "README.md"


def _make_long_description():
	with open(_README, _MODE_R, encoding=_ENCODING_UTF8) as readme_file:
		long_description = readme_file.read()

	start_index = long_description.index("## FRANÇAIS")

	return long_description[start_index:]


if __name__ == "__main__":
	setuptools.setup(
		name = "repr_rw",
		version = "1.0.0",
		author = "Guyllaume Rousseau",
		description = "This library writes Python object representations in a text file and reads the file to recreate the objects. An object representation is a string returned by function repr.",
		long_description = _make_long_description(),
		long_description_content_type = "text/markdown",
		url = "https://github.com/GRV96/repr_rw",
		classifiers = [
			"Development Status :: 5 - Production/Stable",
			"Intended Audience :: Developers",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
			"Programming Language :: Python :: 3",
			"Topic :: Software Development :: Libraries :: Python Modules",
			"Topic :: Utilities"
		],
		packages = setuptools.find_packages(exclude=("demo_package",)),
		license = "MIT",
		license_files = ("LICENSE",))

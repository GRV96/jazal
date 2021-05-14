# path_checker

Before an application uses a path to a file, Python class PathChecker and its
subclass ArgPathChecker can verify whether the path has the right extension,
whether it exists and whether it is a directory or a file. In addition,
ArgPathChecker can warn the user about invalid paths and make correct ones.
These two classes require pathlib.Path in order to work. This library also
provides functions that make default values for missing or invalid paths.

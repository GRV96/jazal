# Jazal

Before an application uses a path to a file, it may be important to verify
whether it has the right extension, whether it exists and whether it is a
directory or a file. For this purpose, library Jazal provides class PathChecker
and its subclass ReactivePathChecker. The latter is also able to warn the user
about invalid paths and make correct ones. These two classes require
pathlib.Path in order to work. Jazal also offers functions that make default
values for missing or invalid paths.

See script demo.py to know how to use Jazal's content.

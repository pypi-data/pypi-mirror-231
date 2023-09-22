INSTRUCTIONS = """

OpenAI error:

    missing `{library}`

This feature requires additional dependencies:

    $ pip install ayenaspring[datalib]

"""

NUMPY_INSTRUCTIONS = INSTRUCTIONS.format(library="numpy")


class MissingDependencyError(Exception):
    pass

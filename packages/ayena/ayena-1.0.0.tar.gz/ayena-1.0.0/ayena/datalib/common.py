INSTRUCTIONS = """

OpenAI error:

    missing `{library}`

This feature requires additional dependencies:

    $ pip install ayena[datalib]

"""

NUMPY_INSTRUCTIONS = INSTRUCTIONS.format(library="numpy")


class MissingDependencyError(Exception):
    pass

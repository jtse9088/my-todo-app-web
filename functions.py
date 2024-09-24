FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH): # default argument in function
    """ # Example of a docstring to explain the function
    Retrieves a list of to-do items from a specified file.

    This function opens a file containing to-do items, reads its contents, and returns the items as a list of strings.
    If no file path is provided, it defaults to "todos.txt".

    Args:
        filepath (str): The path to the file containing to-do items. Defaults to "todos.txt".

    Returns:
        list: A list of to-do items read from the file.
    """

    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()  # returns a list
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH): # non default argument needs to be before default argument
    """
    Writes a list of to-do items to a specified file.

    This function takes a list of to-do items and writes them to a file, overwriting any existing content. If no file
    path is provided, it defaults to "todos.txt".

    Args:
        todos_arg (list): A list of to-do items to be written to the file.
        filepath (str): The path to the file where to-do items will be saved. Defaults to "todos.txt".

    Returns:
        None
    """

    with open(filepath, 'w') as file:
        file.writelines(todos_arg)  # overwriting the entire file


if __name__ == "__main__": # only prints if you run functions.py directly but not when imported from cli.py
    print("Hello")
    print(get_todos())
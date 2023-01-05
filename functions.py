def get_todos(filepath="todos.txt"):
    """Read a text file and return list of to-do items """
    with open(filepath, "r", encoding="utf-8") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """Write to-do items list in the text file"""
    with open(filepath, "w", encoding="utf-8") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello from functions")

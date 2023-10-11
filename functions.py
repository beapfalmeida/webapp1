def get_todos(filepath='todos.txt'):
    """ Read text file and return the list of todo items """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath='todos.txt'):       # (onde escrevo, o que escrevo)
    """ Write in the text file the new todo items """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)



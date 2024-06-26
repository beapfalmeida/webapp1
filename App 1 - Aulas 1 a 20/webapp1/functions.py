def get_todos(filepath='todos.txt'):
    """ Read text file and return the list of todo items """
    with open(filepath, 'r', encoding='iso-8859-1') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath='todos.txt'):       # (onde escrevo, o que escrevo)
    """ Write in the text file the new todo items """
    with open(filepath, 'w', encoding='iso-8859-1') as file:
        file.writelines(todos_arg)



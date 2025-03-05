class filestuff: #fs is short for FILESTUFF

    FILEPATH="todos.txt"

    def writeChanges(mylist , filepath=FILEPATH):
        """Used to write changes to the file by passing it a list"""
        with open(filepath, 'w') as file:
           file.writelines(mylist)


    def loadexisting(filepath=FILEPATH):
        """Returns a list by reading items from a file"""
        with open(filepath, 'r') as file:
            todos = file.readlines()
        return todos

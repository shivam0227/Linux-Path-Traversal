# root list
root = ["", "root"]
# directory list
dir_list = []
# path list
path_list = []
# current path list
curr_path_list = [] or ["", "root"]


# function to change directory from current directory to desired directory using command cd
def cd():
    global curr_path_list, dir, path_list
    # check if directory list is empty than we are on root directory
    if dir == "":
        curr_path_list = root
        path_list = root
        print("you are succesfully enter into root directory")
    # check if directory list has some item than we are move on to desire directory
    elif dir in dir_list:
        curr_path_list.append(dir)
        path_list.clear()
        print("Sucessfully enter into directory")
    # any invalid path name will print directory doesn't exist
    else:
        print("Directory doesn't exist.")


# function to create directory using command mkdir
def mkdir():
    global dir_list
    # checking if directory is already exist or not
    if dir in dir_list:
        print("Directory already exist.")
    else:
        # add directory to directory list
        dir_list.append(dir)
        # add directory to path list
        path_list.append(dir)
        print("Directory created if command is correct.")


# function to remove or delete directory using command rm
def rm():
    global dir_list
    # check if directory is avilable in directory list than remove it otherwise print directory does not exist
    if dir in dir_list:
        dir_list.remove(dir)
        print("Directory sucessfully deleted or removed.")
    else:
        print("Directory does not exist can't be deleted.")


# function to print directory using command pwd
def pwd():
    global curr_path_list
    print(*curr_path_list, sep="/")


# function to list directory using command ls
def ls():
    global path_list
   # checking the length of path_list
    if len(path_list) == 0:
        print("no directory is available or created")
    else:
        print(*path_list, sep="\n")


# function to clear all the previous operations & put back the application to starting point using command session clear
def session_clear():
    global dir_list
    # clear directory list
    dir_list.clear()
    global curr_path_list
    # clear current path list and set it to root
    curr_path_list.clear()
    curr_path_list = root
    global path_list
    # clear path list
    path_list.clear()


# function to execute all the function together
def commands(arguments):
    # create dictionary for commands
    command = {
        "mkdir": mkdir,
        "ls": ls,
        "cd": cd,
        "pwd": pwd,
        "rm": rm,
        "session_clear": session_clear,
    }
    # check whether the value is in comm dictionary or not
    if value in command:
        # Get the function from comm dictionary
        function_to_run = command.get(arguments)
        # Execute the function
        function_to_run()
    else:
        print("command does not exist!")


print("Choose from: mkdir, ls, cd, pwd, rm, session_clear")

while True:
    # take input from user
    value = input("$: ")
    # create a list and append the input value in it
    a = []
    a.append(value.split(" "))
    value = a[0][0]
    # check if mkdir and rm command have there operand or not
    if value in ["mkdir", "rm"] and len(a[0]) == 1:
        print("{}:missing operand".format(value))
    elif len(a[0]) == 1:
        dir = ""
    elif len(a[0]) == 2:
        dir = a[0][1]
    else:
        print("Invalid Syntax")
    commands(value)

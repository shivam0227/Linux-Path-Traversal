LINUX PATH TRAVERSAL:
this task is to create an application which does
a Linux Path Traversal.
using the various Linux commands, as follows.
•	cd <path>
•	mkdir <path>
•	rm <path>
•	pwd
•	ls
•	session_clear

this program is will do logical tracking of directories in a running session

in this program we create functions for each command.

• the function cd is for changing the directory in this we check if dir is empty or not
if dir is empty than we are on root directory if dir consist some dir from the directory list
than we add that dir to current path list.


• the function mkdir is to create the directory in this we create the directory first we check if
directory is already exist or not if already exis than we print "directory already exist". if not
than we create that directory by adding it to directory list.

• the function rm is to remove the directory in this we remove the directory first we check if
directory is exist or not if exis than we remove that directory from the directory list. if not
than we print "Directory does not exist can't be deleted.

• the function pwd is use to print the current path.

• the function ls is use to print the list of all the directory at the current directory first we
checking if the path list lenght is 0 than we print no directory is created. else we print the path list.

• the function session_clear It will clear all the previous operations and put back the application to
starting point, as if application started just now.

than we create the main function "commands" with an argument and inside it
create the dictionary in which assign the above functions to the keys. than we check the input which is enter
by the user is member of dictionary or not if yes than we pass that input to the function as an argument
if no than we print command does not exist.
after taking the input from user we add it to the list and check for some commands like mkdir and rm that
they have their operand or not if yes than proceed if no than we print command missing their operands

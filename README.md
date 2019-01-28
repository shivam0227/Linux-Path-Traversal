LINUX PATH TRAVERSAL	
Task is to create an application which does a Linux Path Traversal. You would be implementing various Linux commands, as follows.
•	cd <path>
•	mkdir <path>
•	rm <path>
•	pwd
•	ls
There would be an additional command, for application purpose, which is
•	session clear
It will clear all the previous operations and put back the application to starting point, as if application started just now.
Problem will have a command line environment, where testing input would be as command line input. 
 
	“Above is just a representation. Basically, your application must keep running and keep accepting user input and keep providing outputs.

At start, application would be at ROOT directory ‘/’. Overtime, application would be provided with various commands, your task is to successfully work on commands if there is a scope or throw error message.
You would provide us source code as well as executable binary of your application, so it could be run from command line as shown in the picture.
We don’t want you to ‘actually’ create/remove real directories (using OS functions). Your application should keep a logical track of directories in a running session.
Examples:
	Following is in ordered way. 
$ <Starting your application...>
$ pwd
	PATH: /
$ cd /some/random/path/which/doesn’t/exist
	ERR: INVALID PATH
$ mkdir dir1
	SUCC: CREATED
$ mkdir dir1
	ERR: DIRECTORY ALREADY EXISTS
$ mkdir dir2
	SUCC: CREATED
$ ls
	DIRS: dir1	dir2

$ cd dir1
	SUCC: REACHED
$ pwd
	PATH: /dir1
$ cd /
	SUCC: REACHED
$ rm /dir1
	SUCC: DELETED
$ cd /dir1
	ERR: INVALID PATH
$ mkdir /dir3
	SUCC: CREATED
$ cd /dir2
	SUCC: REACHED
$ pwd
	PATH: /dir2
$ session clear
	SUCC: CLEARED: RESET TO ROOT
$ pwd
	PATH: /
$ asdf asdf
	ERR: CANNOT RECOGNIZE INPUT.
NOTE: You can give absolute path as well as relative path. Means- if you are at path /root/abc/ so you can give dir as well as /root/abc/dir

APPLICATION EVALUATION PARAMETERS	

Your application would be evaluated on following parameters.
•	Code quality, we prefer Object Oriented architecture.
•	Appropriately commented
•	How extendable your code is. You could be asked to add support for additional commands.
•	Corner cases handling and proper success/error message outputs.

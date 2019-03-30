# pygrader

The autograder "check.py" only works in a Linux environment. I use cloud9 which is free to schools and provides virtual Linux machines for each student. The grader is designed for my curriculum I've been developing specifically for a Python class or AP Computer Science Principles.

check.py is written in python 3 and therefore must be used in a python3 environment. You can do this simply in cloud9 by typing "python3 filename.py" at the prompt to override the default python2.

You must install the "pexpect" library for the grader to work properly. You can do this by typing "sudo pip3 install pexpect" at the Linux terminal prompt.

The "check.py" program must be installed on the student's workspace (working directory).

The grader is designed around specific problem sets I have written and or borrowed/copied from resources such as books, CS50...

The grader uses command line arguments to determine which problem set to check. Around line 95 you will see a selector of "options"; these options are the files it looks for and are names of specific problem sets.

Here is an example:
I want to check "greedy.py"
I would type "python3 grader.py greedy.py"
python3 calls the interpreter, grader.py the first argument calls the grader file, greedy.py the second argument is passed to grader to evaluate

I am working on converting the problem sets to PDF which I can host here as well. 

Students can game the system if they can understand the source code. I am OK with that. IMO if they can do that then they are A+ students.

Here is an example page of work my students have created. https://cacsd.github.io/apcsp/student_work.html

Email me if you have any questions or would like a demo. 
pietrofesar@gmail.com
Rocco Pietrofesa


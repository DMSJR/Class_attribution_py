# Class_attribution_py
Code for attributing classes to teachers
This program attributes classes to teachers in such a manner that there's no schedule conflict and teacher cannot teach a class they teached last semester.
It's an adaptation from the other repository, coded in C++.

The input file should respect the following structure:

first line: blank
next lines: name of teacher, followed by integers representing classes taught in the previous semester, one each line.
"?" after information about each teacher.

"*" to begin the information about the schedule of each class. The classes that occur at the same time should be in following lines, with a ? to begin the next time.
"*" to begin direct attribution of classes to teachers. Write the name, followed by the number of the classes, finish information about a teacher with a "?". 
In this part of the code it's essential that the teachers follow the same order as in the beggining of file.

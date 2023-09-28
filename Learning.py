Python 3.10.12 (main, Jun 11 2023, 05:26:28) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
print("Hello, World!")
Hello, World!
"42" + 2
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#1>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
'42' + 3
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#2>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> clear
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#3>", line 1, in <module>
NameError: name 'clear' is not defined
>>> 
=============================================== RESTART: Shell ==============================================
>>> 2+2
4
>>> 4
4
>>> 2**3
8
>>> 15%7
1
>>> 15//7
2
>>> 22//7
3
>>> 5 +
SyntaxError: incomplete input
>>> 5 + *2
SyntaxError: invalid syntax
>>> "Hello
SyntaxError: incomplete input
>>> "Ahmed " * 2
'Ahmed Ahmed '
>>> spam = 40
>>> spam
40
\
>>> eggs = 2
>>> spam + eggs
42
>>> spam + eggs * 2
44
>>> spam = spam + 2
>>> spam
42
>>> spam = 40
>>> spam
40
>>> spam+=
SyntaxError: incomplete input
>>> spam += spam
>>> spam
80
>>> spam-=spam
>>> spam
0

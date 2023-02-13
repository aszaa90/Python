Python 3.9.13 (main, Aug 25 2022, 23:51:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Using input statement
>>> welcome = input(Cześć, jak się nazywasz?)
SyntaxError: invalid syntax
>>> welcome = input('Cześć, jak się nazywasz?')
Cześć, jak się nazywasz? Asia
>>> pritn('Hello ' + welcome)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    pritn('Hello ' + welcome)
NameError: name 'pritn' is not defined
>>> print('Hello ' + welcome)
Hello  Asia
>>> 
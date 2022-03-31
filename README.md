# py_encapsulated

I made this decorator, because I wanted to enforce private, protected, and public class members in Python

This is a decorator to enforce private, protected and public access on class members in python
Just, use it and name your private variables, with "__" at the front,
your protected variables with "_" at the front,
and public variables with nothing at the front.
It works for class methods too.

Grab a copy, using git, like this:

git clone https://github.com/legitjimmyjalight/py_encapsulated

Example Usage

from encapsulated import encapsulated

# note, you have to put the brackets after encapsulated,
# because I didn't know how to make that unnecessary, maybe someone could teach me how
# 
# but, also if you put inside @encapsulated, strict=True, like this @encapsulated(strict=True)
# it will make the class strict, in the sense, that you can not dynamically add properties to it
#
# also, if you use the dataclass decorator,
# I found that you have to put the encapsulated decorator first or it bugs out, I don't know why
#
# This class might not work perfectly. I suggest you test it, to see how it works for you
#
# Also, if you think you can make this encapsulated decorator better,
# feel free to fork it and make your own gitrepos of it
#
@encapsulated()
class SomeClass:
     __aPrivateVar : int
     _aProtectedVar : float
     aPublicVar : str

     def __init__(self):
         self.__anotherPrivateVar = 1
         self._anotherProtectedVar = "foo"
         self.anotherPublicVar = {}

     def __aPrivateMethod(self):
         print("a private method")

     def _aProtectedMethod(self):
         print("a protected method")

     def aPublicMethod(self):
         print("a public method")

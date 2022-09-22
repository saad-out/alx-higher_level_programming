<img src="https://miro.medium.com/max/664/1*pA8a2yHULkxj-f1OPSDrrQ.png" width=430 height=230>

# 0x02-python-import_modules
## About
This is a directory for the **Python - import & modules** project's tasks, it covers *Python modules*
## Learning objectives
- Why Python programming is awesome
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function `dir()`
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs
## Requirements
All files are designed to be compiled/interpreted on `Ubuntu 20.04 LTS`
### Python Scripts
- Python 3
- Code should use the `pycodestyle (version 2.8.*)`
- First line `#!/usr/bin/python3`
## Tasks
1. [0-add.py](https://github.com/saad-out/alx-higher_level_programming/blob/main/0x02-python-import_modules/0-add.py): **Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`**
   * You have to use `print` function with string format to display integers
   * You have to assign:
     * the value `1` to a variable called `a`
     * the value `2` to a variable called `b`
     * and use those two variables as arguments when calling the functions `add` and `print`
   * `a` and `b` must be defined in 2 different lines: `a = 1` and another `b = 2`
   * Your program should print: `<a value> + <b value> = <add(a, b) value>` followed with a new line
   * You can only use the word `add_0` once in your code
   * You are not allowed to use `*` for importing or `__import__`
   * Your code should not be executed when imported - by using `__import__`, like the example below
   ```
   guillaume@ubuntu:~/0x02$ cat add_0.py
   #!/usr/bin/python3
   def add(a, b):
   """My addition function

   Args:
       a: first integer
       b: second integer
   
   Returns:
       The return value. a + b
   """
   return (a + b)
   
   guillaume@ubuntu:~/0x02$ ./0-add.py
   1 + 2 = 3
   guillaume@ubuntu:~/0x02$ cat 0-import_add.py
   __import__("0-add")
   guillaume@ubuntu:~/0x02$ python3 0-import_add.py 
   guillaume@ubuntu:~/0x02$ 
   ```
1. [1-calculation.py](https://github.com/saad-out/alx-higher_level_programming/blob/main/0x02-python-import_modules/1-calculation.py): **Write a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result.**
   * Do not use the function `print` (with string format to display integers) more than 4 times
   * You have to define:
     * the value `10` to a variable `a`
     * the value `5` to a variable `b`
     * and use those two variables only, as arguments when calling functions (including `print`)
   * `a` and `b` must be defined in 2 different lines: `a = 10` and another `b = 5`
   * Your program should call each of the imported functions. See example below for format
   * the word `calculator_1` should be used only once in your file
   * You are not allowed to use `*` for importing or `__import__`
   * Your code should not be executed when imported
   ```
   guillaume@ubuntu:~/0x02$ cat calculator_1.py
   #!/usr/bin/python3
   def add(a, b):
        """My addition function

        Args:
            a: first integer
            b: second integer

        Returns:
            The return value. a + b
        """
        return (a + b)


   def sub(a, b):
        """My subtraction function

        Args:
            a: first integer
            b: second integer

        Returns:
            The return value. a - b
        """
        return (a - b)


   def mul(a, b):
        """My multiplication function

        Args:
            a: first integer
            b: second integer

        Returns:
            The return value. a * b
        """
        return (a * b)


   def div(a, b):
        """My division function

        Args:
            a: first integer
            b: second integer

        Returns:
            The return value. a / b
        """
        return int(a / b)

   guillaume@ubuntu:~/0x02$ ./1-calculation.py
   10 + 5 = 15
   10 - 5 = 5
   10 * 5 = 50
   10 / 5 = 2
   guillaume@ubuntu:~/0x02$
   ```
1. [2-args.py](https://github.com/saad-out/alx-higher_level_programming/blob/main/0x02-python-import_modules/2-args.py): **Write a program that prints the number of and the list of its arguments.**
   * The output should be:
     * Number of argument(s) followed by `argument` (if number is one) or `arguments` (otherwise), followed by
     * `:` (or `.` if no arguments were passed) followed by
     * a new line, followed by (if at least one argument),
     * one line per argument:
       * the position of the argument (starting at 1) followed by `:`, followed by the argument value and a new line
   * Your code should not be executed when imported
   * The number of elements of `argv` can be retrieved by using: `len(argv)`
   * You do not have to fully understand lists yet, but imagine that `argv` can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.
   ```
   guillaume@ubuntu:~/0x02$ ./2-args.py 
   0 arguments.
   guillaume@ubuntu:~/0x02$ ./2-args.py Hello
   1 argument:
   1: Hello
   guillaume@ubuntu:~/0x02$ ./2-args.py Hello Welcome To The Best School
   6 arguments:
   1: Hello
   2: Welcome
   3: To
   4: The
   5: Best
   6: School
   guillaume@ubuntu:~/0x02$ 
   ```
1. [3-infinite_add.py](https://github.com/saad-out/alx-higher_level_programming/blob/main/0x02-python-import_modules/3-infinite_add.py): **Write a program that prints the result of the addition of all arguments**
   * The output should be the result of the addition of all arguments, followed by a new line
   * You can cast arguments into integers by using `int()` (you can assume that all arguments can be casted into integers)
   * Your code should not be executed when imported
   ```
   guillaume@ubuntu:~/0x02$ ./3-infinite_add.py
   0
   guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10
   89
   guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10 -40 -300 89 
   -162
   guillaume@ubuntu:~/0x02$ 
   ```
1. [4-hidden_discovery.py](https://github.com/saad-out/alx-higher_level_programming/blob/main/0x02-python-import_modules/4-hidden_discovery.py): **Write a program that prints all the names defined by the compiled module `hidden_4.pyc` (please download it locally).**
   * You should print one name per line, in alpha order
   * You should print only names that do **not** start with `__`
   * Your code should not be executed when imported
   * Make sure you are running your code in Python3.8.x (`hidden_4.pyc` has been compiled with this version)
   ```
   guillaume@ubuntu:~/0x02$ curl -Lso "hidden_4.pyc" "https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc"
   guillaume@ubuntu:~/0x02$ ./4-hidden_discovery.py | sort
   my_secret_santa
   print_hidden
   print_school
   guillaume@ubuntu:~/0x02$ 
   ```
1. [5-variable_load.py](https://github.com/saad-out/alx-higher_level_programming/blob/main/0x02-python-import_modules/5-variable_load.py): **Write a program that imports the variable `a` from the file `variable_load_5.py` and prints its value.**
   * ou are not allowed to use `*` for importing or `__import__`
   * Your code should not be executed when imported
   ```
   guillaume@ubuntu:~/0x02$ cat variable_load_5.py
   #!/usr/bin/python3
   a = 98
   """Simple variable
   """

   guillaume@ubuntu:~/0x02$ ./5-variable_load.py
   98
   guillaume@ubuntu:~/0x02$
   ```

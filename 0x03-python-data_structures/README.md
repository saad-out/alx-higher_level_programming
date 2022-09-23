<img src="https://www.simplilearn.com/ice9/free_resources_article_thumb/List_vs_Tuple.jpg" width=420 height=200>

# 0x03-python-data_structures
## About
This is a repository for the **Python - Data structures: Lists, Tuples** project's tasks, it covers *Lists* and *Tuples* data structures in *Python*
## Learning objectives
- Why Python programming is awesome
- What are lists and how to use them
- What are the differences and similarities between strings and lists
- What are the most common methods of lists and how to use them
- How to use lists as stacks and queues
- What are list comprehensions and how to use them
- What are tuples and how to use them
- When to use tuples versus lists
- What is a sequence
- What is tuple packing
- What is sequence unpacking
- What is the `del` and how to use it
## Requirements
All files are designed to be compiled/interpreted on `Ubuntu 20.04 LTS`
### Python Scripts
- Python 3
- Code should use the `pycodestyle (version 2.8.*)`
- First line `#!/usr/bin/python3`
### C scripts
- Compiled with `gcc` using the options `-Wall -Werror -Wextra -pedantic -std=gnu89`
- Code should use the `Betty` style
- No more than 5 functions per file
## Tasks
1. [0-print_list_integer.py](https://github.com/saad-out/alx-higher_level_programming/blob/main/0x03-python-data_structures/0-print_list_integer.py): **Write a function that prints all integers of a list.**
   * Prototype: `def print_list_integer(my_list=[]):`
   * Format: one integer per line. See example
   * You are not allowed to import any module
   * You can assume that the list only contains integers
   * You are not allowed to cast integers into strings
   * You have to use `str.format()` to print integers
```
guillaume@ubuntu:~/0x03$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./0-main.py
1
2
3
4
5
guillaume@ubuntu:~/0x03$ 
```

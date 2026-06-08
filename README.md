# Task tracker CLI

## **Requirements**

The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:

- Add, Update, and Delete tasks
- Mark a task as in progress or done
- List all tasks
- List all tasks that are done
- List all tasks that are not done
- List all tasks that are in progress

### Important Notes

1. Argparse module : **The `argparse` module** is Python's standard library tool for building user-friendly command-line interfaces (CLIs)
    - [prog](https://docs.python.org/3/library/argparse.html#prog) - The name of the program (default: generated from the `__main__` module attributes and `sys.argv[0]`)
    - [usage](https://docs.python.org/3/library/argparse.html#usage) - The string describing the program usage (default: generated from arguments added to parser)
    - [description](https://docs.python.org/3/library/argparse.html#description) - Text to display before the argument help (by default, no text)
    - [epilog](https://docs.python.org/3/library/argparse.html#epilog) - Text to display after the argument help (by default, no text)
        
        ```python
        parser = argparse.ArgumentParser(
        					prog='ProgramName',
        					description='What the program does',
        					epilog='Text at the bottom of help')
        ```
        
    1. Subparser : Main command is broken down into separate **sub-commands**, each with its own unique arguments
        
        ```python
        status_parser = subparser.add_parser("change-status", help = "update status of an existing task")
        status_parser.add_argument("id", type = int)
        status_parser.add_argument("status", type = str)
        ```
        
    2. The [`ArgumentParser.add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument) method attaches individual argument specifications to the parser. 
        
        ```python
        parser.add_argument('filename')           # positional argument
        parser.add_argument('-c', '--count')      # option that takes a value
        ```
        
2. OS module : It allows you to automate tasks involving files, directories, environment variables, and system commands natively across Windows, macOS, and Linux. 
**`os.path.exists(path)`**: Returns `True` if the path exists, otherwise `False`.

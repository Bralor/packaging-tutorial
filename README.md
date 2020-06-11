# Packaging projects with Python
## Create package folder
Inside this folder create file __\_\_init\_\_.py__:
```bash
$ mkdir my_package && touch my_package/__init__.py
```
Once you create this structure, you want to run all of the commands within the top-level folder (cd packaging_tutorial).

## Creating the package files
There is a list of [files](https://packaging.python.org/tutorials/packaging-projects/#creating-the-package-files) you should now add to the project:
```bash
packaging_tutorial
├── LICENSE
├── README.md
├── my_package
│   └── __init__.py
├── setup.py
└── tests
```

## Running the package
In the root directory run Python interpreter:
```bash
~/your/path/to/package/packaging-tutorial$ python
```

Import the package and then run the main function:
```bash
>>> import my_package.main as app
>>> app.my_func()

    Running the main file,
    TODAY: 2020-06-11 10:00:49.605398
    End of calling function
```
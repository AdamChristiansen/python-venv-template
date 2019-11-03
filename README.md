# Python Package Template

This template is used to create a Python package in a [virtual environment]
that can be tested with [tox].

The sample project that computes Fibonacci numbers is provided. It uses the
_`src` layout_ project structure, which is explained below:

- `.gitignore` is very important because many additionaly files will be created
  than are byproducts of other processes. If nothing else, this is useful for
  `git clean` before sharing the source.
- `requirements.txt` contains all of the dependencies that are required to be
  installed by `pip` for this package.
- `setup.py` is the `pip` configuration file that tells it how to distribute
  the package. This should be updated with the package information. Even if the
  package is not going to be distributed through `pip`, `tox` still requires
  this file.
- `tox.ini` is the file that describes the tox testing environment.
- `src` contains individual Python packages.
  - `conftest.py` is an empty file to tell `pytest` to import packages from
    this directory.
  - `fib` is the package that is provided by this project.
    - `__init__.py` is used if this package is a library (it can be both a
      library and a binary simultaneously).
    - `__main__.py` is used if this package is a binary (it can be both a
      library and a binary simultaneously).
    - `...` also include the rest of the project files, so generally other
      `.py` files.
  - `...` more packages can be provided by creating subdirectories for them.
- `tests` contains all test files.
  - `test_fib` contains the tests for the `fib` package.
  - `...` tests can be provided for other packages by creating subdirectories
    for them.

## Virual Environments

This project runs in a _virtual environment_. A virtual environment is a
project specific Python installation that manages its own Python binaries and
packages. A major advantage that this offers is that each project has its own
environment that it runs in with no global configuration. This means that there
are no conflicts due to global package installation. Suppose one project uses
version `1.0.0` of a package and another project uses version `2.0.0` of
the same package, there are no issues because each project has its own version
of all of the package files.

See the [virtual environment] documentation for information on how this works.

## Using this Project

### Step 1: Install required programs

1.  Install Python 3
2.  Install `virtualenv` and `tox`

    ```sh
    pip3 install virtualenv tox
    ```

### Step 2: Create a new project

1.  Copy this project somewhere and rename it to whatever your project will be
    called.
2.  In a terminal, run

    ```sh
    virtualenv .env
    ```

    to set up a new virtual environment.

    **Note**: This will create a virtual environment using the Python version
    that `virtualenv` was run with (which will be the version it was installed
    with). To use a specific Python version, use

    ```sh
    virtualenv --python=<path_to_other_python_version> .env
    # For example, this might look like
    virtualenv --python=/usr/bin/python3.5 .env
    ```

    instead.
3.  Assuming you are using the `bash` shell, run

    ```sh
    source .env/bin/activate
    ```

    For other shells, see the other `activate.*` scripts in the `.env/bin/`
    directory. If you are on Windows, use PowerShell and run

    ```sh
    .env\Scripts\activate.bat
    ```

You are now in a virtual environment. The `activate` script sets up some
environment variables and functions to point to a project local Python
configuration. This means that instead of using the the global `python` and
`pip` configuration, you are in the configuration contained in the `.env`
directory.

**Note**: The rest of this document assumes that the virtual environment is
active, unless otherwise noted.

You can see that you are in the virtual environment by running

```sh
# macOS/Linux
which python
# Windows
where python
```

and it will show `<path_to_project>/.env/bin/python` instead of the globally
installed Python, which will be something like `/usr/bin/python`. These paths
will be different on Windows.

If you ever want to leave the virtual environment, simply run `deactivate` in
the terminal.

**Note**: You need to activate the virtual environment every time you want to
work on the project in a new terminal.

4.  Now you can install all of the required packages using

    ```sh
    pip install -r requirements.txt
    ```

You can see that these packages are installed in
`.env/lib/python3.7/site-packages`.

**Optional**

5.  Set this up as a git repository by running `git init`.

### Step 3: Run tests

Testing is handled by [tox], which is a virtual environment wrapper that does
not require much configuration. You will likely not need to change the
`tox.ini` file. Simply run

```sh
tox
```

and the testing environment will automatically be created, tests will be
discovered and run, and a report will be printed.

**Note**: The `envlist` in `tox.ini` requires that the appropriately versioned
Python binaries be installed somewhere in the `PATH`.

### Step 4: Running a binary

In the sample Fibonacci project, the `fib` package provides both a library and
a binary. To use the binary, run

```sh
python3 src/fib
```

Note that this path is a directory. This is fine because the `__main__.py` file
in the package is executed using this path. The program will complain because
no arguments were given. Instead, run

```sh
python3 src/fib -s 10
```

### Step 5: Committing Changes and Sharing

When a change is made and is ready to be committed to git, take the following
steps:

1.  If dependencies were installed or upgraded, run
    ```sh
    pip freeze > requirements.txt
    ```
    to save the updated dependencies.
2.  Commit the changes as usual.

To share this code without using `pip` or a service like [GitHub]:

1.  Make sure that all of the changes are committed.
2.  Run
    ```sh
    git clean -fdxn
    ```
    to do a dry run of all of the files that will be removed. Nothing on the
    disk will be changed.
3.  Run
    ```sh
    git clean -fdx
    ```
    to remove all of the ignored files after checking over the dry run list.
4.  Share repository.
    - **Note**: it might be smart to remove the `.git` directory before
      sharing.

## Using a Virtual Environment in IDEs

- [PyCharm]
  - Refer to the [PyCharm creating a virtual environment] documentation
- [Spyder]
  - Go to `Tools > Preferences > Python Interpreter` and select the
      interpreter that the virtual envirinment installs (ie.
      `<path_to_project>/.env/bin/python`)
- [VS Code]
  - Refer to the [using Python environments in VS Code] documentation


[GitHub]: https://github.com/
[PyCharm]: https://www.jetbrains.com/pycharm/
[PyCharm creating a virtual environment]: https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html
[Spyder]: https://www.spyder-ide.org/
[tox]: https://github.com/tox-dev/tox
[Using Python environments in VS Code]: https://code.visualstudio.com/docs/python/environments
[virtual environment]: https://docs.python.org/3/tutorial/venv.html
[VS Code]: https://code.visualstudio.com/

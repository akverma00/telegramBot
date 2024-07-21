# Prerequisites

Before you can run the `main.py` file, make sure you have completed the following steps:

1. Install Python: Make sure you have Python installed on your system. You can download the latest version of Python from the official Python website.

2. Install pip: Pip is a package manager for Python. It is usually installed by default when you install Python. To check if pip is installed, open a terminal or command prompt and run the following command:

    ```
    pip --version
    ```

    If pip is not installed, you can install it by following the instructions on the official pip website.

3. Install dependencies: The `requirements.txt` file contains a list of Python packages that your project depends on. To install these dependencies, navigate to the project directory in your terminal or command prompt and run the following command:

    ```
    pip install -r requirements.txt
    ```

    This will install all the required packages specified in the `requirements.txt` file.

4. Create a copy of the `.sample-env` file: In order to update the actual values, create a copy of the `.sample-env` file and rename it to `.env`. You can do this by running the following command in your terminal or command prompt:

    ```
    cp .sample-env .env
    ```

    This will create a copy of the file and allow you to update the actual values in the `.env` file.

# Start Server
To start the server, run the following command in your terminal or command prompt:

```
python telegramBot/__init__.py
```

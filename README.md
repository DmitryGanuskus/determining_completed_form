# Definition of the completed form

This repository contains a script to determine whether the form is completed
or not. It serves as a simple example of a FastAPI project

## Usage

To use this script, Python must be installed on your computer.

1. Clone this repository:

```shell
git clone https://github.com/DmitryGanuskus/determining_completed_form.git
```

2. Go to the cloned directory:

```shell
cd determining_completed_form
```

3. Install the necessary dependencies:

```shell
poetry install
```

4. [Download MongoDB](https://www.mongodb.com/try/download/community) <br/>
   How to check if MongoDB is installed in windows
   For checking MongoDB is installed or not you need to follow the below
   instructions step by step:

open command prompt
go to till mongod.exe file in bin folder

```shell
C:\Program Files\MongoDB\Server\5.0\bin>
```

Now start the MongoDB server by using mongo

```shell
C:\Program Files\MongoDB\Server\5.0\bin>mongo
```

<br/>
For checking the MongoDB is installed in Ubuntu or not you have to follow these commands:

Start the MongoDB server

```shell
$ sudo service mongod start
```

With the help of this, you start the MongoDB server in ubuntu if exists.

If this gives you an error then you have to first install MongoDB in your
system.

Check the status of MongoDB server is running or not

```shell
$ sudo service mongod status
```

5. Run the script:

```shell
python shell main.py
```

## Running in a container:
**For the following items, you need to have Docker on your device.**
[You can find out more here.](https://docs.docker.com/engine/install/)

1. Building a project
```shell
docker-compose build
```

2. Launching the project
```shell
docker-compose up
```

## Running tests:

1. If you want to run all files

```shell
pytest
```

2. If you want to run a specific file:

```shell
pytest tests/forms/test_forms.py
```

3. If you want to run a specific test:

```shell
pytest tests/forms/test_forms.py::some_test
```

## Actions on GitHub

This repository uses GitHub actions to automate testing using Ruff.
Whenever a push request or pull request event occurs, the Ruff GitHub action
will be
executed and run the Ruff tests.

The Ruff action on GitHub is defined in the file `.github/workflows/ruff.yml`.

## Deposits

Contributions are welcome! If you find any problems or want to add improvements
to this project, feel free to open an extraction request.

## License

This project is licensed under the [MIT License] (LICENSE).
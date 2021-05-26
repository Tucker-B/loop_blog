# ループブログ | Loop Blog
### 概要 | Overview
***

このウェブアップは簡単なCRUDブログように設計されている。

This web app is designed to be a basic CRUD blog. 

Caution: It is in Japanese, so you may want to change various parts to suite your own language/needs.


### 必要なこと | Requirements
***

The only requirement at the moment is for python 3.X.X & Django >= 1.10 to be installed. You can check this by running the following commands in terminal:

`python -V`


`python3 -V`


`django-admin --version`


### 使い方 | Instructions
***

> // Inside the terminal, the `python3` command may be substituted with `python` if your python command points to >= python 3.X.X

1. In order to clone and use this project, you have to make a '.env' file in your root directory and supply your own 'SECRET_KEY' in it.

* The basic syntax for doing so is as follows:

`SECRET_KEY=[KEY]`

> // Without the []

* If you need to generate your own key, you can do so by running the command below in terminal: 


`python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`

> // Credit to Humberto Rocha


2. Open root directory in terminal and create a virtual environment:

`python3 -m venv venv/`

3. Start the virtual environment:

`source venv/bin/activate`

4. Install project dependencies:

`pip3 install -r requirements.txt`

5. Finally, run the web server:

`python3 manage.py runserver`



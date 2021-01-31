### Goal this project:
To demonstrate how start a project in python with pipenv (which is like a package.json em javascript) and venv (virtual env)
#

### Principals referencies:
#### A) Pipenv
- https://packaging.python.org/tutorials/managing-dependencies/
- https://towardsdatascience.com/python-environment-101-1d68bda3094d
- https://python-guide-pt-br.readthedocs.io/pt_BR/latest/dev/virtualenvs.html
#### B) Venv (virtual env)
- https://docs.python.org/pt-br/3/library/venv.html
#

### Installing venv and pipenv
#### A) Linux
1- Install `sudo apt-get install python3-venv` case don't exists python3-venv installed\
2- Execute `pip install pipenv`
#### B) Windows
1- It's don't necessary install venv because when download python already with this dependencies\
2- Execute `pip install pipenv`
#

### Start Project without git clone:
1- Execute `python3.8 -m venv ./venv`. The argument ./venv is the folder where save python env. Note when execution finish there will be a folder venv\
2- To active virtual env, execute `source venv/bin/activate`. If will was in Linux so `source venv/bin/Activate.ps1`\
3- Install dependencies python with pipenv. As example we install pandas: `pipenv install pandas`\
4- After install dependencies execute `pipenv shell` to active virtual env with dependencies installed\
5- Create a folder src and start with coding
#

### Start Project with git clone:
1- Execute `git clone https://github.com/ElderVivot/project-python-with-pipenv-venv.git`\
2- Create virtual env with `python3.8 -m venv ./venv`\
3- To active virtual env, execute `source venv/bin/activate`. If will was in Linux so `source venv/bin/Activate.ps1`\
4- Install dependencies that are file Pipfile.lock, execute `pipenv sync`\
5- After install, then execute `python src/main.py`

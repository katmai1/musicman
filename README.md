# Music Manager

PyQt5 App to clean and organize music colection.


## Features

- Internationalization.
- Basic Context class.
- Docopt to manage arguments.
- Versionner integrated.
- DevScript to prepare ui files, icons and i18n.



---


## Prepare develop environment with anaconda

Create and active environment.

`conda create -n env_name python=3.7`

`conda activate env_name`

Install PyQt5

`conda install -c anaconda pyqt`


---


## Creating new project

- Create new repository using github button named 'Use this template'.
- Install requeriments:

    `pip install -r requirements.txt`

- Initialize versionner:

    `ver init`

- Modify mainwindow.ui file with QtDesigner
- Run devtool script:

    `./devtool-update_project.sh`

- Run application:

    `python run.py`

---

## Mandatory folders and files

- .ui: ui files generated with qt designer
- .icons/icons.qrc: resource file with all icons, generated with qt designer
- .app: your code
- ./devtool-update_project.sh - script to prepare our project:
    - Convert ui files to python code and copy into 'app/ui'
    - generate translation files and copy into 'app/i18n' (prepared to use with linguist)
    - convert icons.qrc file to python code

---

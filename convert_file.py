from setuptools import setup

APP = ['Discord_Python.py'] #Name of filename to convert

OPTIONS = {
    'argv_emulation' : True,}

setup(

    app = APP,
    options={'py2app' : OPTIONS},
    setup_requires=['py2app']
    )

#this script needs to be run on a macbook


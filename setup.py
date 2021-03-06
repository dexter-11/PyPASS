"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup
from glob import glob

APP_NAME = "PyPASS"
APP = ['pypass.py']
DATA_FILES = [('libs', glob('libs/*.py')),'app.icns']
OPTIONS = {
	'iconfile':'app.icns',
	'argv_emulation': True,
	 'plist': {
	        'CFBundleName': APP_NAME,
	        'CFBundleDisplayName': APP_NAME,
	        'CFBundleGetInfoString': "PyPASS Password Manager",
	        'CFBundleVersion': "1.0.0",
	        'CFBundleShortVersionString': "1.0.0", 
	        'NSHumanReadableCopyright': u"Copyright © PyPASS 2021 - Minor Project (KIIT University)"
	    },	
    'compressed': True,
	'packages': ['numpy','pandas','pyAesCrypt','cryptography','PyQt5-sip','PyQt5']
}

setup(
	name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
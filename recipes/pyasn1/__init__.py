
from pythonforandroid.toolchain import PythonRecipe


class PyASN1Recipe(PythonRecipe):
    version = '0.4.2'
    url = 'https://pypi.python.org/packages/source/p/pyasn1/pyasn1-{version}.tar.gz'
    depends = [('python2', 'python3crystax')]


recipe = PyASN1Recipe()

python3 setup.py build
python3 setup.py sdist
twine upload .\dist\tsjPython-${1}.tar.gz
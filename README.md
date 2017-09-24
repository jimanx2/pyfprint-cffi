pyfprint-cffi
=============

tl;dr
-----
This is a python module with [CFFI](https://cffi.readthedocs.org/en/latest/) bindings for [libfprint](http://www.freedesktop.org/wiki/Software/fprint/libfprint/)

**warning:** i've cut off some things from the [original](https://github.com/xantares/pyfprint) [SWIG](https://github.com/swig/swig) bindings

Compiling
---------
```
	1. You need MSYS2 with gcc, g++ toolchains
	2. You also need Python 2.7 for Windows
	3. python setup.py install
```

Usage
-----
```
	1. add <python site-packages dir>/pyfprint/ to PATH
	2. run python and import pyfprint
	3. example invocation:
		
		REM start.bat
		SET PATH=%PATH%;<python site-packages dir>/pyfprint
		python -c "import pyfprint"

		REM if this script doesn't yield an error, you should be
		REM good to go
```

P/S: Please open an issue if this does not work for you. 

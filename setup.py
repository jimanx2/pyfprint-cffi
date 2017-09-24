#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CFFI bindings for libfprint"""

import os
from distutils.core import setup, Extension

setup(
    name="pyfprint-cffi",
    version="0.1",
    description="CFFI bindings for libfprint",
    author="Francisco Demartino",
    author_email="demartino.francisco@gmail.com",
    url="https://github.com/franciscod/pyfprint-cffi",
    license="GPL-2",
    packages=["pyfprint"],
    package_data={
        "pyfprint": [
            "msys-fprint-0.dll",
            "libgcc_s_dw2-1.dll",
            "libglib-2.0-0.dll",
            "libiconv-2.dll",
            "libintl-8.dll",
            "libnspr4.dll",
            "libpcre-1.dll",
            "libpixman-1-0.dll",
            "libplc4.dll",
            "libplds4.dll",
            "libusb-1.0.dll",
            "libwinpthread-1.dll",
            "nss3.dll",
            "nssutil3.dll"
        ]
    },
    install_requires=[
        "cffi==1.11.0",
        "Pillow",
    ],
)

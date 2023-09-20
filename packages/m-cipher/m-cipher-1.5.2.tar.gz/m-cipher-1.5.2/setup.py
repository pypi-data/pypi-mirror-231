#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Author: ChungNT
    Company: MobioVN
    Date created: 05/06/2020
"""
import os

from distutils.core import setup, Extension

SOURCE_PATH = 'mobio'


def package_files(directory, ext=None):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            if filename.endswith(ext):
                paths.append(os.path.join(path, filename))
    return paths


extra_files = package_files('mobio', '.c')

cryp2_module = Extension('mobio.libs.ciphers.mobio_crypt_2', sources=['mobio/libs/ciphers/mobio_crypt_2.c'])
cryp3_module = Extension('mobio.libs.ciphers.mobio_crypt_3', sources=['mobio/libs/ciphers/mobio_crypt_3.c'])
cryp4_module = Extension('mobio.libs.ciphers.mobio_crypt_4', sources=['mobio/libs/ciphers/mobio_crypt_4.c'])

version_dev='1.5.5'
version_prod='1.5.2'

run_mode=''

setup(
    name='m-cipher' + run_mode,
    version='1.5.2',
    author='Mobio Company',
    author_email='dev@mobio.io',
    packages=['mobio/libs/ciphers'],
    zip_safe=False,
    ext_modules=[cryp2_module, cryp3_module, cryp4_module],
    python_requires='>=3.11'
)

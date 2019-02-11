# Copyright (C) 2014 Chrysostomos Nanakos <chris@include.gr>
#
# This file is part of kmodpy.
#
# kmodpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with kmodpy.  If not, see <http://www.gnu.org/licenses/>.


import os
import sys
if sys.version_info < (2, 6):
    from distutils.command import register

    def isstr(k, v):
        return isinstance(v, basestring)

    def patch(func):
        def post_to_server(self, data, auth=None):
            for key, value in filter(isstr, data.items()):
                data[key] = value.decode('utf8')
            return func(self, data, auth)
        return post_to_server

    register.register.post_to_server = patch(register.register.post_to_server)

from setuptools import setup

package_name = "kmodpy"

sys.path.insert(0, package_name)
from version import __version__

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(name="kmodpy",
      version=__version__,
      author='Chrysostomos Nanakos',
      author_email='chris@include.gr',
      description='Python binding for kmod',
      long_description=read('README'),
      license='GPL',
      keywords='kmod libkmod kmodpy',
      platforms=['posix'],
      packages=[package_name],
      provides=[package_name],
      classifiers=[
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
        ],
     )


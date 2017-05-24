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


from ctypes import *
from ctypes.util import find_library
from ._libkmod_h import *

libkmod = find_library("kmod")
if libkmod is None:
    raise OSError("Could not load libkmod dynamic library")

kmod = cdll.LoadLibrary(libkmod)

kmod_new = kmod.kmod_new
kmod_new.argtypes = [c_char_p, c_char_p]
kmod_new.restype = POINTER(kmod_ctx)

kmod_load_resources = kmod.kmod_load_resources
kmod_load_resources.argtypes = [POINTER(kmod_ctx)]
kmod_load_resources.restype = c_int

kmod_module_new_from_loaded = kmod.kmod_module_new_from_loaded
kmod_module_new_from_loaded.argtypes = [POINTER(kmod_ctx), POINTER(POINTER(kmod_list))]
kmod_module_new_from_loaded.restype = c_int

kmod_module_get_module = kmod.kmod_module_get_module
kmod_module_get_module.argtypes = [POINTER(kmod_list)]
kmod_module_get_module.restype = POINTER(kmod_module)

kmod_module_get_name = kmod.kmod_module_get_name
kmod_module_get_name.argtypes = [POINTER(kmod_module)]
kmod_module_get_name.restype = c_char_p

kmod_module_unref = kmod.kmod_module_unref
kmod_module_unref.argtypes = [POINTER(kmod_module)]

kmod_module_get_refcnt = kmod.kmod_module_get_refcnt
kmod_module_get_refcnt.argtypes = [POINTER(kmod_module)]
kmod_module_get_refcnt.restype = c_int

kmod_module_get_size = kmod.kmod_module_get_size
kmod_module_get_size.argtypes = [POINTER(kmod_module)]
kmod_module_get_size.restype = c_long

kmod_module_new_from_lookup = kmod.kmod_module_new_from_lookup
kmod_module_new_from_lookup.argtypes = [POINTER(kmod_ctx), c_char_p,
                                        POINTER(POINTER(kmod_list))]
kmod_module_new_from_lookup.restype = c_int

kmod_module_insert_module = kmod.kmod_module_insert_module
kmod_module_insert_module.argtypes = [POINTER(kmod_module), c_uint32, c_char_p]
kmod_module_insert_module.restype = c_int

kmod_module_remove_module = kmod.kmod_module_remove_module
kmod_module_remove_module.argtypes = [POINTER(kmod_module), c_uint32]
kmod_module_remove_module.restype = c_int

kmod_module_get_info = kmod.kmod_module_get_info
kmod_module_get_info.argtypes = [POINTER(kmod_module),
                                 POINTER(POINTER(kmod_list))]
kmod_module_get_info.restype = c_int

kmod_module_info_get_key = kmod.kmod_module_info_get_key
kmod_module_info_get_key.argtypes = [POINTER(kmod_list)]
kmod_module_info_get_key.restype = c_char_p

kmod_module_info_get_value = kmod.kmod_module_info_get_value
kmod_module_info_get_value.argtypes = [POINTER(kmod_list)]
kmod_module_info_get_value.restype = c_char_p

kmod_module_info_free_list = kmod.kmod_module_info_free_list
kmod_module_info_free_list.argtypes = [POINTER(kmod_list)]

kmod_module_get_dependencies = kmod.kmod_module_get_dependencies
kmod_module_get_dependencies.argtypes = [POINTER(kmod_module)]
kmod_module_get_dependencies.restype = POINTER(kmod_list)

__all__ = ['kmod_new', 'kmod_load_resources', 'kmod_module_new_from_loaded',
           'kmod_module_get_module', 'kmod_module_get_name',
           'kmod_module_unref', 'kmod_module_get_refcnt',
           'kmod_module_get_size', 'kmod_module_new_from_lookup',
           'kmod_module_insert_module', 'kmod_module_remove_module',
           'kmod_ctx', 'kmod_list', 'kmod_module_get_info',
           'kmod_module_info_get_key', 'kmod_module_info_get_value',
           'kmod_module_info_free_list', 'kmod_module_get_dependencies']

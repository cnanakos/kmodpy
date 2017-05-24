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


from ctypes import (
    POINTER,
    byref,
    addressof
)
from ._libkmod import *
from .error import KmodError
import errno


class Kmod(object):
    "Kmod Class -- Python interface to kmod API"
    def __init__(self, mod_dir=None):
        self._kmod_ctx = kmod_new(mod_dir, None)
        if self._kmod_ctx:
            kmod_load_resources(self._kmod_ctx)

    def __offsetof(self, typ, membname):
        return getattr(typ, membname).offset

    def __container_of(self, membaddr, typ, membname):
        return typ.from_address(addressof(membaddr) -
                                self.__offsetof(typ, membname))

    def loaded(self):
        """
        Generate currently loaded modules, use_count and sizes
        """
        klist = POINTER(kmod_list)()
        err = kmod_module_new_from_loaded(self._kmod_ctx, byref(klist))
        if err:
            raise KmodError('Could not get loaded modules')
        itr = klist.contents.node.next
        while True:
            itrnode = self.__container_of(itr.contents, kmod_list, "node")
            mod = kmod_module_get_module(itrnode)
            name = kmod_module_get_name(mod)
            use_count = kmod_module_get_refcnt(mod)
            size = kmod_module_get_size(mod)
            kmod_module_unref(mod)
            yield (name, use_count, size)
            if addressof(klist.contents) == addressof(itr.contents):
                break
            itr = itr.contents.next

    def list(self):
        """
        Generate currently loaded modules
        """
        for mod in self.loaded():
            yield (mod[0], mod[2])

    def lookup(self, alias_name):
        """
        Generate modules matching 'alias_name'
        """
        if hasattr(alias_name, 'encode'):
            alias_name = alias_name.encode('ascii')
        mlist = POINTER(kmod_list)()
        err = kmod_module_new_from_lookup(self._kmod_ctx, alias_name,
                                          byref(mlist))
        if err < 0:
            raise KmodError('Could not modprobe')
        if not mlist:
            return
        itr = mlist.contents.node.next
        while True:
            itrnode = self.__container_of(itr.contents, kmod_list, "node")
            mod = kmod_module_get_module(itrnode)
            yield mod
            if addressof(mlist.contents) == addressof(itr.contents):
                break
            itr = itr.contents.next

    def modinfo(self, name):
        """
        Generate modules parameters and info
        """
        mods = list(self.lookup(name))
        if not mods:
            raise KmodError("Could not modinfo '%s'" % name)
        ilist = POINTER(kmod_list)()
        err = kmod_module_get_info(mods[0], byref(ilist))
        if err < 0:
            raise KmodError("Could not modinfo '%s'" % name)
        if not ilist:
            return
        itr = ilist.contents.node.next
        while True:
            itrnode = self.__container_of(itr.contents, kmod_list, "node")
            key = kmod_module_info_get_key(itrnode)
            value = kmod_module_info_get_value(itrnode)
            yield (key, value)
            if addressof(ilist.contents) == addressof(itr.contents):
                kmod_module_info_free_list(ilist)
                break
            itr = itr.contents.next

    def show_depends(self, name):
        """
        Generate module dependencies
        """
        mods = list(self.lookup(name))
        if not mods:
            raise KmodError("Could not modprobe '%s'" % name)
        flist = kmod_module_get_dependencies(mods[0])
        if not flist:
            return
        itr = flist.contents.node.next
        while True:
            itrnode = self.__container_of(itr.contents, kmod_list, "node")
            m = kmod_module_get_module(itrnode)
            name = kmod_module_get_name(m)
            yield name
            if addressof(flist.contents) == addressof(itr.contents):
                break
            itr = itr.contents.next

    def __insert(self, mod, flags=0, extra_options=None):
        err = kmod_module_insert_module(mod, flags, extra_options)
        if err == -errno.EEXIST:
            raise KmodError('Module already loaded')
        elif err < 0:
            raise KmodError('Could not load module')

    def __remove(self, mod, flags=0):
        err = kmod_module_remove_module(mod, flags)
        if err < 0:
            raise KmodError('Could not remove module')

    def modprobe(self, name, quiet=False, *args, **kwargs):
        """
        Load a module and all dependent modules.
        The 'quiet' options defaults to False; set True to mimic the behavior
        of the '--quiet' commandline options.
        """
        mods = list(self.lookup(name))
        if not mods and not quiet:
            raise KmodError("Could not modprobe '%s'" % name)

        for mod in mods:
            self.__insert(mod, *args, **kwargs)

    def rmmod(self, name, *args, **kwargs):
        "Remove module from current tree"
        mods = list(self.lookup(name))
        if not mods:
            raise KmodError("Could not rmmod '%s'" % name)
        for mod in mods:
            self.__remove(mod, *args, **kwargs)

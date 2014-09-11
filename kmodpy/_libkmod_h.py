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

STRING = c_char_p


P_PGID = 2
P_PID = 1
P_ALL = 0


class hash_entry(Structure):
    pass
hash_entry._fields_ = [
    ('key', STRING),
    ('value', c_void_p),
]


class hash_bucket(Structure):
    pass
hash_bucket._fields_ = [
    ('entries', POINTER(hash_entry)),
    ('used', c_uint),
    ('total', c_uint),
]


class hash(Structure):
    pass
hash._fields_ = [
    ('count', c_uint),
    ('step', c_uint),
    ('n_buckets', c_uint),
    ('free_value', CFUNCTYPE(None, c_void_p)),
    ('buckets', hash_bucket),
]


class kmod_ctx(Structure):
    pass


class __va_list_tag(Structure):
    pass


class kmod_config(Structure):
    pass


class index_mm(Structure):
    pass
kmod_ctx._fields_ = [
    ('refcount', c_int),
    ('log_priority', c_int),
    ('log_fn', CFUNCTYPE(None, c_void_p, c_int, STRING, c_int, STRING, STRING,
                         POINTER(__va_list_tag))),
    ('log_data', c_void_p),
    ('userdata', c_void_p),
    ('dirname', STRING),
    ('config', POINTER(kmod_config)),
    ('modules_by_name', POINTER(hash)),
    ('indexes', POINTER(index_mm) * 4),
    ('indexes_stamp', c_ulonglong * 4),
]
uint32_t = c_uint32
size_t = c_ulong
index_mm._fields_ = [
    ('ctx', POINTER(kmod_ctx)),
    ('mm', c_void_p),
    ('root_offset', uint32_t),
    ('size', size_t),
]
class list_node(Structure):
    pass
list_node._fields_ = [
    ('next', POINTER(list_node)),
    ('prev', POINTER(list_node)),
]
class kmod_list(Structure):
    pass
kmod_list._fields_ = [
    ('node', list_node),
    ('data', c_void_p),
]
kmod_config._fields_ = [
    ('ctx', POINTER(kmod_ctx)),
    ('aliases', POINTER(kmod_list)),
    ('blacklists', POINTER(kmod_list)),
    ('options', POINTER(kmod_list)),
    ('remove_commands', POINTER(kmod_list)),
    ('install_commands', POINTER(kmod_list)),
    ('softdeps', POINTER(kmod_list)),
    ('paths', POINTER(kmod_list)),
]
class kmod_module(Structure):
    pass
class N11kmod_module4DOT_20E(Structure):
    pass
N11kmod_module4DOT_20E._fields_ = [
    ('dep', c_bool, 1),
    ('options', c_bool, 1),
    ('install_commands', c_bool, 1),
    ('remove_commands', c_bool, 1),
]
kmod_module._fields_ = [
    ('ctx', POINTER(kmod_ctx)),
    ('hashkey', STRING),
    ('name', STRING),
    ('path', STRING),
    ('dep', POINTER(kmod_list)),
    ('options', STRING),
    ('install_commands', STRING),
    ('remove_commands', STRING),
    ('alias', STRING),
    ('n_dep', c_int),
    ('refcount', c_int),
    ('init', N11kmod_module4DOT_20E),
    ('visited', c_bool, 1),
    ('ignorecmd', c_bool, 1),
    ('builtin', c_bool, 1),
]
class imaxdiv_t(Structure):
    pass
imaxdiv_t._fields_ = [
    ('quot', c_long),
    ('rem', c_long),
]
int8_t = c_int8
int16_t = c_int16
int32_t = c_int32
int64_t = c_int64
uint8_t = c_uint8
uint16_t = c_uint16
uint64_t = c_uint64
int_least8_t = c_byte
int_least16_t = c_short
int_least32_t = c_int
int_least64_t = c_long
uint_least8_t = c_ubyte
uint_least16_t = c_ushort
uint_least32_t = c_uint
uint_least64_t = c_ulong
int_fast8_t = c_byte
int_fast16_t = c_long
int_fast32_t = c_long
int_fast64_t = c_long
uint_fast8_t = c_ubyte
uint_fast16_t = c_ulong
uint_fast32_t = c_ulong
uint_fast64_t = c_ulong
intptr_t = c_long
uintptr_t = c_ulong
intmax_t = c_long
uintmax_t = c_ulong
class div_t(Structure):
    pass
div_t._fields_ = [
    ('quot', c_int),
    ('rem', c_int),
]
class ldiv_t(Structure):
    pass
ldiv_t._fields_ = [
    ('quot', c_long),
    ('rem', c_long),
]
class lldiv_t(Structure):
    pass
lldiv_t._fields_ = [
    ('quot', c_longlong),
    ('rem', c_longlong),
]
class random_data(Structure):
    pass
random_data._fields_ = [
    ('fptr', POINTER(int32_t)),
    ('rptr', POINTER(int32_t)),
    ('state', POINTER(int32_t)),
    ('rand_type', c_int),
    ('rand_deg', c_int),
    ('rand_sep', c_int),
    ('end_ptr', POINTER(int32_t)),
]
class drand48_data(Structure):
    pass
drand48_data._fields_ = [
    ('__x', c_ushort * 3),
    ('__old_x', c_ushort * 3),
    ('__c', c_ushort),
    ('__init', c_ushort),
    ('__a', c_ulonglong),
]
__compar_fn_t = CFUNCTYPE(c_int, c_void_p, c_void_p)
comparison_fn_t = __compar_fn_t
__compar_d_fn_t = CFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p)
__clock_t = c_long
clock_t = __clock_t
__time_t = c_long
time_t = __time_t
__clockid_t = c_int
clockid_t = __clockid_t
__timer_t = c_void_p
timer_t = __timer_t
class timespec(Structure):
    pass
__syscall_slong_t = c_long
timespec._fields_ = [
    ('tv_sec', __time_t),
    ('tv_nsec', __syscall_slong_t),
]
pthread_t = c_ulong
class pthread_attr_t(Union):
    pass
pthread_attr_t._fields_ = [
    ('__size', c_char * 56),
    ('__align', c_long),
]
class __pthread_internal_list(Structure):
    pass
__pthread_internal_list._fields_ = [
    ('__prev', POINTER(__pthread_internal_list)),
    ('__next', POINTER(__pthread_internal_list)),
]
__pthread_list_t = __pthread_internal_list
class __pthread_mutex_s(Structure):
    pass
__pthread_mutex_s._fields_ = [
    ('__lock', c_int),
    ('__count', c_uint),
    ('__owner', c_int),
    ('__nusers', c_uint),
    ('__kind', c_int),
    ('__spins', c_short),
    ('__elision', c_short),
    ('__list', __pthread_list_t),
]
class pthread_mutex_t(Union):
    pass
pthread_mutex_t._fields_ = [
    ('__data', __pthread_mutex_s),
    ('__size', c_char * 40),
    ('__align', c_long),
]
class pthread_mutexattr_t(Union):
    pass
pthread_mutexattr_t._fields_ = [
    ('__size', c_char * 4),
    ('__align', c_int),
]
class N14pthread_cond_t4DOT_13E(Structure):
    pass
N14pthread_cond_t4DOT_13E._fields_ = [
    ('__lock', c_int),
    ('__futex', c_uint),
    ('__total_seq', c_ulonglong),
    ('__wakeup_seq', c_ulonglong),
    ('__woken_seq', c_ulonglong),
    ('__mutex', c_void_p),
    ('__nwaiters', c_uint),
    ('__broadcast_seq', c_uint),
]
class pthread_cond_t(Union):
    pass
pthread_cond_t._fields_ = [
    ('__data', N14pthread_cond_t4DOT_13E),
    ('__size', c_char * 48),
    ('__align', c_longlong),
]
class pthread_condattr_t(Union):
    pass
pthread_condattr_t._fields_ = [
    ('__size', c_char * 4),
    ('__align', c_int),
]
pthread_key_t = c_uint
pthread_once_t = c_int
class N16pthread_rwlock_t4DOT_16E(Structure):
    pass
N16pthread_rwlock_t4DOT_16E._fields_ = [
    ('__lock', c_int),
    ('__nr_readers', c_uint),
    ('__readers_wakeup', c_uint),
    ('__writer_wakeup', c_uint),
    ('__nr_readers_queued', c_uint),
    ('__nr_writers_queued', c_uint),
    ('__writer', c_int),
    ('__shared', c_int),
    ('__pad1', c_ulong),
    ('__pad2', c_ulong),
    ('__flags', c_uint),
]
class pthread_rwlock_t(Union):
    pass
pthread_rwlock_t._fields_ = [
    ('__data', N16pthread_rwlock_t4DOT_16E),
    ('__size', c_char * 56),
    ('__align', c_long),
]
class pthread_rwlockattr_t(Union):
    pass
pthread_rwlockattr_t._fields_ = [
    ('__size', c_char * 8),
    ('__align', c_long),
]
pthread_spinlock_t = c_int
class pthread_barrier_t(Union):
    pass
pthread_barrier_t._fields_ = [
    ('__size', c_char * 32),
    ('__align', c_long),
]
class pthread_barrierattr_t(Union):
    pass
pthread_barrierattr_t._fields_ = [
    ('__size', c_char * 4),
    ('__align', c_int),
]
__sig_atomic_t = c_int
class __sigset_t(Structure):
    pass
__sigset_t._fields_ = [
    ('__val', c_ulong * 16),
]
class timeval(Structure):
    pass
__suseconds_t = c_long
timeval._fields_ = [
    ('tv_sec', __time_t),
    ('tv_usec', __suseconds_t),
]
__u_char = c_ubyte
__u_short = c_ushort
__u_int = c_uint
__u_long = c_ulong
__int8_t = c_byte
__uint8_t = c_ubyte
__int16_t = c_short
__uint16_t = c_ushort
__int32_t = c_int
__uint32_t = c_uint
__int64_t = c_long
__uint64_t = c_ulong
__quad_t = c_long
__u_quad_t = c_ulong
__dev_t = c_ulong
__uid_t = c_uint
__gid_t = c_uint
__ino_t = c_ulong
__ino64_t = c_ulong
__mode_t = c_uint
__nlink_t = c_ulong
__off_t = c_long
__off64_t = c_long
__pid_t = c_int
class __fsid_t(Structure):
    pass
__fsid_t._fields_ = [
    ('__val', c_int * 2),
]
__rlim_t = c_ulong
__rlim64_t = c_ulong
__id_t = c_uint
__useconds_t = c_uint
__daddr_t = c_int
__key_t = c_int
__blksize_t = c_long
__blkcnt_t = c_long
__blkcnt64_t = c_long
__fsblkcnt_t = c_ulong
__fsblkcnt64_t = c_ulong
__fsfilcnt_t = c_ulong
__fsfilcnt64_t = c_ulong
__fsword_t = c_long
__ssize_t = c_long
__syscall_ulong_t = c_ulong
__loff_t = __off64_t
__qaddr_t = POINTER(__quad_t)
__caddr_t = STRING
__intptr_t = c_long
__socklen_t = c_uint

# values for enumeration 'idtype_t'
idtype_t = c_int  # enum
class wait(Union):
    pass
class N4wait3DOT_3E(Structure):
    pass
N4wait3DOT_3E._fields_ = [
    ('__w_termsig', c_uint, 7),
    ('__w_coredump', c_uint, 1),
    ('__w_retcode', c_uint, 8),
    ('', c_uint, 16),
]
class N4wait3DOT_4E(Structure):
    pass
N4wait3DOT_4E._fields_ = [
    ('__w_stopval', c_uint, 8),
    ('__w_stopsig', c_uint, 8),
    ('', c_uint, 16),
]
wait._fields_ = [
    ('w_status', c_int),
    ('__wait_terminated', N4wait3DOT_3E),
    ('__wait_stopped', N4wait3DOT_4E),
]
sigset_t = __sigset_t
__fd_mask = c_long
class fd_set(Structure):
    pass
fd_set._fields_ = [
    ('fds_bits', __fd_mask * 16),
]
fd_mask = __fd_mask
u_char = __u_char
u_short = __u_short
u_int = __u_int
u_long = __u_long
quad_t = __quad_t
u_quad_t = __u_quad_t
fsid_t = __fsid_t
loff_t = __loff_t
ino_t = __ino_t
ino64_t = __ino64_t
dev_t = __dev_t
gid_t = __gid_t
mode_t = __mode_t
nlink_t = __nlink_t
uid_t = __uid_t
off_t = __off_t
off64_t = __off64_t
pid_t = __pid_t
id_t = __id_t
ssize_t = __ssize_t
daddr_t = __daddr_t
caddr_t = __caddr_t
key_t = __key_t
useconds_t = __useconds_t
suseconds_t = __suseconds_t
ulong = c_ulong
ushort = c_ushort
uint = c_uint
u_int8_t = c_ubyte
u_int16_t = c_ushort
u_int32_t = c_uint
u_int64_t = c_ulong
register_t = c_long
blksize_t = __blksize_t
blkcnt_t = __blkcnt_t
fsblkcnt_t = __fsblkcnt_t
fsfilcnt_t = __fsfilcnt_t
blkcnt64_t = __blkcnt64_t
fsblkcnt64_t = __fsblkcnt64_t
fsfilcnt64_t = __fsfilcnt64_t
class __locale_struct(Structure):
    pass
class __locale_data(Structure):
    pass
__locale_struct._fields_ = [
    ('__locales', POINTER(__locale_data) * 13),
    ('__ctype_b', POINTER(c_ushort)),
    ('__ctype_tolower', POINTER(c_int)),
    ('__ctype_toupper', POINTER(c_int)),
    ('__names', STRING * 13),
]
__locale_data._fields_ = [
]
__locale_t = POINTER(__locale_struct)
locale_t = __locale_t
__va_list_tag._fields_ = [
]
__gnuc_va_list = __va_list_tag * 1
va_list = __gnuc_va_list
__all__ = ['__uint16_t', '__pthread_mutex_s', '__int16_t',
           'pthread_condattr_t', 'int_fast32_t', 'pthread_once_t',
           'fsfilcnt_t', '__timer_t', 'mode_t', 'pthread_mutexattr_t',
           'size_t', 'random_data', '__uint32_t', 'uint8_t', 'P_PGID',
           'blkcnt_t', 'uint_least16_t', '__syscall_slong_t',
           '__ino64_t', 'fsblkcnt64_t', '__qaddr_t', 'N4wait3DOT_3E',
           '__mode_t', 'hash_bucket', '__loff_t', 'intptr_t',
           'off64_t', 'id_t', 'blksize_t', 'daddr_t', 'int_fast8_t',
           '__locale_data', 'u_char', 'uid_t', 'u_int64_t',
           'u_int16_t', '__time_t', 'sigset_t', 'int_least16_t',
           'N11kmod_module4DOT_20E', 'uint_fast16_t', '__int32_t',
           'pthread_rwlock_t', '__nlink_t', '__compar_fn_t',
           '__fsid_t', 'N4wait3DOT_4E', '__uint64_t', 'timespec',
           '__va_list_tag', '__off64_t', '__fsword_t', '__fd_mask',
           'kmod_list', 'intmax_t', 'int16_t', 'clock_t', 'u_int32_t',
           '__id_t', 'int_fast64_t', '__sigset_t', '__clockid_t',
           '__useconds_t', 'uint_fast32_t', 'int_least8_t', 'div_t',
           'hash_entry', 'list_node', 'kmod_ctx', 'ldiv_t',
           'N16pthread_rwlock_t4DOT_16E', 'va_list', 'uint_least8_t',
           'pthread_barrier_t', 'hash', 'fd_mask',
           '__pthread_internal_list', 'kmod_module', '__gnuc_va_list',
           '__intptr_t', 'P_PID', '__u_long', 'wait', 'ushort',
           '__blkcnt_t', '__pthread_list_t', 'clockid_t',
           'pthread_attr_t', 'fd_set', 'caddr_t', 'uint',
           '__rlim64_t', 'uint16_t', 'uint_fast8_t', 'int32_t',
           'uint_least64_t', '__blksize_t', '__syscall_ulong_t',
           'pthread_spinlock_t', '__off_t', 'fsblkcnt_t', '__gid_t',
           'u_quad_t', '__ssize_t', 'register_t', '__compar_d_fn_t',
           'fsfilcnt64_t', '__locale_struct', 'comparison_fn_t',
           '__daddr_t', 'ino64_t', '__sig_atomic_t', 'uint_least32_t',
           'int_least64_t', 'uintptr_t', '__uint8_t', '__u_char',
           '__fsblkcnt64_t', 'int8_t', '__caddr_t', '__blkcnt64_t',
           '__dev_t', 'gid_t', 'pthread_barrierattr_t', 'kmod_config',
           '__suseconds_t', 'pid_t', 'timer_t', 'quad_t', 'u_long',
           '__fsfilcnt64_t', '__socklen_t', 'pthread_key_t',
           'index_mm', 'uint64_t', 'blkcnt64_t', 'u_int8_t', 'loff_t',
           'pthread_cond_t', 'uintmax_t', 'off_t', '__fsblkcnt_t',
           'int64_t', 'int_fast16_t', '__rlim_t', 'locale_t',
           'time_t', 'pthread_t', '__locale_t', 'drand48_data',
           'ino_t', 'imaxdiv_t', 'lldiv_t', '__quad_t', 'timeval',
           '__u_quad_t', '__u_short', 'int_least32_t', 'fsid_t',
           '__pid_t', 'ssize_t', 'ulong', 'u_short', 'key_t',
           '__ino_t', 'u_int', 'useconds_t', 'nlink_t',
           'pthread_rwlockattr_t', 'idtype_t',
           'N14pthread_cond_t4DOT_13E', 'uint_fast64_t',
           '__fsfilcnt_t', '__u_int', 'P_ALL', 'pthread_mutex_t',
           '__int64_t', '__key_t', 'uint32_t', '__clock_t', 'dev_t',
           '__uid_t', '__int8_t', 'suseconds_t']

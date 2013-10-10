import shutil
from setuptools import setup

from rosfreeze import import_ros_core, import_ros_package, get_disutils_cmds

#clean the build dir incase we just built the rosfreeze package itself
#(if you use rosfreeze, you do not need this step)
try:
    shutil.rmtree('build')
except OSError:
    pass

MY_PACKAGE = ''

if MY_PACKAGE:
    srcdir, bindir, datadir = import_ros_package(MY_PACKAGE, data='data')
else:
    srcdir, bindir, datadir = import_ros_core()

setup(name='python-ros-electric' if not MY_PACKAGE else 'python-ros-electric-%s' % MY_PACKAGE,
      version='1.0',
      description='Pure Python Ros (Electric)',
      author='John Stowers',
      author_email='john.stowers@gmail.com',
      url='https://github.com/strawlab/ros-freeze.git',
      **get_disutils_cmds(srcdir, bindir, datadir)
 )


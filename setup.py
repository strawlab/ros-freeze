from setuptools import setup

from build import import_ros_core, import_ros_package, get_disutils_cmds

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
      url='https://github.com/nzjrs/python-ros.git',
      **get_disutils_cmds(srcdir, bindir, datadir)
 )

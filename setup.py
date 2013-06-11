from distutils.core import setup

from build import import_ros_core, import_ros_package, get_disutils_cmds

srcdir, bindir, datadir = import_ros_core(".")
import_ros_package(srcdir, bindir, datadir, "flycave", data='data')

setup(name='python-pyros',
      version='1.0',
      description='Pure Python Ros Core',
      author='John Stowers',
      author_email='john.stowers@gmail.com',
      url='https://github.com/nzjrs/python-ros.git',
      **get_disutils_cmds(srcdir, bindir, datadir)
 )

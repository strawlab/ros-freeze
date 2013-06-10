from distutils.core import setup

from build import import_ros_core, get_disutils_cmds

setup(name='python-pyros',
      version='1.0',
      description='Pure Python Ros Core',
      author='John Stowers',
      author_email='john.stowers@gmail.com',
      url='https://github.com/nzjrs/python-ros.git',
      **get_disutils_cmds(*import_ros_core("./"))
 )

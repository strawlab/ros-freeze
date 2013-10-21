from setuptools import setup

setup(name='python-rosfreeze',
      version='1.1',
      description='Convert ROS packages to python packages',
      author='John Stowers',
      author_email='john.stowers@gmail.com',
      url='https://github.com/strawlab/ros-freeze.git',
      py_modules=['rosfreeze'],
      scripts=['ros-freeze-package'],
 )


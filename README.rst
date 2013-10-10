ROS Freeze
==========

Ros Freeze converts an entire (pure python only) ROS package to
a python source or binary distribution which includes all dependencies and
ROS components required to run.

This tool has been tested on ROS Electric where it has been used to convert
complex python ROS applications with dozens of dependencies to standalone
python packages.

An example is included (setup-freeze.py) that builds a python package containig rospy
and all its dependencies, including the core ros command line tools
(rostopic, rosnode, etc) and std_msgs.

Why are there two setup.py files?
"""""""""""""""""""""""""""""""""

setup.py builds a python package that contains *only* the rosfreeze script.
You may then install this on your system and use it to freeze other ROS packages.

setup-freeze.py contains is an example setup.py file that you may,
from this source directory if you wish, modify and use to freeze your ROS package.

Converting a ROS pacakge to a pure python package
-------------------------------------------------

1. modify the included setup-freeze.py (edit MY_PACKAGE)

2. freeze the ROS package::

   $ source /path/to/your/ros/environment.sh
   $ python setup-freeze.py build

2. build an egg::

   $ python setup.py bdist_egg

Running the pure python ROS
---------------------------

1. install the frozen ROS package generated egg (in a virtual env for example)
2. roscore is not implemented fully (logging is not supported), but you
   can run roscore manually::

   $ rosmaster --core -p 11311

3. you can then run any of the standard command line tools::

   $ rostopic pub /foo std_msgs/String bar

4. or you can run your ros based application::

   $ my-ros-app.py


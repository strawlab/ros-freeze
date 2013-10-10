ROS Freeze
==========

Ros Freeze converts an entire (pure python only) ROS package to
a python source or binary distribution which includes all dependencies and
ROS components required to run.

This tool has been tested on ROS Electric where it has been used to convert
complex python ROS applications with dozens of dependencies to standalone
python packages.

By default this builds a python package containig rospy
and all its dependencies, including the core ros command
line tools (rostopic, rosnode, etc) and std_msgs.

To modify this to freeze *your* ROS package edit MY_PACKAGE in setup.py

Converting a ROS pacakge to a pure python package
-------------------------------------------------

1. freeze the ROS package::

   $ source /path/to/your/ros/environment.sh
   $ python setup.py build

2. build an egg::

   $ python setup.py bdist_egg

Running the pure python ROS
---------------------------

1. install the egg file (in a virtual env for example)
2. roscore is not implemented fully (logging is not supported), but you
   can run roscore manually::

   $ rosmaster --core -p 11311

3. you can then run any of the standard command line tools::

   $ rostopic pub /foo std_msgs/String bar

4. or you can run your ros based application::

   $ my-ros-app.py


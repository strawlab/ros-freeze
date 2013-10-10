ROS Freeze
==========

Ros Freeze can freeze and entire (pure python only) ROS stack to
a python source or binary distribution. This software has been tested
on ROS Electric. By default this builds a python package containig rospy
and all its dependencies, including the core ros command
line tools (rostopic, rosnode, etc) and std_msgs.

To modify this to freeze your ROS package edit MY_PACKAGE in setup.py

Building the python package
---------------------------

  $source /path/to/your/ros/environment.sh
  $python setup.py build

to build an egg

  $python setup.py bdist_egg

Running the pure python ROS
---------------------------

1. install the egg file (in a virtual env for example)
2. roscore is not implemented fully (logging is not supported), but you
   can run roscore manually

   $rosmaster --core -p 11311

3. you can then run any of the standard command line tools

   $rostopic pub /foo std_msgs/String bar

4. or you can run your ros based application

   $my-ros-app.py


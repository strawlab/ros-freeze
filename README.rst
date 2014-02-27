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

How to use (simple)
"""""""""""""""""""

After checking out this repository, use the included ``ros-freeze-package``
command

   $ ./ros-freeze-package --version 0.3 my_ros_package

the command will try and guess your name and email from your git configuration.
you can also set them manually using ``--author`` and ``email``. You can also
build an egg binary package using ``--egg``.

   $ ./ros-freeze-package --egg --version 0.3 my_ros_package

How to use (advanced)
"""""""""""""""""""""

You may wish to integrate ros-freeze into your build system, such as by adding
a setup.py to your ros package. For example, this allows you to use
ros-freeze to build a standalone python package every time you rebuild your ROS
package.

*examples/example-setup.py* contains is an example setup.py file that you may,
from this source directory if you wish, modify and use to freeze your ROS package.

Converting a ROS pacakge to a pure python package
-------------------------------------------------

1. modify the included setup-freeze.py (edit MY_PACKAGE)

2. freeze the ROS package::

   $ source /path/to/your/ros/environment.sh
   $ python setup-freeze.py build

2. build an egg::

   $ python setup.py bdist_egg

Running a complex pure python ROS package
"""""""""""""""""""""""""""""""""""""""""

1. install the frozen ROS package (in a virtual env for example)
2. roscore is not implemented fully (logging is not supported), but you
   can run roscore manually::

   $ rosmaster --core -p 11311

3. you can then run any of the standard command line tools::

   $ rostopic pub /foo std_msgs/String bar

4. or you can run your ros based application::

   $ my-ros-app.py


import shutil
import os.path
import roslib.packages

def _copy_pkg_data(p, file, ddir):
    src = os.path.join(
            roslib.packages.get_pkg_dir(p, required=True),file)
    dest = os.path.join(ddir,p)

    if os.path.isdir(src):
        dest = os.path.join(dest,os.path.basename(src))
        shutil.copytree(src,dest)
    else:
        if not os.path.isdir(dest):
            os.makedirs(dest)
        shutil.copy2(src,dest)

    
def _import_and_copy(p, odir):
    mod = __import__(p)
    fn = mod.__file__
    if os.path.basename(fn).startswith("__init__"):
        shutil.copytree(
            os.path.dirname(fn),
            os.path.join(odir,p),
            ignore=shutil.ignore_patterns("*.pyc")
        )
    elif os.path.isfile(fn) and fn.endswith(".pyc"):
        #this is just a file, not a module. copy the py (not pyc) file
        shutil.copy2(fn[0:-1],odir)

    return fn

def _copy_executables(p, bdir):
    for f in os.listdir(p):
        path = os.path.join(p,f)
        #executable
        if os.access(path, os.X_OK) and os.path.isfile(path):
            with open(path,'r') as exe:
                for line in exe:
                    if "python" in line:
                        shutil.copy2(path,os.path.join(bdir,f))
                    break

def _import_roslaunch(srcdir,bindir,ddir):
    import_packages(srcdir,bindir,ddir,"rosmaster","roslaunch")
    _copy_pkg_data("roslaunch","roscore.xml",ddir)

    #FIXME: rewrite roscore here...

def _import_roslib(srcdir,bindir,ddir):
    _import_and_copy("ros",srcdir)
    _import_and_copy("roslib",srcdir)
    #rewrite roslib to make load_manifest a noop and to set some env variables

    #FIXME: use setuptools to get the installation /bin path and datadir
    contents = """
import os.path
import tempfile

os.environ['ROS_PACKAGE_PATH'] = tempfile.mkdtemp()
os.environ['ROS_ROOT'] = os.environ.get('ROS_ROOT','/usr/local')
os.environ['ROS_BUILD'] = os.environ['ROS_ROOT']
os.environ['ROS_MASTER_URI'] = os.environ.get('ROS_MASTER_URI','http://localhost:11311')

from roslib.scriptutil import is_interactive, set_interactive
import roslib.stacks

#from roslib.launcher import load_manifest
def load_manifest(*args):
    pass

def _get_pkg_dir(package, required=True, ros_root=None, ros_package_path=None):
    p = os.path.join('/home/stowers/Desktop/pyros/data',package)
    print "monkey patched get_pkg/stack_dir",package,"=",p
    return p

import roslib.packages
roslib.packages.get_pkg_dir = _get_pkg_dir

def _get_stack_dir(stack, env=None):
    return _get_pkg_dir(stack)

roslib.stacks.get_stack_dir = _get_stack_dir

import roslib.manifest
def _manifest_file_by_dir(package_dir, required=True, env=None):
    print "monkey patching manifest for", package_dir
    tdir = tempfile.mkdtemp()
    dest = os.path.join(tdir,'manifest.xml')
    with open(dest,'w') as f:
        f.write('<package></package>')
    return dest
roslib.manifest._manifest_file_by_dir = _manifest_file_by_dir

"""
    with open(os.path.join(srcdir,'roslib','__init__.py'),'w') as f:
        f.write(contents)

def _import_ros_binaries(bdir):
    rosroot = os.environ['ROS_ROOT']
    _copy_executables(os.path.join(rosroot,"bin"), bdir)

def import_msgs(srcdir,bindir,ddir,*pkgs):
    for p in pkgs:
        import_packages(srcdir,bindir,ddir,p)
        _copy_pkg_data(p, "msg", ddir)

def import_srvs(srcdir,bindir,ddir,*pkgs):
    for p in pkgs:
        import_packages(srcdir,bindir,ddir,p)
        _copy_pkg_data(p, "srv", ddir)

def import_packages(srcdir,bindir,ddir,*pkgs):
    for p in pkgs:
        roslib.load_manifest(p)
        fn = _import_and_copy(p, srcdir)

        base  = os.path.abspath(roslib.packages.get_pkg_dir(p, required=True))
        _copy_pkg_data(p, os.path.join(base,"manifest.xml"), ddir)

        for _bin in ("bin","scripts"):
            _bindir = os.path.abspath(
                            os.path.join(os.path.dirname(fn), "..","..",_bin))
            if os.path.isdir(_bindir):
                _copy_executables(_bindir, bindir)

def import_ros_core(srcdir, bindir, ddir):
    for d in (srcdir,bindir,datadir):
        if os.path.exists(d):
            shutil.rmtree(d)
        os.mkdir(d)

    _import_roslib(srcdir,bindir,datadir)
    _import_roslaunch(srcdir,bindir,datadir)
    _import_ros_binaries(bindir)

    import_srvs(srcdir,bindir,datadir,"std_srvs")
    import_msgs(srcdir,bindir,datadir,"std_msgs","geometry_msgs","rosgraph_msgs")
    import_packages(srcdir,bindir,datadir,"rosgraph","rostopic","rosnode","rospy","rosbag")

if __name__ == "__main__":
    srcdir = "./src"
    bindir = "./bin"
    datadir = "./data"

    import_ros_core(srcdir, bindir, datadir)



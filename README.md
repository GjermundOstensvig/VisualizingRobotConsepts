# VisualizingRobotConsepts
This repo. was made to visualize robot consepts like Kinematics and ROS.

I'd like to use ROS2 as it is more mature at this point and since it is available on Ubuntu, Windows, and MacOS, whereas ROS1 is only available on Ubuntu.
This will make it easier for students to use.
The distro. of ROS2 I plan to use is [Iron Irwini](https://docs.ros.org/en/iron/index.html).
For the first version, I'll program this using Ubuntu 22.04 (Jammy). This is because Iron Irwini is only supported on Windows 10, and I have Windows 11. In the future I might consider making a docker container that can run my code on any OS.
I'll be using rviz for the visualtzation, and the python programming language.
The original CAD files for the h_bot robot were designed by Haris Jasarevic. They were provided as `.iges` files and were converted to `.dae` files using FreeCad.

## How to install on Ubuntu 22.04 
- Install the ROS2 Iron Irwini distrobution globally following [this guide](https://docs.ros.org/en/iron/Installation.html). 

**_NOTE:_**  Please use the Debian package installation using `apt` instead of building from source, or installing from downloaded binary. The following steps for sourcing your environment will fail if you got this wrong. 

- Clone this git repo

```
git clone https://github.com/GjermundOstensvig/VisualizingRobotConsepts.git
``````

Setup your sources by running the following command. After you've run this, every time you start a new terminal, it will automatically souce the correct files. 
```
echo "source /opt/ros/iron/setup.bash # For ros2 iron environment (underlay) 
source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash # For autocompleting colcon options" >> ~/.bashrc
```

To check that you have the correct distro installed of ROS, and to se that you sourced the ROS environment properly you can run this:
```
printenv | grep -i ROS_DISTRO
```
you should expec to see `ROS_DISTRO=iron`

Running the following will let you know that your ROS distro was installed in the correct loaction:
```
ls /opt/ros
```
You should expect to see the names of all installed ros distros. In my case that's `humble` and `iron`.

## How to build 

The following commands should create three new folders in addition to `src` called `build`, `install`, and  `log`.
```
cd VisualizingRobotConsepts/ros2_ws/
```

```
colcon build
```
Once built, you can source your overlay:
```
echo "source ~/VisualizingRobotConsepts/ros2_ws/install/setup.bash # For my custom ros overlay" >> ~/.bashrc
```

To only build one package instead of all packages in the workspace, run:
```
colcon build --packages-select <package_name>
```

## Running things

After successfully building and sourcing the overlay, you can run the following to run the `my_joint_state_publisher` node:
```
ros2 run robot_consepts_viz_pkg my_joint_state_publisher
```

To start the visualizer, run the following command:
```
ros2 run rviz2 rviz2
```
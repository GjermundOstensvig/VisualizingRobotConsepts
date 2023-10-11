# VisualizingRobotConsepts
This repo. was made to visualize robot consepts like Kinematics and ROS.

I'd like to use ROS2 as it is more mature at this pointand and since it is available on Ubuntu, Windows, and MacOS, whereas ROS1 is only available on Ubuntu.
This will make it easier for students to use.
The distro. of ROS2 I plan to use is [Iron Irwini](https://docs.ros.org/en/iron/index.html).
For the first version, I'll program this using Ubuntu 22.04 (Jammy). This is because Humble Hawksbill is only supportedon Windows 10, and I have Windows 11. In the future I might consider making a docker container that can run my code on any OS.
I'll be using rviz for the visualtzation, and the python programming language.

## How to use on Ubuntu 22.04 
- Install the ROS2 Humble Hawksbill distrobution globally following [this guide](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html). 
- Clone this git repo

`git clone https://github.com/GjermundOstensvig/VisualizingRobotConsepts.git`
- Go to your barhrc file

`gedit ~/.bashrc`
- Setup your sources by atting the following lines at the bottom of the file, save and exit:
```
source /opt/ros/humble/setup.bash # For ros humble environment
source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash # For autocompleting colcon options
source ~/VisualizingRobotConsepts/ros2_ws/install/setup.bash # For my custom ros overlay
```

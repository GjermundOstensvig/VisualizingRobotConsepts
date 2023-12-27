from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
import os.path
from launch.substitutions import PathJoinSubstitution
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command


def generate_launch_description():
    ld = LaunchDescription()

    package_path = get_package_share_directory("robot_consepts_viz_pkg")
    rviz_config_path = PathJoinSubstitution(
        [package_path, "rviz", "my_rviz_config.rviz"]
    )
    urdf_path = os.path.join(package_path, "urdf", "h_bot.urdf")

    robot_description_content = ParameterValue(
        Command(["xacro ", urdf_path]), value_type=str
    )
    ld.add_action(
        Node(
            package="rviz2",
            executable="rviz2",
            output="screen",
            arguments=["-d", rviz_config_path],
        ),
    )
    # This loads the urdf using the joint_state_publicher package.
    # TODO: Is in necessary to use this extra node to load the urdf?
    ld.add_action(
        Node(
            name="robot_state_publisher",
            package="robot_state_publisher",
            executable="robot_state_publisher",
            parameters=[{"robot_description": robot_description_content}],
        ),
    )
    # This runc our custom joint state publisher to control the loaded urdf.
    ld.add_action(
        Node(
            name="my_joint_state_publisher",
            package="robot_consepts_viz_pkg",
            executable="my_joint_state_publisher",
            parameters=[{"robot_description": robot_description_content}],
        ),
    )

    return ld

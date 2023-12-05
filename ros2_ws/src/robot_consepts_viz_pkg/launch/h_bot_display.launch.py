from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    ld = LaunchDescription()

    package_path = FindPackageShare('robot_consepts_viz_pkg')
    default_model_path = PathJoinSubstitution(['urdf', 'h_bot.urdf.xacro'])
    default_rviz_config_path = PathJoinSubstitution([package_path, 'rviz', 'my_rviz_config.rviz'])
    rviz_arg = DeclareLaunchArgument(name='rvizconfig', default_value=default_rviz_config_path,
                                     description='Absolute path to rviz config file')
    ld.add_action(rviz_arg)

    model_arg = DeclareLaunchArgument(name='model', default_value=default_model_path,
                                        description='Path to robot urdf file relative to urdf_tutorial package')
    ld.add_action(model_arg)

    ld.add_action(IncludeLaunchDescription(
        launch_description_source=PathJoinSubstitution([FindPackageShare('urdf_launch'), 'launch', 'display.launch.py']),
        launch_arguments={
            'urdf_package': 'robot_consepts_viz_pkg',
            'urdf_package_path': LaunchConfiguration('model'),
            'rviz_config': LaunchConfiguration('rvizconfig')
        }.items()
    ))

    return ld

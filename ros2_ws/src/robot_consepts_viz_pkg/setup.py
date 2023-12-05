from glob import glob
from setuptools import find_packages, setup

package_name = "robot_consepts_viz_pkg"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (
            "share/" + package_name + "/meshes/stl",
            glob(pathname="meshes/**/**/*.stl", recursive=True),
        ),
        (
            "share/" + package_name + "/meshes/dae",
            glob(pathname="meshes/**/**/*.dae", recursive=True),
        ),
        ("share/" + package_name + "/launch", ["launch/h_bot_gui.launch.py"]),
        ("share/" + package_name + "/urdf", ["urdf/h_bot.urdf"]),
        ("share/" + package_name + "/rviz", ["rviz/my_rviz_config.rviz"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="gjermund",
    maintainer_email="gjermund1995@gmail.com",
    description="TODO: Package description",
    license="MIT",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "my_joint_state_publisher = robot_consepts_viz_pkg.my_joint_state_publisher:main"
        ],
    },
)

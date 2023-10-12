from setuptools import find_packages, setup

package_name = 'my_joint_state_publisher_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gjermund',
    maintainer_email='gjermund1995@gmail.com',
    description='TODO: Package description',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_joint_state_publisher = my_joint_state_publisher_package.my_joint_state_publisher:main'
        ],
    },
)

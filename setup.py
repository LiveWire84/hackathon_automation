# from setuptools import find_packages
# from setuptools import setup

# setup(
#     name='src',
#     version='0.1.1',
#     packages=find_packages(
#         include=('src', 'src.*')),
# )
from setuptools import setup
from setuptools import find_packages

package_name = 'hackathon_automation'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(include=[package_name, package_name + '.*']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'path_planner = hackathon_automation.path_planner:main',
            'tb3_controller = hackathon_automation.controller:main',
            'colour_detector = hackathon_automation.colour_detection:main',
        ],
    },
)

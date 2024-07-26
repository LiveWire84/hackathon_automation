cmake_minimum_required(VERSION 3.5)
project(hackathon_automation)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

if(MSVC)
  add_compile_definitions(_USE_MATH_DEFINES)
endif()

################################################################################
# Find ament packages and libraries for ament and system dependencies
################################################################################
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(PkgConfig REQUIRED)
pkg_check_modules(GAZEBO REQUIRED gazebo)

find_package(gazebo_ros_pkgs REQUIRED)
find_package(geometry_msgs REQUIRED)
# find_package(nav_msgs REQUIRED)
# find_package(rclcpp REQUIRED)
# find_package(rclpy REQUIRED)
# find_package(sensor_msgs REQUIRED)
# find_package(tf2 REQUIRED)

################################################################################
# Build
################################################################################
# Use pkg-config to get the necessary include and library paths
execute_process(COMMAND pkg-config --cflags-only-I gazebo OUTPUT_VARIABLE GAZEBO_CFLAGS)
execute_process(COMMAND pkg-config --libs-only-L gazebo OUTPUT_VARIABLE GAZEBO_LFLAGS)
execute_process(COMMAND pkg-config --libs-only-l gazebo OUTPUT_VARIABLE GAZEBO_LIBS)

# Strip the '-I' and '-L' from the beginning of the include and library paths
string(REPLACE "-I" "" GAZEBO_CFLAGS ${GAZEBO_CFLAGS})
string(REPLACE "-L" "" GAZEBO_LFLAGS ${GAZEBO_LFLAGS})

# Convert to list
separate_arguments(GAZEBO_CFLAGS)
separate_arguments(GAZEBO_LFLAGS)
separate_arguments(GAZEBO_LIBS)

message(STATUS "GAZEBO_CFLAGS: ${GAZEBO_CFLAGS}")
message(STATUS "GAZEBO_LFLAGS: ${GAZEBO_LFLAGS}")
message(STATUS "GAZEBO_LIBS: ${GAZEBO_LIBS}")

# Include and link directories
include_directories(${GAZEBO_CFLAGS})
link_directories(${GAZEBO_LFLAGS})

set(dependencies
  "geometry_msgs"
  # "nav_msgs"
  # "rclcpp"
  "sensor_msgs"
  # "tf2"
)

install(DIRECTORY launch models worlds
  DESTINATION share/${PROJECT_NAME}/
)

# install(PROGRAMS  
#   scripts/controller.pt
#   DESTINATION lib/${PROJECT_NAME} )

# Add additional files for installation, if needed
# install(FILES my_file.py
#   DESTINATION share/${PROJECT_NAME}/
# )

ament_python_install_package(${PROJECT_NAME})

install(PROGRAMS
  hackathon_automation/path_planner.py
  DESTINATION lib/${PROJECT_NAME})
ament_package()


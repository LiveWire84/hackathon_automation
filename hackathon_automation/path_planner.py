#! /usr/bin/env python3
########################################################################################################

# Wassup! This is where your Path Planning code goes for the Automation Task of the ERC Hackathon '24
#
# Remember to use the transform points function in obstacle_detection.py to get points corresponding to
#         your path in the gazebo coordinate system. This is what controller.py should use!!
#
#                                       Happy Planning!!!

########################################################################################################

# import functions from obstacle_detection.py

# Cooridinates of the cones as per the map (image version) - look at get_landmarks.py & obstacle_detection.py
# ERC Room: 109, 296
# Cone 1: 159, 208
# Cone 2: 296, 142
# Cone 3: 502, 539
# Cone 4: 244, 640
# Cone 5: 190, 326

# You can look at the visualization function in demo.py to see how to visualize the path

# These are the coordinates you have to go to in Gazebo
# Start Location (ERC Room): 12.994061, 14.233000
# Cone 1 (near Sandbox): 19.765875, 10.429128
# Cone 2 (NAB): 24.820259, -0.089209
# Cone 3 (VGH): -5.729289, -15.973051
# Cone 4 (SAC): -13.520048, 3.922464
# Cone 5 (BDome): 10.654515,8.028189
# Cones colors will be randomized

# There is a function to convert the obstacle_detection-> Maze-> points point_transform


import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PathPlanner(Node):
    def __init__(self):
        super().__init__('path_planner')
        #self.publisher_ = self.create_publisher(String, '/planned_path', 10)
        #self.timer = self.create_timer(1.0, self.publish_path)
        self.get_logger().info("TEST_PYTHON")

    def publish_path(self):
        msg = String()
        msg.data = "Planned path coordinates"
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing planned path: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = PathPlanner()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


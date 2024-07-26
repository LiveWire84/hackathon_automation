########################################################################################################

# Wassup! This is where your controller code goes for the Automation Task of the ERC Hackathon '24
#                                      ( Don't ) Lose Control!!!

########################################################################################################
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class TB3Controller(Node):
    def __init__(self):
        super().__init__('tb3_controller')
        self.subscription_path = self.create_subscription(
            String,
            '/planned_path',
            self.path_callback,
            10)
        self.subscription_odom = self.create_subscription(
            String,
            '/odom',
            self.odom_callback,
            10)
        self.publisher_cmd_vel = self.create_publisher(Twist, '/cmd_vel', 10)
        self.path = None

    def path_callback(self, msg):
        self.path = msg.data
        self.get_logger().info('Received path: "%s"' % msg.data)
        self.follow_path()

    def odom_callback(self, msg):
        # Process odometry data here
        pass

    def follow_path(self):
        if self.path:
            msg = Twist()
            # Set your velocities here
            msg.linear.x = 0.5
            msg.angular.z = 0.1
            self.publisher_cmd_vel.publish(msg)
            self.get_logger().info('Publishing velocity command')

def main(args=None):
    rclpy.init(args=args)
    node = TB3Controller()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()



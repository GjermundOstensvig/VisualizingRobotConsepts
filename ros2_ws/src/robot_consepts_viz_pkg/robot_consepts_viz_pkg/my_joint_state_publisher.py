import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from sensor_msgs.msg import JointState


class HBotJointStatePublisher(Node):
    def __init__(self):
        super().__init__("h_bot_joint_state_publisher")
        self.jsp = self.create_publisher(
            msg_type=JointState, topic="joint_states", qos_profile=10
        )
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.joint_state = [0, 0, 0, 0, 0, 0]

    def timer_callback(self):
        # update joint state message
        joint_state_msg = JointState()
        now = self.get_clock().now()
        joint_state_msg.header.stamp = now.to_msg()
        joint_state_msg.name = [
            "joint_1",
            "joint_2",
            "joint_3",
            "joint_4",
            "joint_5",
            "joint_6",
        ]
        joint_state_msg.position = self.joint_state
        self.jsp.publish(joint_state_msg)
        self.get_logger().info('Publishing: "%s"' % joint_state_msg.position)

        # increment joint states
        for i, q in enumerate(self.joint_state):
            self.joint_state[i] = round(self.joint_state[i] + 0.01, 3)


def main(args=None):
    rclpy.init(args=args)

    node = HBotJointStatePublisher()
    rclpy.spin(node)


if __name__ == "__main__":
    main()

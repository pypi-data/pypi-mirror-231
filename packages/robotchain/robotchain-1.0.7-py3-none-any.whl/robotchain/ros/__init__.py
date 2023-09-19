import roslibpy
import app as app_file

class ROS:

    def __init__(self, framework):
        self._framework = framework
        self.client = roslibpy.Ros(host="127.0.0.1", port=9090)
        self.received_message = ""

    def subscribe(self, topic):
        topic_data = False
        if self.client.is_connected:
            topic_data = roslibpy.Topic(self.client, topic, "std_msgs/String")
            topic_data.subscribe(self.subscribe_callback)
        return topic_data

    def subscribe_callback(self, message):
        self.received_message = message["data"]
        robot_message = "robot_message"
        if robot_message in dir(app_file):
            getattr(app_file, robot_message)(self._framework, self.received_message)
        pass

    def publisher(self, topic, message):
        topic_data = False
        if self.client.is_connected:
            topic_data = roslibpy.Topic(self.client, topic, "std_msgs/String")
            topic_data.publish({"data": self._framework.utils.json.dumps(message)})
        return topic_data

    def publish_string(self, topic, message):
        topic_data = False
        if self.client.is_connected:
            topic_data = roslibpy.Topic(self.client, topic, "std_msgs/String")
            topic_data.publish({"data": message})
        return topic_data

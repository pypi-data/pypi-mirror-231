import sys
import signal
import app as app_file
from .board import Board
from .utils import Utils
from .ros import ROS

class Init:

    def __init__(self):
        signal.signal(signal.SIGINT, self.sigint_handler)
        signal.signal(signal.SIGTERM, self.sigint_handler)
        self.board = Board(self)
        self.utils = Utils(self)
        self.ros = ROS(self)
        self.setup()

    def setup(self):
        self.ros.client.run()
        self.utils.log.robot_start("Robot start.")
        robot_start = "robot_start"
        if robot_start in dir(app_file):
            getattr(app_file, robot_start)(self)
        self.sigint_handler(False, False)

    def sigint_handler(self, signum, frame):
        robot_exit = "robot_exit"
        if robot_exit in dir(app_file):
            getattr(app_file, robot_exit)(self)
        self.utils.log.robot_exit("Robot exit.")
        self.utils.time.sleep(.2)
        sys.exit()

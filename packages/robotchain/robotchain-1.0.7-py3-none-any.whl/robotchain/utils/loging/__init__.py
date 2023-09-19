import logging
import colorlog
import websocket
import threading
import json

class Loging:

    def __init__(self):
        self.socket = None
        self.socket_status = False
        self.task = threading.Thread(name="socket_task", target=self.task)
        self.task.daemon = True
        self.logger = logging.getLogger(None)
        self.logger.handlers = []
        self.logger.setLevel(logging.DEBUG)
        console_fmt = "%(log_color)s%(asctime)s %(levelname)s: %(message)s"
        color_config = {
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "purple",
        }
        console_formatter = colorlog.ColoredFormatter(fmt=console_fmt, log_colors=color_config)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)
        self.task.start()

    def task(self):
        websocket.enableTrace(False)
        self.socket = websocket.WebSocketApp("ws://127.0.0.1:10081/message/service", on_message=self.on_message, on_error=self.on_error, on_close=self.on_close)
        self.socket.on_open = self.on_open
        self.socket.run_forever()

    def on_open(self, ws):
        self.socket_status = True

    def on_message(self, ws, message):
        pass

    def on_error(self, ws, error):
        self.socket_status = False

    def on_close(self, ws):
        self.socket_status = False

    def debug(self, log):
        self.logger.debug(log)
        if self.socket_status:
            self.socket.send(json.dumps({"command": "program:software:debug", "data": log}))

    def info(self, log):
        self.logger.info(log)
        if self.socket_status:
            self.socket.send(json.dumps({"command": "program:software:info", "data": log}))

    def warning(self, log):
        self.logger.warning(log)
        if self.socket_status:
            self.socket.send(json.dumps({"command": "program:software:warning", "data": log}))

    def error(self, log):
        self.logger.error(log)
        if self.socket_status:
            self.socket.send(json.dumps({"command": "program:software:error", "data": log}))

    def critical(self, log):
        self.logger.critical(log)
        if self.socket_status:
            self.socket.send(json.dumps({"command": "program:software:critical", "data": log}))

    def robot_start(self, log):
        self.logger.info(log)
        if self.socket_status:
            self.socket.send(json.dumps({"command": "program:software:start"}))

    def robot_exit(self, log):
        self.logger.warning(log)
        if self.socket_status:
            self.socket.send(json.dumps({"command": "program:software:exit"}))

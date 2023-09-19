class Board:

    def __init__(self, framework):
        self._framework = framework
        self.send_message = ""
        self.key_status = 0
        self.cpu_temperature = 0.00
        self.mpu_pit = 0.000
        self.mpu_yaw = 0.000
        self.mpu_rol = 0.000
        self.mpu_temperature = 0.000
        self.mpu_altitude = 0.000
        self.mpu_pressure = 0.000

    def led_status(self, channel, status):
        message = {"type": "led-status", "channel": channel, "status": status}
        self.send_message = self._framework.utils.json.dumps(message)
        return self.send_message

    def io_mode(self, channel, mode):
        message = {"type": "io-mode", "channel": channel, "mode": mode}
        self.send_message = self._framework.utils.json.dumps(message)
        return self.send_message

    def io_status(self, channel, status):
        message = {"type": "io-status", "channel": channel, "status": status}
        self.send_message = self._framework.utils.json.dumps(message)
        return self.send_message

    def power_status(self, channel, channel_id, status):
        message = {"type": "power-status", "channel": channel, "id": channel_id, "status": status}
        self.send_message = self._framework.utils.json.dumps(message)
        return self.send_message

    def pwm_control(self, channel, width):
        message = {"type": "pwm", "channel": channel, "width": width}
        self.send_message = self._framework.utils.json.dumps(message)
        return self.send_message

    def key_status(self):
        message = {"type": "key-status"}
        self.send_message = self._framework.utils.json.dumps(message)
        return self.send_message

    def read_key_status(self):
        return self.key_status

    def cpu_temperature(self):
        message = {"type": "cpu-temperature"}
        self.send_message = self._framework.utils.json.dumps(message)
        return self.send_message

    def read_cpu_temperature(self):
        return self.cpu_temperature

    def mpu_data(self):
        message = {"type": "mpu"}
        self.send_message = self._framework.utils.json.dumps(message)
        return self.send_message

    def read_mpu_data(self, data):
        if data == "pit":
            return self.mpu_pit
        if data == "yaw":
            return self.mpu_yaw
        if data == "rol":
            return self.mpu_rol
        if data == "temperature":
            return self.mpu_temperature
        if data == "altitude":
            return self.mpu_altitude
        if data == "pressure":
            return self.mpu_pressure
        return 0.000


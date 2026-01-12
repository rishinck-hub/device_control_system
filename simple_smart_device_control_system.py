from abc import abstractmethod,ABC


class Device(ABC):
    """The common parent class for devices"""

    def __init__(self):
        self.__is_on = False # private

    @abstractmethod
    def start(self):
        """initialize start method"""
        pass

    @abstractmethod
    def stop(self):
        """initialize stop method"""
        pass

    # Protected method to change the state of the device
    def _turn_on(self):
        """method to turn the device on"""
        self.__is_on = True

    def _turn_off(self):
        """method to turn the device off"""
        self.__is_on = False
    
    # Public method to check device status
    def is_on(self):
        """public method to return the device status"""
        return self.__is_on



class Motor(Device):
    """new device-Motor"""

    def start(self):
        if not self.is_on():
            self._turn_on()
            print("Motor has started")
    
    def stop(self):
        if self.is_on():
            self._turn_off()
            print("Motor has stopped")



class Light(Device):
    """new device-Light"""

    def start(self):
        if not self.is_on():
            self._turn_on()
            print("Light switched on")

    def stop(self):
        if self.is_on():
            self._turn_off()
            print("Light switched off")


class Controller:
    """Generic controller for operating any device"""

    def operate_device(self, device: Device):
        if not isinstance(device,Device):
            raise TypeError("Controller can operate only with Device objects")
        device.start()
        device.stop()


"""Testing"""
motor = Motor()
light = Light()

motor_controller = Controller()
light_controller = Controller()

motor_controller.operate_device(motor)
light_controller.operate_device(light)
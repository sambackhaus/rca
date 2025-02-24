from device import Device


class Static(Device):

    def __init__(self, state: int = 0):
        self.state = state

    def get_state(self):
        return self.state
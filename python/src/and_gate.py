from typing import List
from device import Device
from two_input_device import TwoInputDevice
from static import Static
from transistor import Transistor


class AndGate(TwoInputDevice):

    def __init__(self, a: List[Device]=None, b: List[Device]=None):
        super().__init__(a, b)

        self.t1 = Transistor(a=self.a, b=[Static(1)])
        self.t2 = Transistor(a=self.b, b=[self.t1])

    def get_state(self):
        return self.t2.get_state()

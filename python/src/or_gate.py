from typing import List
from device import Device
from two_input_device import TwoInputDevice
from static import Static
from transistor import Transistor


class OrGate(TwoInputDevice):

    def __init__(self, a: List[Device]=None, b: List[Device]=None):
        super().__init__(a, b)

        static_one = Static(1)

        self.t1 = Transistor(a=self.a, b=[static_one])
        self.t2 = Transistor(a=self.b, b=[static_one])

    def get_state(self):
        t1_state = self.t1.get_state()
        t2_state = self.t2.get_state()

        state = 1 if t1_state == 1 or t2_state == 1 else 0
        return state

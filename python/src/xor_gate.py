from typing import List
from and_gate import AndGate
from device import Device
from two_input_device import TwoInputDevice
from inverter import Inverter
from or_gate import OrGate


class XorGate(TwoInputDevice):

    def __init__(self, a: List[Device]=None, b: List[Device]=None):
        super().__init__(a, b)

        self.or_gate_1 = OrGate(a=self.a, b=self.b)
        self.and_gate = AndGate(a=self.a, b=self.b)

        self.inverter_1 = Inverter(a=[self.or_gate_1])

        self.or_gate_2 = OrGate(a=[self.inverter_1], b=[self.and_gate])

        self.inverter_2 = Inverter(a=[self.or_gate_2])

    def get_state(self):
        return self.inverter_2.get_state()

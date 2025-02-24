from typing import List

from adder import Adder
from and_gate import AndGate
from device import Device
from xor_gate import XorGate


class HalfAdder(Adder):

    def __init__(self, a: List[Device]=None, b: List[Device]=None):
        super().__init__(a, b)

        self.xor_gate = XorGate(a=self.a, b=self.b)
        self.and_gate = AndGate(a=self.a, b=self.b)

    def get_state(self):
        return self.xor_gate.get_state()

    def get_cout(self):
        return self.and_gate.get_state()

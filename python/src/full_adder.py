from typing import List
from adder import Adder
from and_gate import AndGate
from device import Device
from half_adder import HalfAdder
from or_gate import OrGate
from static import Static
from xor_gate import XorGate


class FullAdder(Adder):

    cin: List[Device] = None

    def __init__(self, a: List[Device], b: List[Device], cin: List[Device]):
        super().__init__(a=a, b=b)

        if cin is None:
            cin = []
        self.cin = cin

        self.half_adder_1 = HalfAdder(a=self.a, b=self.b)
        self.half_adder_2 = HalfAdder(a=[self.half_adder_1], b=self.cin)
        self.or_gate = OrGate(a=[Static(self.half_adder_1.get_cout())], b=[Static(self.half_adder_2.get_cout())])

    def get_state(self):
        return self.half_adder_2.get_state()
    
    def get_cout(self):
        return self.or_gate.get_state()

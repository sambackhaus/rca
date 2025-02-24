from typing import List
from adder import Adder
from and_gate import AndGate
from device import Device
from or_gate import OrGate
from xor_gate import XorGate


class FullAdder(Adder):

    cin: List[Device] = None

    def __init__(self, a: List[Device], b: List[Device], cin: List[Device]):
        super().__init__(a=a, b=b)

        if cin is None:
            cin = []
        self.cin = cin

        self.xor_gate_1 = XorGate(a=self.a, b=self.b)
        self.and_gate_1 = AndGate(a=self.a, b=self.b)

        self.xor_gate_2 = XorGate(a=[self.xor_gate_1], b=self.cin)
        self.and_gate_2 = AndGate(a=[self.xor_gate_1], b=self.cin)

        self.or_gate = OrGate(a=[self.and_gate_2], b=[self.and_gate_1])

    def get_state(self):
        return self.xor_gate_2.get_state()
    
    def get_cout(self):
        return self.or_gate.get_state()
    
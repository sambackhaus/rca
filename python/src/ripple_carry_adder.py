from typing import List
from device import Device
from full_adder import FullAdder
from multiple_input_device import MultipleInputDevice
from static import Static


class RippleCarryAdder(MultipleInputDevice):

    cin: List[Device] = None

    def __init__(self, n_inputs: int, a_ins: List[List[Device]], b_ins: List[List[Device]], cin: List[Device]):
        super().__init__(n_inputs=n_inputs, a_ins=a_ins, b_ins=b_ins)

        if cin is None:
            cin = []
        self.cin = cin

        self.first_full_adder = FullAdder(a=self.a_ins[0], b=self.b_ins[0], cin=self.cin)
        self.last_adder = self.first_full_adder

        self.all_adders = [self.first_full_adder]

        for i in range(1, self.n_inputs):
            full_adder_n = FullAdder(a=a_ins[i], b=b_ins[i], cin=[Static(self.last_adder.get_cout())])
            self.all_adders.append(full_adder_n)
            self.last_adder = full_adder_n

    def get_state(self):
        return [fa.get_state() for fa in self.all_adders]

    def get_cout(self):
        return self.last_adder.get_cout()
        
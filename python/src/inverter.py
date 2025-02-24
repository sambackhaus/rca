from typing import List
from device import Device


class Inverter(Device):

    a: List[Device] = None

    def __init__(self, a : List[Device]=None):
        if a is None:
            a = []
        self.a = a

    def get_state(self):
        states_are_zero = [v.get_state() == 0 for v in self.a]

        state = 1 if all(states_are_zero) else 0
        return state

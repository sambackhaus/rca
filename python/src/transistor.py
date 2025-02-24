from typing import List
from device import Device
from two_input_device import TwoInputDevice


class Transistor(TwoInputDevice):
    
    def get_state(self):
        g_states = [v.get_state() == 1 for v in self.a]
        d_states = [v.get_state() == 1 for v in self.b]
        state = 1 if any(g_states) and any(d_states) else 0

        return state
    

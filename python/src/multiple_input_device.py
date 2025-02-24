from typing import List
from device import Device


class MultipleInputDevice(Device):

    n_inputs: int = 0
    a_ins: List[List[Device]] = None
    b_ins: List[List[Device]] = None

    def __init__(self, n_inputs: int, a_ins: List[List[Device]]=None, b_ins: List[List[Device]]=None):
        if n_inputs < 1:
            raise Exception(f"Illegal amount of inputs: {n_inputs}")
        
        self.n_inputs = n_inputs

        if a_ins is None:
            a_ins = []
        self.a_ins = a_ins

        if b_ins is None:
            b_ins = []
        self.b_ins = b_ins

        if len(a_ins) != n_inputs or len(b_ins) != n_inputs:
            raise Exception("Invalid amout of a or b inputs provied")

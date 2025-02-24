from abc import abstractmethod
from typing import List
from device import Device


class TwoInputDevice(Device):

    a: List[Device] = None
    b: List[Device] = None

    def __init__(self, a: List[Device]=None, b: List[Device]=None):

        if a is None:
            a = []
        self.a = a

        if b is None:
            b = []
        self.b = b
        
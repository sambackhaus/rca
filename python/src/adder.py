from abc import abstractmethod
from two_input_device import TwoInputDevice


class Adder(TwoInputDevice):

    @abstractmethod
    def get_cout():
        pass
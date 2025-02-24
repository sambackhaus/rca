from abc import ABC, abstractmethod

class Device(ABC):

    state: int = 0

    @abstractmethod
    def get_state(self):
        pass        

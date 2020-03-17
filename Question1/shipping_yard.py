from abc import ABC, abstractmethod
 
class Perahu_Abstract(ABC):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        super().__init__()
    
    @abstractmethod
    def penggerak(self):
        pass

    @abstractmethod
    def wilayah_operasi(self):
        pass

class PerahuLayar(Perahu_Abstract):
    def penggerak(self):
        return "Layar"

    def wilayah_operasi(self):
        return "Danau"

class PerahuMotor(Perahu_Abstract):
    def penggerak(self):
        return "Motor"

    def wilayah_operasi(self):
        return "Danau"

class KapalPesiar(Perahu_Abstract):
    def penggerak(self):
        return "Motor"

    def wilayah_operasi(self):
        return "Laut"

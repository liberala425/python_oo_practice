"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """initialize the serial generator"""
        self.start = start
        self.serialNum = start
        self.increment = 0
    
    def generate(self):
        """increment 1 each time calling generator function"""
        
        self.serialNum = self.start + self.increment 
        self.increment += 1
        return self.serialNum

    def reset(self):
        """reset serial number to be the start number"""
        self.serialNum = self.start
        self.increment = 0

    def __repr__(self):
        """Show serial representation."""
        return f"<SerialGenerator start={self.start} next={self.start + 1}>"
    


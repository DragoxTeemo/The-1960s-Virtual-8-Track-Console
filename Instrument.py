class Instruments:
    def __init__(self, name, frequency, energy, volume=5, label=None):
        self.name = name
        self.frequency = frequency
        self.energy = energy
        self.bounce_count = 0
        # If no label is given, just use the name
        self.label = label if label else name

    def __repr__(self):
        return f"[{self.label}] (Energy: {self.energy}, Vol: {self.volume}, Bounce: {self.bbounce_count})"
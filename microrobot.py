class MicroRobot:
    def __init__(self, position, identifier) -> None:
        self.position = position
        self.identifier = identifier

    def move(self, new_pos):
        self.position = new_pos
    
    
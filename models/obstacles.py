class Obstacle:
    def __init__(self, start_pos, end_pos, color : str = "red" , width : int = 8):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.width = width
        self.color = color
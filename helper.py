import math

def calculate_velocity(start_position: tuple, end_position: tuple):
    x1, y1 = start_position
    x2, y2 = end_position
    return (x2 - x1, y2 -y1)
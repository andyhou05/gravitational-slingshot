import math

## Fg = Gm1m2/r**2



def calculate_velocity(start_position: tuple, end_position: tuple):

    x1, y1 = start_position
    x2, y2 = end_position



    return (x2 - x1, y2 -y1)


def gravitational_gravity(start_position: tuple):
    x, y = start_position
    dx = x - 400
    dy = y - 300
    distance = math.sqrt(dx ** 2 + dy ** 2)

    if distance == 0:
        return (0, 0)

    G = 6.67*10**-11 * 5.972*(10**24)
    acc_magnitude = G / (distance*100000)** 2


    acc_x = -acc_magnitude * (dx / distance)
    acc_y = -acc_magnitude * (dy / distance)

    return (acc_x, acc_y)

import math
from models.planet import Planet

## Fg = Gm1m2/r**2



def calculate_velocity(start_position: tuple, end_position: tuple):

    x1, y1 = start_position
    x2, y2 = end_position



    return (x2 - x1, y2 -y1)

def distance_calc(start_position: tuple,end_position : tuple):
    # USED TO GET DISTANCE ONLY, NOT THE ACCELERATION
    x, y = start_position
    x1,y1 = end_position
    dx = x - x1
    dy = y - y1
    return math.sqrt(dx ** 2 + dy ** 2)

def gravitational_acceleration(projectile_position: tuple, planet: Planet):
    x_projectile, y_projectile = projectile_position
    x_planet, y_planet = planet.position
    dx = x_projectile - x_planet
    dy = y_projectile - y_planet
    distance = math.sqrt(dx ** 2 + dy ** 2)

    if distance == 0:
        return (0, 0)

    G = 1000
    acc_magnitude = (G * planet.radius) / (distance)** 2

    acc_x = -acc_magnitude * (dx / distance)
    acc_y = -acc_magnitude * (dy / distance)

    return (acc_x, acc_y)

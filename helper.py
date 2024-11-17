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

    G = 6.67*(10**-11)*5.97*(10**24)
    acc_magnitude = (G) / (distance*100000)** 2

    acc_x = -acc_magnitude * (dx / distance)
    acc_y = -acc_magnitude * (dy / distance)

    return (acc_x, acc_y)

def circle_line_collison(cx, cy, r, x1, y1, x2, y2):
    # Vector from line start to circle center
    acx, acy = cx - x1, cy - y1
    # Vector of the line segment
    abx, aby = x2 - x1, y2 - y1
    ab_len = math.sqrt(abx ** 2 + aby ** 2)

    # Project vector ac onto ab
    projection = (acx * abx + acy * aby) / (ab_len ** 2)
    closest_x = x1 + projection * abx
    closest_y = y1 + projection * aby

    # Ensure the closest point lies within the segment
    if not (0 <= projection <= 1):
        # Check distance to endpoints if projection is outside the segment
        dist1 = math.sqrt((cx - x1) ** 2 + (cy - y1) ** 2)
        dist2 = math.sqrt((cx - x2) ** 2 + (cy - y2) ** 2)
        return dist1 <= r or dist2 <= r

    # Distance from circle center to closest point
    dist_to_closest = math.sqrt((closest_x - cx) ** 2 + (closest_y - cy) ** 2)
    return dist_to_closest <= r

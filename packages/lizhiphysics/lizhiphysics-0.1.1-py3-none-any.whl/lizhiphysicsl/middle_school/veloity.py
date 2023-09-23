import math


def velocity(dis, t):
    if not isinstance(dis, (int, float)) or not isinstance(t, (int, float)):
        raise TypeError("distance and time must be numbers")
    if dis <= 0 or t <= 0:
        raise ValueError("distance and time can't be <= 0")
    else:
        a = dis / t
        return a


def distance(vel, t):
    if not isinstance(vel, (int, float)) or not isinstance(t, (int, float)):
        raise TypeError("velocity and time must be numbers")
    if vel <= 0 or t <= 0:
        raise ValueError("velocity and time can't be <= 0")
    else:
        a = vel * t
        return a


def time(vel, dis):
    if not isinstance(vel, (int, float)) or not isinstance(dis, (int, float)):
        raise TypeError("distance and velocity must be numbers")
    if vel <= 0 or dis <= 0:
        raise ValueError("distance and velocity can't be <= 0")
    else:
        a = dis / vel
        return a


def free_fall_speed(high, g=9.8):
    if not isinstance(high, (int, float)) or not isinstance(g, (int, float)):
        raise TypeError("distance and velocity must be numbers")
    if high <= 0 or g <= 0:
        raise ValueError("distance and velocity can't be <= 0")
    else:
        v = math.sqrt(2 * g * high)
        return v

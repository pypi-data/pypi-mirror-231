def pressure_force(f, a):
    """
    计算压强力的函数

    参数:
    F (float): 应用于物体上的力，单位为牛顿 (N)
    A (float): 物体的表面积，单位为平方米 (m^2)

    返回值:
    float: 压强力，单位为帕斯卡 (Pa)
    """
    return f / a


def area(frc, pre):
    return frc / pre


def force(pre, ar):
    return pre * ar


def fluid_column_pressure(h, rho, g=9.81):
    """
    计算液体柱的压强的函数

    参数:
    h (float): 液体柱的高度，单位为米 (m)
    rho (float): 液体的密度，单位为千克每立方米 (kg/m^3)
    g (float): 重力加速度，单位为米每平方秒 (m/s^2)

    返回值:
    float: 液体柱的压强，单位为帕斯卡 (Pa)
    """
    return rho * g * h


def high(pre, rho, g=9.81):
    return pre / (rho * g)


def rh(pre, h, g=9.81):
    return pre / (g * h)

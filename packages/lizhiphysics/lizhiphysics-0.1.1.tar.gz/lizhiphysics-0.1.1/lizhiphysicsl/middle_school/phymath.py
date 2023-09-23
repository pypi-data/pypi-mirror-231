import math

g = 9.81
m_e = 9.10938356e-31
m_earth = 5.9722e+24
c = 299792458
G = 6.67430e-11
μ0 = 4 * math.pi * 1e-7
ε0 = 8.854187817e-12
k_B = 1.380649e-23
e = 1.602176634e-19
h = 6.62607015e-34
h_bar = h / (2 * math.pi)
Z0 = μ0 * c
n0 = 1 / math.sqrt(ε0 * μ0)
a0 = 0.52917721e-10
R_infinity = 10973731.568160
h_c_green_photon = h * c / 540e-9
h_bar_e = h_bar / e
α = 7.2973525664e-3
k = 1 / (4 * math.pi * ε0)
v_s_air = 331.3 + 0.606 * 20
ε_air = 1.00058986
n_air = math.sqrt(1 + ε_air)
Thermal_conductivity = 0.0263
M = 28.0134e-3
r_e = e ** 2 / (4 * math.pi * ε0 * m_e * c ** 2)
Na = 6.02214076e23
A = 4 * math.pi * n0 * r_e ** 2 / 3
B = 4 * math.pi * Z0 / c
K = G * m_earth
T0 = 273.15
A_J = 7.2973525693e-3


def cube_volume(a):
    return a ** 3


def rectangular_volume(a, b, c1):
    return a * b * c1


def cylinder_volume(r, high):
    return math.pi * r ** 2 * high


def cone_volume(r, high):
    return 1 / 3 * math.pi * r ** 2 * high


def sphere_volume(r):
    return 4 / 3 * math.pi * r ** 3


def ellipsoid_volume(a, b, c1):
    return 4 / 3 * math.pi * a * b * c1


def icosahedron_volume(a):
    return 5 / 12 * (3 + math.sqrt(5)) * a ** 3


def trisoctahedron_volume(a):
    return 2 * (3 + math.sqrt(5)) * a ** 3


def square_pyramid_volume(a, high):
    return 1 / 3 * a ** 2 * high


def hexahedron_volume(a):
    return a ** 3 * math.sqrt(2)


def octahedron_volume(a):
    return 1 / 3 * math.sqrt(2) * a ** 3


def dodecahedron_volume(a):
    return (15 + 7 * math.sqrt(5)) / 4 * a ** 3


def tetrahedron_volume(a):
    return (a ** 3) / (6 * math.sqrt(2))


def prism_volume(a, b, high):
    return 1 / 2 * a * b * high


def pyramid_volume(b, high):
    return 1 / 3 * b ** 2 * high


def rotated_surface_volume(r, high):
    return 1 / 2 * math.pi * r ** 2 * high


def arch_volume(w, high, r):
    return (w * high * (2 * r - high)) / 6


def buoy_volume(d, high):
    return 1 / 3 * math.pi * (d / 2) ** 2 * high


def strokerow_volume(l1, w, high):
    return l1 * w * high * 0.5


def torus_volume(r1, r2):
    return 2 * math.pi ** 2 * r1 ** 2 * r2


def tire_volume(d, w):
    return math.pi * (d / 2) ** 2 * w


def helix_volume(r, high):
    return math.pi * r ** 2 * high


def bilatin_cube_volume(a):
    return 6 * a ** 3


def portal_volume(high, a):
    return 4 * high ** 3 + 20 * a ** 3


def triacontahedron_volume(high, r):
    return 32 / 9 * high ** 2 * r ** 3 * math.sqrt(3)


def tetracontahedron_volume(a, high):
    return 1 / 18 * (80 + 30 * math.sqrt(6)) * a ** 3 + 2 * high ** 3


def battleboat_volume(w, l1, high):
    return w * l1 * high / 2


def pleated_skirt_volume(w, high, d):
    return w * high * d / 2


def hanging_chain_sphere_volume(r, a):
    return (4 / 3) * math.pi * r ** 3 - math.pi * a ** 2 * (r - a / 3)


def rect_area(length, width):
    return length * width


def square_area(side):
    return side ** 2


def circle_area(radius):
    return math.pi * radius ** 2


def trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2


def triangle_area_sides(a, b, c1):
    s = (a + b + c1) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c1))


def pentagon_area(side):
    return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side ** 2


def hexagon_area(side):
    return 3 * math.sqrt(3) / 2 * side ** 2


def regular_polygon_area(n, side):
    return 0.25 * n * side ** 2 * 1 / math.tan(math.pi / n)


def ellipse_area(a, b):
    return math.pi * a * b


def triangle_area_heron(a, b, c1):
    s = (a + b + c1) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c1))


def trapezoid_area_diagonal(d1, d2):
    return 0.5 * d1 * d2


def rect_area_diagonal(d1, d2):
    return 0.5 * d1 * d2


def pyramid_area(l1, high):
    return l1 * math.sqrt(l1**2 / 4 + high**2)


def octahedron_area(a):
    return 2 * math.sqrt(3) * a ** 2


def dodecahedron_area(a):
    return 3 * math.sqrt(25 + 10 * math.sqrt(5)) * a ** 2


def icosahedron_area(a):
    return 5 * math.sqrt(3) * a ** 2


def sector_area(radius, angle):
    return math.pi * radius ** 2 * angle / 360


def triangle_area_2sas(s1, s2, theta):
    return 0.5 * s1 * s2 * math.sin(theta)


def triangle_area_bh(b, high):
    return 0.5 * b * high


def tetrahedron_area(a):
    return math.sqrt(3) * a ** 2


def spherical_cap_area(radius, high):
    return 2 * math.pi * radius * high


def rect_area_diagonal_and_width(d, w):
    l1 = math.sqrt(d ** 2 - w ** 2)
    return l1 * w


def annulus_area(r1, r2):
    outer_area = math.pi * r1**2
    inner_area = math.pi * r2**2
    return outer_area - inner_area


def annulus_area_width(radius, w):
    r1 = radius + w
    r2 = radius - w
    return annulus_area(r1, r2)


def sphere_area(radius):
    return 4 * math.pi * radius ** 2


def cylinder_lateral_area(radius, height):
    return 2 * math.pi * radius * height


def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def count_prime_factors(numbers):
    prime_count = {}
    for num in numbers:
        factors = prime_factors(num)
        for factor in factors:
            if factor in prime_count:
                prime_count[factor] += 1
            else:
                prime_count[factor] = 1
    return prime_count


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def filter_double_prime(result):
    filtered_result = {}
    for key, value in result.items():
        if value % 2 == 0 and is_prime(key):
            filtered_result[key] = value
    return filtered_result


def filter_double_prime2(result):
    filtered_result2 = {}
    for key, value in result.items():
        if value % 2 == 1 and is_prime(key):
            filtered_result2[key] = value
    return filtered_result2


def count_prime_numbers(filtered_result):
    prime_numbers_product = 1
    for prime in filtered_result:
        count = filtered_result[prime]
        prime_numbers_product *= prime ** count
    return prime_numbers_product


def count_prime_numbers2(filtered_result):
    prime_numbers_product = 1
    for prime in filtered_result:
        count = filtered_result[prime]
        prime_numbers_product *= prime ** (count - 1)
    return prime_numbers_product


def count_prime_numbers3(filtered_result):
    prime_numbers_product = 1
    for prime in filtered_result:
        prime_numbers_product *= prime ** 1
    return prime_numbers_product


def decrease_prime_count(filtered_result):
    for prime in filtered_result:
        filtered_result[prime] -= 1
    return filtered_result


def gcd(numbers):
    if len(numbers) < 2:
        raise NameError("请提供至少两个数字")

    def find_gcd(a, b):
        if b == 0:
            return a
        return find_gcd(b, a % b)

    gcd_result = numbers[0]

    for i in range(1, len(numbers)):
        gcd_result = find_gcd(gcd_result, numbers[i])

    return gcd_result


def open_squared_operation(number):
    for num in number:
        if num < 0:
            raise TypeError("Only non-negative numbers can be squared")
        elif isinstance(math.sqrt(num), int):
            return str(math.sqrt(num))
        elif isinstance(num, int):
            result = count_prime_factors(number)
            filtered_result = filter_double_prime(result)
            filtered_result2 = filter_double_prime2(result)
            a = count_prime_numbers(filtered_result)
            b = count_prime_numbers2(filtered_result2)
            c = count_prime_numbers3(filtered_result2)
            if c == 1:
                aa = str(math.sqrt(a) * math.sqrt(b))
                return aa
            else:
                if math.sqrt(a) * math.sqrt(b) == 1:
                    aa = str("√" + str(c))
                    return aa
                else:
                    aa = str(str(math.sqrt(a) * math.sqrt(b)) + "√" + str(c))
                    return aa
        elif isinstance(num, float):
            decimal_length = len(str(num).split('.')[1])
            if decimal_length % 2 == 1:
                aa = (num * (10**(decimal_length + 1))) // 1
                result = count_prime_factors([aa])
                filtered_result = filter_double_prime(result)
                filtered_result2 = filter_double_prime2(result)
                a = count_prime_numbers(filtered_result)
                b = count_prime_numbers2(filtered_result2)
                c = count_prime_numbers3(filtered_result2)
                number2 = [math.sqrt(a) * math.sqrt(b), math.sqrt(10**(decimal_length + 1))]
                d = gcd(number2)
                if (math.sqrt(a) * math.sqrt(b)) / d == 1.0:
                    aa = str("√" + str(c) + "/" + str(math.sqrt(10 ** (decimal_length + 1)) / d))
                    return aa
                elif (math.sqrt(a) * math.sqrt(b)) / d == 1.0 and math.sqrt(10 ** (decimal_length + 1)) / d == 1:
                    aa = str("√" + str(c))
                    return aa
                else:
                    aa1 = str(str((math.sqrt(a) * math.sqrt(b))/d) + "√" + str(c) + "/")
                    bb = str(math.sqrt(10**(decimal_length + 1)) / d)
                    aa = str(aa1 + bb)
                    return aa
            elif decimal_length % 2 == 0:
                aa = num * (10**decimal_length)
                result = count_prime_factors([aa])
                filtered_result = filter_double_prime(result)
                filtered_result2 = filter_double_prime2(result)
                a = count_prime_numbers(filtered_result)
                b = count_prime_numbers2(filtered_result2)
                c = count_prime_numbers3(filtered_result2)
                number2 = [math.sqrt(a) * math.sqrt(b), math.sqrt(10 ** decimal_length)]
                d = gcd(number2)
                if (math.sqrt(a) * math.sqrt(b)) / d == 1:
                    aa = str("√" + str(c) + "/" + str(math.sqrt(10 ** decimal_length) / d))
                    return aa
                if math.sqrt(10 ** decimal_length) / d == 1:
                    aa = str("√" + str(c))
                    return aa
                else:
                    aa1 = str(str((math.sqrt(a) * math.sqrt(b)) / d) + "√" + str(c))
                    bb = str("/" + str(math.sqrt(10 ** decimal_length) / d))
                    aa = str(aa1 + bb)
                    return aa


def open_squared_operation_fraction(molecule_number, denominator_number):  # 分子，分母
    if isinstance(molecule_number / denominator_number, int):
        num = molecule_number / denominator_number
        return open_squared_operation([num])
    else:
        n = [molecule_number, denominator_number]
        a = gcd(n)
        if molecule_number / a == 1 and denominator_number / a == 1:
            return str(1)
        else:
            number = [molecule_number * denominator_number]
            for num in number:
                if num < 0:
                    raise TypeError("Only non-negative numbers can be squared")
            result = count_prime_factors(number)
            filtered_result = filter_double_prime(result)
            filtered_result2 = filter_double_prime2(result)
            a = count_prime_numbers(filtered_result)
            b = count_prime_numbers2(filtered_result2)
            c = count_prime_numbers3(filtered_result2)
            if c == 1:
                return str(math.sqrt(a) * math.sqrt(b))
            else:
                numbers2 = [math.sqrt(a) * math.sqrt(b), denominator_number]
                a2 = gcd(numbers2)
                if math.sqrt(a) * math.sqrt(b) / a2 == 1 or math.sqrt(a) * math.sqrt(b) / a2 == -1:
                    if denominator_number / a2 == 1:
                        aa = str("√" + str(c))
                        return aa
                    else:
                        aa = str("√" + str(c) + "/" + str(denominator_number / a2))
                        return aa
                elif denominator_number / a2 == 1:
                    aa = str("√" + str(c))
                    return aa
                else:
                    aa = str(str(math.sqrt(a) * math.sqrt(b) / a2) + "√" + str(c) + "/" + str(denominator_number / a2))
                    return aa

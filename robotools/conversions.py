import math


def deg_to_rad(degrees: float) -> float:
    return degrees * math.pi / 180


def rpm_to_rad_s(rpm: float) -> float:
    return rpm * 2 * math.pi / 60


def vector_magnitude(*components: float) -> float:
    return math.sqrt(sum(c ** 2 for c in components))
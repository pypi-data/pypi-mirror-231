from vecked.logging import logger


def inverse_lerp(
    a: float,
    b: float,
    v: float,
) -> float:
    """
    Gets the normalised distance of :code:`v` from :code:`a` in the direction of
    :code:`b`.
    """

    return (v - a) / (b - a)


def lerp(
    a: float,
    b: float,
    t: float,
) -> float:
    """
    Gets the value :code:`t` distance from :code:`a` in the direction of
    :code:`b`.
    """

    result = a + t * (b - a)

    logger.debug("%f is lerp %f between %f and %f", t, result, a, b)

    return result

from __future__ import annotations

from vecked.logging import logger
from vecked.numbers import inverse_lerp, lerp
from vecked.vector2.vector2 import Vector2


class Vector2f(Vector2[float]):
    """
    A two-dimensional floating-point vector.
    """

    def __add__(self, other: object) -> Vector2f:
        if isinstance(other, Vector2):
            return self.add_vector2(other)

        raise ValueError("cannot add %s to %s" % (repr(other), repr(self)))

    def __mul__(self, other: object) -> Vector2f:
        if isinstance(other, float | int):
            return self.multiply_length(other)

        if isinstance(other, Vector2):
            return self.multiply_vector2(other)

        raise ValueError("cannot multiply %s by %s" % (repr(self), repr(other)))

    def __sub__(self, other: object) -> Vector2f:
        if isinstance(other, Vector2):
            return self.subtract_vector2(other)

        raise ValueError("cannot subtract %s from %s" % (repr(other), repr(self)))

    def add_vector2(self, length: Vector2[float | int]) -> Vector2f:
        """
        Returns the addition of this vector to another.
        """

        return self.__class__(
            self._x + length.x,
            self._y + length.y,
        )

    def inverse_lerp(self, a: Vector2f, b: Vector2f) -> Vector2f:
        """
        Gets the normalised distance of this vector from :code:`a` in the
        direction of :code:`b`.
        """

        result = Vector2f(
            inverse_lerp(a.x, b.x, self._x),
            inverse_lerp(a.y, b.y, self._y),
        )

        logger.debug(
            "%s is inverse lerp %s between %s and %s",
            self,
            result,
            a,
            b,
        )

        return result

    def lerp(self, a: Vector2f, b: Vector2f) -> Vector2f:
        """
        Gets the value this normalised vector's distance between :code:`a`
        towards :code:`b`.
        """

        result = Vector2f(
            lerp(a.x, b.x, self._x),
            lerp(a.y, b.y, self._y),
        )

        logger.debug(
            "%s is lerp %s between %s and %s",
            self,
            result,
            a,
            b,
        )

        return result

    def multiply_length(self, length: float | int) -> Vector2f:
        """
        Returns the multiplication of this vector by a length in both
        dimensions.
        """

        return self.__class__(
            self._x * length,
            self._y * length,
        )

    def multiply_vector2(self, length: Vector2[float | int]) -> Vector2f:
        """
        Returns the multiplication of this vector by another.
        """

        return self.__class__(
            self._x * length.x,
            self._y * length.y,
        )

    def subtract_vector2(self, length: Vector2[float | int]) -> Vector2f:
        """
        Returns the subtraction of a two-dimensional vector from this.
        """

        return Vector2f(
            self._x - length.x,
            self._y - length.y,
        )

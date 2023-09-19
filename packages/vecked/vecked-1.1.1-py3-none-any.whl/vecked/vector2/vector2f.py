from __future__ import annotations

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

    def add_vector2(self, length: Vector2[float | int]) -> Vector2f:
        """
        Returns the addition of this vector to another.
        """

        return self.__class__(
            self._x + length.x,
            self._y + length.y,
        )

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

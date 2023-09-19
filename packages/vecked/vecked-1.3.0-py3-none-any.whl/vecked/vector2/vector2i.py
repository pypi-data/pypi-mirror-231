from __future__ import annotations

from typing import overload

from vecked.vector2.vector2 import Vector2
from vecked.vector2.vector2f import Vector2f


class Vector2i(Vector2[int]):
    @overload
    def __add__(self, other: Vector2[float]) -> Vector2f:
        ...  # pragma: no cover

    @overload
    def __add__(self, other: Vector2[int]) -> Vector2i:
        ...  # pragma: no cover

    def __add__(self, other: object) -> Vector2i | Vector2f:
        if isinstance(other, Vector2):
            if isinstance(other.x, int):
                return self.add_vector2i(other)

            return self.add_vector2f(other)

        raise ValueError("cannot add %s to %s" % (repr(other), repr(self)))

    @overload
    def __sub__(self, other: Vector2[float]) -> Vector2f:
        ...  # pragma: no cover

    @overload
    def __sub__(self, other: Vector2[int]) -> Vector2i:
        ...  # pragma: no cover

    def __sub__(self, other: object) -> Vector2i | Vector2f:
        if isinstance(other, Vector2):
            if isinstance(other.x, int):
                return self.subtract_vector2i(other)

            return self.subtract_vector2f(other)

        raise ValueError("cannot subtract %s from %s" % (repr(other), repr(self)))

    @overload
    def __mul__(self, other: int | Vector2[int]) -> Vector2i:
        ...  # pragma: no cover

    @overload
    def __mul__(self, other: float | Vector2[float]) -> Vector2f:
        ...  # pragma: no cover

    def __mul__(self, other: object) -> Vector2i | Vector2f:
        if isinstance(other, int):
            return self.multiply_int(other)

        if isinstance(other, float):
            return self.multiply_float(other)

        if isinstance(other, Vector2):
            if isinstance(other.x, int):
                return self.multiply_vector2i(other)

            return self.multiple_vector2f(other)

        raise ValueError("cannot multiply %s by %s" % (repr(self), repr(other)))

    def add_vector2f(self, length: Vector2[float]) -> Vector2f:
        """
        Returns the addition of this vector to another.
        """

        return Vector2f(
            self._x + length.x,
            self._y + length.y,
        )

    def add_vector2i(self, length: Vector2[int]) -> Vector2i:
        """
        Returns the addition of this vector to another.
        """

        return self.__class__(
            self._x + length.x,
            self._y + length.y,
        )

    def subtract_vector2f(self, length: Vector2[float]) -> Vector2f:
        """
        Returns the subtraction of a floating-point two-dimensional vector from
        this.
        """

        return Vector2f(
            self._x - length.x,
            self._y - length.y,
        )

    def subtract_vector2i(self, length: Vector2[int]) -> Vector2i:
        """
        Returns the subtraction of an integer two-dimensional vector from this.
        """

        return self.__class__(
            self._x - length.x,
            self._y - length.y,
        )

    def multiply_float(self, length: float) -> Vector2f:
        """
        Returns the multiplication of this vector by a floating-point length in
        both dimensions.
        """

        return Vector2f(self._x * length, self._y * length)

    def multiply_int(self, length: int) -> Vector2i:
        """
        Returns the multiplication of this vector by an integer length in both
        dimensions.
        """

        return self.__class__(self._x * length, self._y * length)

    def multiple_vector2f(self, length: Vector2[float]) -> Vector2f:
        """
        Returns the multiplication of this vector by a floating-point
        two-dimensional vector.
        """

        return Vector2f(self._x * length.x, self._y * length.y)

    def multiply_vector2i(self, length: Vector2[int]) -> Vector2i:
        """
        Returns the multiplication of this vector by an integer two-dimensional
        vector.
        """

        return self.__class__(self._x * length.x, self._y * length.y)

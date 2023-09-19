from __future__ import annotations

from abc import ABC
from typing import Generic, cast

from vecked.types import TNumeric


class Vector2(ABC, Generic[TNumeric]):
    """
    A two-dimensional vector.

    .. testcode::

        from vecked import Vector2

        v = Vector2(3, 9)

        print(f"x = {v.x}")
        print(f"y = {v.y}")

    .. testoutput::
       :options: +NORMALIZE_WHITESPACE

       x = 3
       y = 9
    """

    def __init__(
        self,
        x: TNumeric,
        y: TNumeric,
    ) -> None:
        self._x: TNumeric = x
        self._y: TNumeric = y

    def __abs__(self) -> Vector2[TNumeric]:
        return self.__class__(
            cast(TNumeric, abs(self._x)),
            cast(TNumeric, abs(self._y)),
        )

    def __eq__(self, other: object) -> bool:
        if other is None:
            return False

        if isinstance(other, Vector2):
            return self.vector == other.vector

        return self.vector == other

    def __repr__(self) -> str:
        return "%s%s" % (self.__class__.__name__, str(self))

    def __str__(self) -> str:
        return str(self.vector)

    @property
    def vector(self) -> tuple[TNumeric, TNumeric]:
        """
        Tuple of lengths.

        .. testcode::

            from vecked import Vector2

            v = Vector2(3, 9)

            print(f"vector = {v.vector}")

        .. testoutput::
            :options: +NORMALIZE_WHITESPACE

            vector = (3, 9)
        """

        return (self._x, self._y)

    @property
    def x(self) -> TNumeric:
        """
        X length.

        .. testcode::

            from vecked import Vector2

            v = Vector2(3, 9)

            print(f"x = {v.x}")

        .. testoutput::
            :options: +NORMALIZE_WHITESPACE

            x = 3
        """

        return self._x

    @property
    def y(self) -> TNumeric:
        """
        Y length.

        .. testcode::

            from vecked import Vector2

            v = Vector2(3, 9)

            print(f"y = {v.y}")

        .. testoutput::
            :options: +NORMALIZE_WHITESPACE

            y = 9
        """

        return self._y

    def reflect_across(self, origin: Vector2[TNumeric]) -> Vector2[TNumeric]:
        """
        Reflects this vector across another in both dimensions.
        """

        return self.__class__(
            origin.x - (self._x - origin.x),  # type: ignore
            origin.y - (self._y - origin.y),  # type: ignore
        )

    def reflect_horizontally(self, x: TNumeric) -> Vector2[TNumeric]:
        """
        Reflects this vector across a vertical mirror.
        """

        return self.__class__(
            x - (self._x - x),  # type: ignore
            self._y,
        )

    def reflect_vertically(self, y: TNumeric) -> Vector2[TNumeric]:
        """
        Reflects this vector across a horizontal mirror.
        """

        return self.__class__(
            self._x,
            y - (self._y - y),  # type: ignore
        )

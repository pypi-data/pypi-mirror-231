from __future__ import annotations

from abc import ABC
from typing import Generic

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

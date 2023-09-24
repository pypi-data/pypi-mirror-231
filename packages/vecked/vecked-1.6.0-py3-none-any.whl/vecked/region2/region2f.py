from __future__ import annotations

from vecked.vector2 import Vector2f


class Region2f:
    """
    A two-dimensional region described by floating-point position and size.
    """

    def __init__(self, position: Vector2f, size: Vector2f) -> None:
        self._position = position
        self._size = size

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Region2f)
            and other._position == self._position
            and other._size == self._size
        )

    def __repr__(self) -> str:
        return "%sx%s" % (self._position, self._size)

    def accommodate(self, point: Vector2f) -> Region2f:
        """
        Returns a copy of this region expanded to accommodate :code:`point`.
        """

        position_delta = (point - self._position).clamp(minimum=0)
        size_delta = (point - (self._position + self._size)).clamp(maximum=0)

        return self.translate(
            position_delta,
        ).expand(
            (position_delta * -1) + size_delta,
        )

    def expand(self, length: Vector2f) -> Region2f:
        """
        Returns a copy of this region with each length increased by
        :code:`length`.
        """

        return Region2f(
            self._position,
            self._size + length,
        )

    def interpolate(self, position: Vector2f, into: Region2f) -> Vector2f:
        """
        Interpolates :code:`position` within this region into `into`.

        .. testcode::

            from vecked import Region2f, Vector2f

            region = Region2f(
                Vector2f(1, 1),
                Vector2f(3, 3),
            )

            interpolated = region.interpolate(
                Vector2f(2.5, 2.5),
                Region2f(
                    Vector2f(10, 10),
                    Vector2f(20, 22),
                ),
            )

            print(f"interpolated = {interpolated}")

        .. testoutput::
            :options: +NORMALIZE_WHITESPACE

            interpolated = (20.0, 21.0)
        """

        return position.inverse_lerp(
            self._position,
            self._position + self._size,
        ).lerp(
            into._position,
            into._position + into._size,
        )

    def reflect_vertically(self, y: float = 0) -> Region2f:
        """
        Reflects this region across a horizontal mirror.
        """

        return self.__class__(
            self._position.reflect_vertically(y),
            Vector2f(self._size.x, -self._size.y),
        )

    def translate(self, distance: Vector2f) -> Region2f:
        """
        Returns a copy of this region translated by :code:`distance`.
        """

        return Region2f(
            self._position + distance,
            self._size,
        )

    def upside_down(self) -> Region2f:
        """
        Turns this region upside-down.
        """

        return self.reflect_vertically(self._position.y + (self._size.y / 2))

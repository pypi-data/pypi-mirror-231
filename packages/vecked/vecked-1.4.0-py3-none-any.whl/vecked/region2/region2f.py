from __future__ import annotations

from vecked.vector2 import Vector2f


class Region2f:
    """
    A two-dimensional region described by floating-point position and size.
    """

    def __init__(self, position: Vector2f, size: Vector2f) -> None:
        self._position = position
        self._size = size

    def __str__(self) -> str:
        return "%sx%s" % (self._position, self._size)

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
                Vector2f(2, 2),
                Region2f(
                    Vector2f(10, 10),
                    Vector2f(20, 22),
                ),
            )

            print(f"interpolated = {interpolated}")

        .. testoutput::
            :options: +NORMALIZE_WHITESPACE

            interpolated = (15.0, 16.0)
        """

        return position.inverse_lerp(
            self._position,
            self._size,
        ).lerp(
            into._position,
            into._size,
        )

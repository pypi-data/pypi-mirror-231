from __future__ import annotations

from typing import Generic

from bendy import CubicBezier
from vecked import Vector2f

from twixt.types import TKey


class Track(Generic[TKey]):
    def __init__(
        self,
        key: TKey,
        start: int = 0,
        value: float = 0.0,
        ease_in_length: float = 0.0,
        ease_in_force: float = 0.0,
    ) -> None:
        self._anchor = Vector2f(start, value)
        self._control = self._anchor + Vector2f(ease_in_length, ease_in_force)
        self._curves: list[CubicBezier] = []
        self._ease_in_force = ease_in_force
        self._ease_in_length = ease_in_length
        self._key = key
        self._max_anchor = max(self._anchor.y, self._control.y)
        self._min_anchor = min(self._anchor.y, self._control.y)

    def add_point(
        self,
        frame: int,
        value: float,
        ease_out_length: float = 0.0,
        ease_out_force: float = 0.0,
    ) -> Track[TKey]:
        anchor = Vector2f(frame, value)
        control = anchor - Vector2f(ease_out_length, ease_out_force)

        self._max_anchor = max(self._max_anchor, anchor.y, control.y)
        self._min_anchor = min(self._min_anchor, anchor.y, control.y)

        if self._curves:
            last_curve = self._curves[len(self._curves) - 1]
            new_curve = last_curve.join(control, anchor)
        else:
            new_curve = CubicBezier(
                self._anchor,
                self._control,
                control,
                anchor,
            )

        self._curves.append(new_curve)
        return self

    @property
    def key(self) -> TKey:
        """
        Track key.
        """

        return self._key

    @property
    def max_anchor(self) -> float:
        """
        Maximum curve anchor.
        """

        return self._max_anchor

    @property
    def min_anchor(self) -> float:
        """
        Minimum curve anchor.
        """

        return self._min_anchor

    def step(self, frame: int) -> float:
        if not self._curves:
            return self._anchor.y

        first_curve = self._curves[0]

        if frame <= first_curve.a0.x:
            return first_curve.a0.y

        for curve in self._curves:
            if frame >= curve.a0.x and frame < curve.a3.x:
                return next(curve.estimate_y(frame))

        final_curve = self._curves[len(self._curves) - 1]
        return final_curve.a3.y

from __future__ import annotations

from typing import Generic

from bendy import CubicBezier
from vecked import Vector2f

from twixt.types import TKey


class Track(Generic[TKey]):
    def __init__(
        self,
        key: TKey,
        length: int,
        start: int = 0,
        value: float = 0.0,
        ease_in_length: float = 0.0,
        ease_in_force: float = 0.0,
    ) -> None:
        self._length = length
        self._key = key
        self._start = start
        self._initial_value = value
        self._ease_in_length = ease_in_length
        self._ease_in_force = ease_in_force
        self._curves: list[CubicBezier] = []

    @property
    def key(self) -> TKey:
        return self._key

    def add_point(
        self,
        frame: int,
        value: float,
        ease_out_length: float = 0.0,
        ease_out_force: float = 0.0,
    ) -> Track[TKey]:
        control = Vector2f(frame - ease_out_length, value - ease_out_force)
        anchor = Vector2f(frame, value)

        if self._curves:
            last_curve = self._curves[len(self._curves) - 1]
            new_curve = last_curve.join(control, anchor)
        else:
            new_curve = CubicBezier(
                (self._start, self._initial_value),
                (
                    self._start + self._ease_in_length,
                    self._initial_value + self._ease_in_force,
                ),
                control,
                anchor,
            )

        self._curves.append(new_curve)
        return self

    def step(self, frame: int) -> float:
        if not self._curves:
            return self._initial_value

        first_curve = self._curves[0]

        if frame <= first_curve.a0.x:
            return first_curve.a0.y

        for curve in self._curves:
            if frame >= curve.a0.x and frame < curve.a3.x:
                return next(curve.estimate_y(frame))

        final_curve = self._curves[len(self._curves) - 1]
        return final_curve.a3.y

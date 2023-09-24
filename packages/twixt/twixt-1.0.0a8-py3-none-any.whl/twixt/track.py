from __future__ import annotations

from typing import Any, Generic

from bendy import CompositeCubicBezier, CubicBezier
from vecked import Region2f, Vector2f

from twixt.logging import logger
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
        self._curves: CompositeCubicBezier | None = None
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
            self._curves.append(control, anchor)
        else:
            new_curve = CubicBezier(
                self._anchor,
                self._control,
                control,
                anchor,
            )
            self._curves = CompositeCubicBezier(new_curve)

        return self

    def draw(
        self,
        image_draw: Any,
        bounds: Region2f,
        resolution: int = 100,
    ) -> None:
        try:
            from PIL.ImageDraw import ImageDraw
        except ImportError:  # pragma: no cover
            msg = "Install `twixt[draw]` to enable drawing."  # pragma: no cover
            logger.error(msg)  # pragma: no cover
            raise  # pragma: no cover

        if not isinstance(image_draw, ImageDraw):
            raise TypeError("image_draw is not PIL.ImageDraw")

        if not self._curves:
            raise ValueError("Cannot render an incomplete track")

        self._curves.draw(
            image_draw,
            bounds,
            axis=True,
            resolution=resolution,
            title=str(self._key),
        )

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

        if frame <= self._curves.head.a0.x:
            return self._curves.head.a0.y

        if frame >= self._curves.tail.a3.x:
            return self._curves.tail.a3.y

        return next(self._curves.estimate_y(frame))

from pathlib import Path
from typing import Generic, Iterator

from vecked import Region2f, Vector2f

from twixt.composed_step import ComposedStep
from twixt.logging import logger
from twixt.track import Track
from twixt.types import TKey


class Timeline(Generic[TKey]):
    def __init__(
        self,
        frames: int,
    ) -> None:
        self._frames = frames
        self._tracks: list[Track[TKey]] = []

    def add_track(
        self,
        key: TKey,
        start_frame: int = 0,
        start_value: float = 0.0,
        ease_in_length: int = 0,
        ease_in_force: float = 0.0,
    ) -> Track[TKey]:
        track = Track[TKey](
            key,
            start_frame,
            start_value,
            ease_in_length,
            ease_in_force,
        )

        self._tracks.append(track)

        return track

    def export(
        self,
        path: Path,
        width: int,
        track_height: int,
        resolution: int = 100,
    ) -> None:
        try:
            from PIL import Image, ImageDraw
        except ImportError:  # pragma: no cover
            msg = "Install `bendy[draw]` to enable drawing."  # pragma: no cover
            logger.error(msg)  # pragma: no cover
            raise  # pragma: no cover

        margin = 50

        image_height = ((track_height + margin) * len(self._tracks)) + margin

        image = Image.new(
            "RGB",
            (width, image_height),
            (255, 255, 255),
        )

        draw = ImageDraw.Draw(image)

        position = Vector2f(margin, margin)

        track_size = Vector2f(
            width - (margin * 2),
            track_height,
        )

        # Flip upside-down so (0, 0) is at the bottom.
        bounds = Region2f(position, track_size).upside_down()

        for track in self._tracks:
            track.draw(
                draw,
                bounds,
                resolution=resolution,
            )

            bounds = bounds.translate(Vector2f(0, margin + track_height))

        image.save(path)

    @property
    def frames(self) -> int:
        """
        Frame count.
        """

        return self._frames

    @property
    def steps(self) -> Iterator[ComposedStep[TKey]]:
        for frame in range(self._frames):
            progress: dict[TKey, float] = {}

            for track in self._tracks:
                progress[track.key] = track.step(frame)

            yield ComposedStep(
                frame=frame,
                progress=progress,
            )

from typing import Generic, Iterator

from twixt.composed_step import ComposedStep
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
            self._frames,
            start_frame,
            start_value,
            ease_in_length,
            ease_in_force,
        )

        self._tracks.append(track)

        return track

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

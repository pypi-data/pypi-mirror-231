from .disaster import Disaster
from .finishing_position import FinishingPosition
from .outcome import Outcome


class RacePerformance:
    """
    A class for grouping together race performance stats into a single object.

    """

    def __init__(
        self,
        outcome: str | int | Disaster | FinishingPosition | Outcome,
        *,
        official_position: str | int | FinishingPosition | None = None,
        comments: str | None = None,
    ):
        """
        Initialize a RacePerformance instance.

        Args:
            outcome: A disaster or finishing position
            official_position: The official finishing position
            comments: Race comments on this performance

        Raises:
            ValueError: If both a disaster and a finishing position are given

        """
        self.comments = comments
        self.outcome = Outcome(outcome) if not isinstance(outcome, Outcome) else outcome
        self.official_position = (
            Outcome(official_position)
            if official_position
            else self.outcome
            if isinstance(self.outcome._value, FinishingPosition)
            else None
        )

        if isinstance(self.outcome._value, Disaster) and self.official_position:
            raise ValueError(
                f"Cannot have both a disaster {self.outcome} and a position {self.official_position}"
            )

    def __repr__(self):
        official_position_repr = (
            f", placed {int(self.official_position._value)}"
            if self.official_position and self.official_position != self.outcome
            else ""
        )
        return f"<RacePerformance: {int(self.outcome._value) if isinstance(self.outcome._value, FinishingPosition) else str(self.outcome._value)}{official_position_repr}>"

    def __str__(self):
        official_position_str = (
            f", placed {self.official_position}"
            if self.official_position and self.official_position != self.outcome
            else ""
        )
        return f"{self.outcome}{official_position_str}"

import re
from .racing_code import RacingCode


class RaceGrade:
    REGEX = r"G(?:roup|rade|)\s*"

    def __init__(self, grade: str | int | None, racing_code: RacingCode = None):
        grade_value = re.sub(RaceGrade.REGEX, "", str(grade or "").title())

        if grade_value.isdigit():
            if not 1 <= int(grade_value) < 4:
                raise ValueError(f"Grade must be between 1 and 3, not {grade}")
        elif grade_value and grade_value != "Listed":
            raise ValueError(f"Grade must be a number or 'Listed', not {grade}")

        code_from_grade = {
            "grade": RacingCode.NATIONAL_HUNT,
            "group": RacingCode.FLAT,
            "default": None,
        }[next((x for x in ["grade", "group"] if x in str(grade).lower()), "default")]

        if code_from_grade and racing_code and code_from_grade != racing_code:
            raise ValueError(
                f"{grade} conflicts with value for racing code: {racing_code.value}"
            )

        self.value = int(grade_value) if grade_value.isdigit() else grade_value
        self.racing_code = code_from_grade or racing_code or RacingCode.FLAT

    def __repr__(self):
        return f"<RaceGrade: {self.value}>"

    def __str__(self):
        if not self.value:
            return ""

        title = "Grade" if self.racing_code == RacingCode.NATIONAL_HUNT else "Group"
        return "Listed" if not str(self.value).isdigit() else f"{title} {self.value}"

    def __bool__(self):
        return bool(self.value)

    def __eq__(self, other):
        if isinstance(other, RaceGrade):
            return self.value == other.value

        if isinstance(other, int):
            return self.value != "Listed" and self.value == other

        return False

    def __lt__(self, other):
        if not self.value:
            return other.value

        if not str(self.value).isdigit():
            return str(other.value).isdigit()

        return str(other.value).isdigit() and self.value > other.value

    def __gt__(self, other):
        if not self.value:
            return False

        return str(self.value).isdigit() and (
            not other.value
            or not str(other.value).isdigit()
            or self.value < other.value
        )

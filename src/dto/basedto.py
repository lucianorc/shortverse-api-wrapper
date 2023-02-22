from datetime import datetime


class BaseDTO:
    def __format_date_by_string(self, date: str) -> datetime | None:
        if date != "None":
            return datetime.strptime(str(date), "%Y-%m-%dT%H:%M:%S.%fZ")

        return None

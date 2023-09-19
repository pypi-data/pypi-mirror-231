from abc import ABC


class Scheduler(ABC):
    def __init__(
        self,
        pl_id=None,
        project_id=None,
        owner_id=None,
        input_parameters=None,
        start_date=None,
        frequency="W-MON",
        start_delay=None,
    ):
        self.pl_id = pl_id
        self.project_id = project_id
        self.owner_id = owner_id
        self.input_parameters = input_parameters
        self.start_date = start_date
        self.frequency = frequency
        self.start_delay = start_delay

    def is_valid(self):
        access_fields = []

        if self.pl_id is not None:
            access_fields.append(self.pl_id)

        if self.project_id is not None:
            access_fields.append(self.project_id)

        if self.owner_id is not None:
            access_fields.append(self.owner_id)

        if (
            self.start_date is not None
            and self.frequency is not None
            and len(access_fields) == 1
        ):
            return True

        return False

    def to_dict(self):
        return {
            "pl_id": self.pl_id,
            "project_id": self.project_id,
            "owner_id": self.owner_id,
            "input_parameters": self.input_parameters,
            "start_date": self.start_date,
            "frequency": self.frequency,
            "start_delay": self.start_delay,
        }

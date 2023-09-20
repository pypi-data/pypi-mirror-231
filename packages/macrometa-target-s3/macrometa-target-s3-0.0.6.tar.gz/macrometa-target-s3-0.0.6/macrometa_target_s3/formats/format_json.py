from decimal import Decimal
from json import dumps, JSONEncoder
from datetime import datetime

from bson import ObjectId

from macrometa_target_s3.formats.format_base import FormatBase


class JsonSerialize(JSONEncoder):
    def default(self, obj: any) -> any:
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        else:
            raise TypeError(f"Type {type(obj)} not serializable")


class FormatJson(FormatBase):
    def __init__(self, config, context) -> None:
        super().__init__(config, context, "json")
        pass

    def _prepare_records(self):
        # use default behavior, no additional prep needed
        # TODO: validate json records?
        return super()._prepare_records()

    def _write(self) -> None:
        if not self.object_to_record:
            return super()._write(dumps(self.records, cls=JsonSerialize))

        deleted_records: list = []
        for r in self.records:
            key: str = self.create_key(r)
            if r.get("_sdc_deleted_at"):
                deleted_records.append(
                    {"Key": f"{key.split('/', 1)[1]}.{self.extension}"}
                )
            else:
                super()._write(dumps(r, cls=JsonSerialize), key)

        # delete files if hard_delete is enabled and object_to_record is enabled
        if self.config["hard_delete"] and self.object_to_record:
            super().delete(deleted_records)

    def run(self) -> None:
        # use default behavior, no additional run steps needed
        return super().run(self.context["records"])

from typing import Any

from seaplane_framework.flow import processor
import json


class TaskContext:
    """TaskContext is what a Task recieves."""

    def __init__(self, body: bytes, meta: dict[str, Any]):
        self.body = body
        # For now let's not imply that customers should touch this
        self._meta = meta

    def emit(self, message: bytes, batch_id: int = 1) -> None:
        """Queues message to send once the task completes.
        batch_id: The index with which to refer to this member of the batch."""
        new_meta = self._meta.copy()

        # TODO: losing-array - see entry_point.py for more details

        as_array = json.loads(new_meta["_seaplane_batch_hierarchy"])
        as_array += [batch_id]
        back_to_string = json.dumps(as_array)
        new_meta["_seaplane_batch_hierarchy"] = back_to_string
        output_msg = processor._Msg(message, new_meta)
        processor.write(output_msg)

from typing import Any
import json

from seaplane_framework.flow import processor


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

        # TODO: I expected msgpack would make this an array already?
        new_meta["_seaplane_batch_hierarchy"] = json.loads(new_meta["_seaplane_batch_hierarchy"]) + [batch_id]

        output_msg = processor._Msg(message, new_meta)
        processor.write(output_msg)

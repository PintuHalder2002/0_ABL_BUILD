from dataclasses import dataclass , field
from typing import Any

@dataclass
class AgentRun:
    run_id: str
    task_id: str
    status: str
    actions: list[dict[str, Any]] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


    def __post_init__(self) -> None:
        if not self.run_id:
            raise ValueError("run_id must not be empty")

        if not self.task_id:
            raise ValueError("task_id must not be empty")

        
    def to_dict(self) -> dict[str, Any]:
        return {
            "run_id": self.run_id,
            "task_id": self.task_id,
            "status": self.status,
            "actions": self.actions,
            "metadata": self.metadata,
        }

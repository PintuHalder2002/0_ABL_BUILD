import pytest

from src.core.entities import AgentRun


def test_known_answer():
    run = AgentRun(
        run_id="run_001",
        task_id="task_001",
        status="success",
    )

    result = run.to_dict()

    assert result["run_id"] == "run_001"
    assert result["task_id"] == "task_001"
    assert result["status"] == "success"


def test_edge_case_empty_actions_and_metadata():
    run = AgentRun(
        run_id="run_002",
        task_id="task_002",
        status="failure",
    )

    result = run.to_dict()

    assert result["actions"] == []
    assert result["metadata"] == {}


def test_invalid_run_id():
    with pytest.raises((TypeError, ValueError)):
        AgentRun(
            run_id="",
            task_id="task_003",
            status="success",
        )

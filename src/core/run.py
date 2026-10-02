from .entities import AgentRun



def create_run() -> AgentRun:
    return AgentRun(
        run_id="run_001",
        task_id="task_001",
        status="success",
        actions=[],
        metadata={"day": 1},
    )





















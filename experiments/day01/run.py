from src.core.entities import AgentRun


def main() -> None:
    success = AgentRun(
        run_id="run_success",
        task_id="task_001",
        status="success",
        actions=[
            {"tool": "lookup_order", "result": "found"}
        ],
    )

    failure = AgentRun(
        run_id="run_failure",
        task_id="task_001",
        status="failure",
        actions=[
            {"tool": "lookup_order", "result": "not_found"}
        ],
    )

    print("SUCCESS")
    print(success.to_dict())

    print("\nFAILURE")
    print(failure.to_dict())


if __name__ == "__main__":
    main()

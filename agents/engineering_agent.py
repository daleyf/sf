from typing import Callable, Dict, List


class EngineeringAgent:
    """Engineering Agent implements core engineering tasks."""

    def generate_and_refactor_code(self, code: str) -> str:
        """Return code stripped of trailing whitespace to simulate refactoring."""
        return "\n".join(line.rstrip() for line in code.splitlines())

    def write_and_run_tests(self, tests: List[Callable[[], bool]]) -> bool:
        """
        Execute each test callable and return True if all pass.

        A failing test raises an AssertionError.
        """
        for test in tests:
            assert test()
        return True

    def manage_deployments_and_ci_cd(self, steps: List[str]) -> List[str]:
        """Simulate deployment pipeline by marking each step as executed."""
        return [f"{step} executed" for step in steps]

    def monitor_performance_and_security(self, metrics: Dict[str, float]) -> Dict[str, float]:
        """Return provided metrics to simulate monitoring."""
        return metrics

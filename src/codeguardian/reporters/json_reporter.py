"""JSON reporter for machine-readable output."""
import json
from typing import List
from codeguardian.models.config import Config
from codeguardian.models.violation import Violation
class JSONReporter:
    """Reporter for JSON output."""
    def generate_report(self, violations: List[Violation], config: Config) -> str:
        """Generate a JSON report."""
        report = {
            "project": config.project_name,
            "architecture": config.architecture,
            "total_violations": len(violations),
            "passed": len(violations) == 0,
            "violations": [
                {
                    "rule_type": v.rule_type,
                    "severity": v.severity,
                    "file": str(v.file_path),
                    "line": v.line_number,
                    "message": v.message,
                    "from_module": v.from_module,
                    "to_module": v.to_module,
                }
                for v in violations
            ],
        }
        return json.dumps(report, indent=2, default=str)

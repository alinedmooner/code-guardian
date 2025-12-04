"""Console reporter for displaying misalignments."""
from typing import List
from colorama import Fore, Style
from codeguardian.models.config import Config
from codeguardian.models.misalignment import Misalignment
class ConsoleReporter:
    """Reporter for console/terminal output."""
    def generate_report(self, misalignments: List[Misalignment], config: Config) -> str:
        """Generate a formatted console report."""
        if not misalignments:
            return f"\n{Fore.GREEN}✓ No misalignments found!{Style.RESET_ALL}"
        lines = [
            f"\n{Fore.RED}✗ Found {len(misalignments)} misalignment(s){Style.RESET_ALL}",
            f"Project: {config.project_name}\n"
        ]
        for i, v in enumerate(misalignments, 1):
            color = Fore.RED if v.severity == "error" else Fore.YELLOW
            lines.append(f"{color}[{i}] {v.message}{Style.RESET_ALL}")
            lines.append(f"    File: {v.file_path}:{v.line_number}")
            lines.append(f"    {v.from_module} → {v.to_module}\n")
        return "\n".join(lines)

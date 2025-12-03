"""Rule engine."""
from pathlib import Path
from typing import List, Optional
from codeguardian.analyzer.ast_parser import ImportInfo
from codeguardian.models.config import Config, Module, Rule
from codeguardian.models.violation import Violation
class RuleEngine:
    def __init__(self, config: Config):
        self.config = config
    def check_violations(self, file_path: Path, file_module: str, imports: List[ImportInfo]) -> List[Violation]:
        violations = []
        source_module = self._get_module_for_path(file_path)
        if not source_module:
            return violations
        for import_info in imports:
            target_module = self._get_module_for_import(import_info.module)
            if target_module and source_module != target_module:
                for rule in self.config.rules:
                    v = self._check_no_import_rule(rule, source_module, target_module, file_path, import_info)
                    if v:
                        violations.append(v)
        return violations
    def _check_no_import_rule(self, rule: Rule, source: Module, target: Module, file_path: Path, import_info: ImportInfo) -> Optional[Violation]:
        if rule.type != "no_import":
            return None
        if rule.from_module and rule.from_module != source.name:
            return None
        if rule.from_layer and rule.from_layer != source.layer:
            return None
        is_forbidden = False
        if rule.to_modules and target.name in rule.to_modules:
            is_forbidden = True
        if rule.to_layers and target.layer in rule.to_layers:
            is_forbidden = True
        if is_forbidden:
            return Violation(
                rule_type=rule.type,
                severity=rule.severity,
                file_path=file_path,
                line_number=import_info.line,
                message=rule.message or f"{source.name} cannot import {target.name}",
                from_module=source.name,
                to_module=target.name,
                illegal_import=import_info.module,
                suggestion="Review dependencies"
            )
        return None
    def _get_module_for_path(self, file_path: Path) -> Optional[Module]:
        file_str = str(file_path)
        for module in self.config.modules:
            if module.path in file_str:
                return module
        return None
    def _get_module_for_import(self, import_name: str) -> Optional[Module]:
        for module in self.config.modules:
            module_parts = module.path.replace("src/", "").replace("/", ".")
            if import_name.startswith(module_parts) or import_name.startswith(module.name):
                return module
        return None

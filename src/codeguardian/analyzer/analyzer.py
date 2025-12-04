"""Main analyzer."""
from pathlib import Path
from typing import List
from codeguardian.analyzer.ast_parser import ASTParser
from codeguardian.analyzer.rule_engine import RuleEngine
from codeguardian.models.config import Config
from codeguardian.models.misalignment import Misalignment
class Analyzer:
    def __init__(self, config: Config, root_path: Path):
        self.config = config
        self.root_path = root_path
        self.ast_parser = ASTParser(root_path)
        self.rule_engine = RuleEngine(config)
    def analyze(self) -> List[Misalignment]:
        misalignments = []
        python_files = self.ast_parser.get_python_files(self.root_path, self.config.exclude_paths)
        for file_path in python_files:
            imports = self.ast_parser.parse_file(file_path)
            file_module = self.ast_parser.extract_module_name(file_path)
            misalignments.extend(self.rule_engine.check_misalignments(file_path, file_module, imports))
        return misalignments

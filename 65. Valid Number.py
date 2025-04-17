import re

class Solution:
    def isNumber(self, s: str) -> bool:
        # Regex breakdown:
        # ^[+-]?                 → optional sign at the beginning
        # (
        #    (\d+\.?\d*)         → digits, optional dot, optional digits (e.g., "1", "1.", "1.2")
        #  | (\d*\.?\d+)         → optional digits, optional dot, but requires digits after dot (e.g., ".2")
        # )
        # ([eE][+-]?\d+)?        → optional exponent part with optional sign and digits (e.g., "e10", "E+5")
        # $                      → end of string
        pattern = r'^[+-]?((\d+\.?\d*)|(\d*\.?\d+))([eE][+-]?\d+)?$'
        engine = re.compile(pattern)
        
        # strip leading/trailing spaces before matching
        return bool(engine.match(s.strip()))

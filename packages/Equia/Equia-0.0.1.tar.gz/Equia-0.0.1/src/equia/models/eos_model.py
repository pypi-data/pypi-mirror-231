from enum import Enum


class EosModel(int, Enum):
    PCSAFT = 0
    """0 - PC-SAFT"""
    CO_PCSAFT = 1
    """1 - coPC-SAFT"""
    PR = 2
    """2 - PR"""
    SRK = 3
    """3 - SRK"""

    def __str__(self) -> str:
        return str(self.value)

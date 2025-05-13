# Program ti Safely create a nested directory

from pathlib import Path

Path("D:/abc/def/ghi").mkdir(parents=True,exist_ok=True)

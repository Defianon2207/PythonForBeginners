import filecmp
from pathlib import Path

result = filecmp.cmp("first.txt", "second.txt")
print(result)

Path("folder_a/documents").mkdir(parents=True, exist_ok=True)
Path("folder_b/documents").mkdir(parents=True, exist_ok=True)

Path("folder_a/documents/report.txt").write_text("Annual report")
Path("folder_b/documents/report.txt").write_text("Annual report")

match, mismatch, errors = filecmp.cmpfiles(
    "folder_a",
    "folder_b",
    ["documents/report.txt"],
    shallow=False
)

print("Match:", match)
print("Mismatch:", mismatch)
print("Errors:", errors)

# Example of dircmp

a = Path("folder_a")
b = Path("folder_b")

a.mkdir(exist_ok=True)
b.mkdir(exist_ok=True)

(a / "same.txt").write_text("Hello")
(b / "same.txt").write_text("Hello")

(a / "changed.txt").write_text("Apple")
(b / "changed.txt").write_text("Mango")

(a / "only_a.txt").write_text("Only in A")
(b / "only_b.txt").write_text("Only in B")

comparison = filecmp.dircmp(
    "folder_a",
    "folder_b",
    shallow=False
)

comparison.report()
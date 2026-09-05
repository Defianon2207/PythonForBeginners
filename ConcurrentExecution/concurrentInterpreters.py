import subprocess

result = subprocess.run(
    [
        "python3",
        "-c",
        """
import sys
print("Normal message")
print("Error message", file=sys.stderr)
"""
    ],
    capture_output=True,
    text=True
)

print("STDOUT:", result.stdout.strip())
print("STDERR:", result.stderr.strip())
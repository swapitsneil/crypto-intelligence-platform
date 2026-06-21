import subprocess
import sys

python_exe = sys.executable

subprocess.run([python_exe, "scripts/extract.py"])
subprocess.run([python_exe, "scripts/transform.py"])
subprocess.run([python_exe, "scripts/kpi_engine.py"])

print("Pipeline Completed Successfully")
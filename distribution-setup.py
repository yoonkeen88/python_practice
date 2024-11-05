# setup.py
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["numpy", "matplotlib", "scipy", "tkinter"],
    "includes": ["numpy", "matplotlib.backends.backend_tkagg"],
    "include_files": [],
    "excludes": []
}

# GUI applications require a different base on Windows
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="NormalDistCalculator",
    version="1.0",
    description="Normal Distribution Calculator",
    options={"build_exe": build_exe_options},
    executables=[Executable("your_script.py", base=base, icon="app.ico")]  # icon은 선택사항
)

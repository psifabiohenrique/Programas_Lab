import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["PySimpleGUI", "pyperclip", "N_Seq", "Recorrencia", "ValorU"], "excludes": []}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Calculos Variabilidade",
    version="0.1",
    description="empty",
    options={"build_exe": build_exe_options, "install_exe":{"force":True},},
    executables=[Executable("main.py", base=base, icon="Icone.ico", target_name="VarCalc.exe", )],
)

from cx_Freeze import setup, Executable
# executables = [Executable("seu_script.py", base=None, targetName="seu_executavel")]

setup(
    name="main",
    version="1.0",
    description="Interface tkinter",
    executables=[Executable("main.py" , base=None , target_name="Calculo Senai")]
)

name = "gui"
version = "1.0.0"
requires = ["bleeding_rez-2.29+", "python>=3,<4", "PySide2"]
private_build_requires = ["rezutil-1"]
tools = [
    "run-gui",
]
build_command = "python -m rezutil build {root}"
# Upon a new release of pip, wheel or setuptools, this is what you edit



def commands():
    global env
    global alias
    env.PYTHONPATH.prepend("{root}/python")
    alias("run-gui", "python {root}/python/rezgui/app.py")

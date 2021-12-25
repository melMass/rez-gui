# rez-gui

Early W.I.P to replace the old rezgui module of rez as a package.
This fork is updated to the latest Qt.py

## requires
- rez with the following packages:
  - [bleeding_rez](https://github.com/mottosso/bleeding-rez)
  - python
  - PySide2 (using [pipz](https://github.com/mottosso/rez-pipz) for instance)

## Install

```shell
git clone https://github.com/melMass/rez-gui.git
cd rez-gui
rez build --install --clean
```

## Usage

```shell
rez env gui -- gui
```

## Contribute

This is a very quick fix for now, the functions I needed from the original module are working (inspecting contexts and variants).
Please do not hesitate to make PRs if you are fixing other parts of rezgui, Issues are welcomed as well.


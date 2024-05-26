# Author-Kevin Schneider
# Description-Install Assembly tab into Fusion design toolbar

import adsk.core, adsk.fusion, adsk.cam, os, sys, traceback, pathlib, zipfile
import urllib.request
from sys import platform

app = adsk.core.Application.get()
ui = app.userInterface

ui.messageBox(
    "Ready to install a new Design document Toolbar with a new Assembly Tab? ",
    "Install Assembly Tab",
    3,
    1,
)


def run(context):
    ui = None
    try:

        if platform == "win32":
            winassytb()
            return

        elif platform == "darwin":
            macassytb()
            return

    except:
        if ui:
            ui.messageBox("Failed:\n{}".format(traceback.format_exc()))


def close():
    ui.messageBox(
        "New Design toolbar with Assembly Tab is installed. Please save and close or close all open documents then restart Fusion",
        "Install Assembly Tab",
        0,
        2,
    )


def macassytb():
    try:
        code_path = pathlib.Path(os.path.dirname(sys.executable))
        print(f"MACOS {code_path}")

        tb_path = os.path.join(
            code_path.parent.parent.parent.parent.parent,
            "Libraries",
            "Applications",
            "Fusion",
            "Fusion",
            "UI",
            "FusionUI",
            "Resources",
            "Toolbar",
            "TabToolbars.xml",
        )

        tb_zip = os.path.join(
            code_path.parent.parent.parent.parent.parent,
            "Libraries",
            "Applications",
            "Fusion",
            "Fusion",
            "UI",
            "FusionUI",
            "Resources",
            "Toolbar",
            "TabToolbars.zip",
        )

        if os.path.exists(tb_path):
            zipfile.ZipFile(tb_zip, mode="w").write(tb_path)
        else:
            return

        urllib.request.urlretrieve(
            "https://raw.githubusercontent.com/schneik80/Fusion-Assembly-Tab/main/TabToolbars.xml",
            tb_path,
        )

        close()

    except:
        if ui:
            ui.messageBox("Failed:\n{}".format(traceback.format_exc()))


def winassytb():
    try:
        code_path = pathlib.Path(os.path.dirname(sys.executable))

        tb_path = os.path.join(
            code_path.parent,
            "Fusion",
            "UI",
            "FusionUI",
            "Resources",
            "Toolbar",
            "TabToolbars.xml",
        )

        tb_zip = os.path.join(
            code_path.parent,
            "Fusion",
            "UI",
            "FusionUI",
            "Resources",
            "Toolbar",
            "TabToolbars.zip",
        )

        if os.path.exists(tb_path):
            zipfile.ZipFile(tb_zip, mode="w").write(tb_path)
        else:
            return

        urllib.request.urlretrieve(
            "https://raw.githubusercontent.com/schneik80/Fusion-Assembly-Tab/main/TabToolbars.xml",
            tb_path,
        )

        close()
        # call to open the path in os file manager
        # os.startfile(tb_path)

    except:
        if ui:
            ui.messageBox("Failed:\n{}".format(traceback.format_exc()))

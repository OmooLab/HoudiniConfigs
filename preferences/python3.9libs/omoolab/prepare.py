import hou
import os
from pathlib import Path
from omoospace import Omoospace, get_route_str, create_omoospace

BACKUP_NAMES = ["old", "Bak", "bak", ".bak", "Backup", "backup"]
HDA_PATHS = ["Contents/HDAs"]
HDA_EXTS = [".hda", ".otl"]


def set_file_env():
    try:
        file_path = Path(hou.hipFile.path()).resolve()
        omoos_path = Omoospace(file_path).root_path.as_posix()
        # hou.putenv("JOB", omoos_path)
        hou.hscript(f"setenv JOB = {omoos_path}")
        print(f"Current omoospace path $JOB: {omoos_path}")

        route_str = get_route_str(file_path)
        # hou.putenv("ROUTE", route_str)
        # hou.putenv not save to file. so use hscript "setenv"
        hou.hscript(f"setenv ROUTE = {route_str}")
        print(f"Current subspace route $ROUTE: {route_str}")

    except:
        try:
            default_omoos = Omoospace(Path(Path.home(), "DefaultOmoos"))
        except:
            default_omoos = create_omoospace(
                name="Default Omoos",
                root_dir=Path.home(),
                description="Default omoospace inited by houdini as default project.",
                reveal_in_explorer=False
            )
        default_omoos_path = default_omoos.root_path.as_posix()
        # hou.putenv("JOB", default_omoos_path)
        hou.hscript(f"setenv JOB = {default_omoos_path}")
        
        route_str = "Untitled"
        # hou.putenv("ROUTE", route_str)
        # hou.putenv not save to file. so use hscript "setenv"
        hou.hscript(f"setenv ROUTE = {route_str}")

        print("No omoospace detected, so...")
        print(f"set default omoospace path $JOB: {default_omoos_path}")
        print(f"set default subspace route $ROUTE: {route_str}")


def install_hda():
    project_path = hou.getenv("JOB")
    if project_path:
        for hda_path in HDA_PATHS:
            for root, dirs, files in os.walk(Path(project_path, hda_path)):
                dirs[:] = [d for d in dirs if d not in BACKUP_NAMES]
                for file in files:
                    hda = Path(root, file)
                    if hda.suffix in HDA_EXTS:
                        hou.hda.installFile(hda.as_posix())


def init_file():
    set_file_env()
    install_hda()

import hou
import os
from pathlib import Path
from omoospace import Omoospace, get_route_str, create_omoospace

BACKUP_NAMES = ["old", "Bak", "bak", ".bak", "Backup", "backup"]
HDA_PATHS = ["Contents/HDAs"]
HDA_EXTS = [".hda", ".otl"]


def set_project_env():
    default_path = Path(Path.home(), "DefaultOmoos")

    try:
        default_omoos = Omoospace(default_path)
    except:
        default_omoos = create_omoospace(
            name="Default Omoos",
            root_dir=Path.home(),
            description="Default omoospace inited by houdini as default project.",
            reveal_in_explorer=False
        )
    default_path = default_omoos.root_path.as_posix()
    hou.putenv("JOB", default_path)

    try:
        file_path = Path(hou.hipFile.path()).resolve()
        omoospace_path = Omoospace(file_path).root_path.as_posix()
        hou.putenv("JOB", omoospace_path)
        print(f"Current omoospace path $JOB: {omoospace_path}")

        route_str = get_route_str(file_path)
        hou.putenv("ROUTE", route_str)
        print(f"Current subspace route $ROUTE: {route_str}")

    except:
        route_str = "Untitled"
        hou.putenv("ROUTE", route_str)

        print("No omoospace detected, so...")
        print(f"set default omoospace path $JOB: {default_path}")
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
    set_project_env()
    install_hda()

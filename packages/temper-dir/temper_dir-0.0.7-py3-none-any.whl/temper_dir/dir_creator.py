import pathlib
import datetime

BASE_TEMP_DIR = pathlib.Path.home() / "temp"


def create_dir() -> tuple[pathlib.Path, bool]:
    current_dir = datetime.datetime.now().strftime("%Y-%m-%d")
    temp_dir_path = pathlib.Path(BASE_TEMP_DIR) / current_dir

    created = True
    if temp_dir_path.exists():
        created = False

    temp_dir_path.mkdir(parents=True, exist_ok=True)

    return temp_dir_path, created

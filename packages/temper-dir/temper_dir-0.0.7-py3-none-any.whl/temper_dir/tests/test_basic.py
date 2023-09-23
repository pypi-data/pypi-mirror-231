from temper_dir.dir_creator import create_dir
import datetime
import pathlib
import sys
import io
import subprocess

SUPPOSED_TEMP_DIR = (
    pathlib.Path.home() / "temp" / datetime.datetime.now().strftime("%Y-%m-%d")
)


def _validate_supposed_dir_doesnt_exist():
    assert SUPPOSED_TEMP_DIR.exists() == False


def test_basic_functionality():
    _validate_supposed_dir_doesnt_exist()

    created = False

    try:
        temp_dir_path, created = create_dir()

        assert temp_dir_path == SUPPOSED_TEMP_DIR
        assert created == True

    finally:
        if created:
            SUPPOSED_TEMP_DIR.rmdir()


def test_cli():
    _validate_supposed_dir_doesnt_exist()

    try:
        pipe = subprocess.run(
            "python3 -m temper_dir", shell=True, check=True, stdout=subprocess.PIPE
        )
        data = pipe.stdout.decode("utf-8")
        assert "Created a new temp" in data

    finally:
        SUPPOSED_TEMP_DIR.rmdir()


def test_folder_exists():
    _validate_supposed_dir_doesnt_exist()
    SUPPOSED_TEMP_DIR.mkdir(parents=True, exist_ok=False)
    try:
        pipe = subprocess.run(
            "python3 -m temper_dir", shell=True, check=True, stdout=subprocess.PIPE
        )
        data = pipe.stdout.decode("utf-8")
        assert "Using existing temp" in data
    finally:
        SUPPOSED_TEMP_DIR.rmdir()

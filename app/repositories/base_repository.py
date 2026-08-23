import json
from pathlib import Path


class BaseRepository:

    def __init__(self, file_path):
        self.file_path = Path(file_path)

        # check if the folder exists
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        # Create the file if it doesn't exist
        if not self.file_path.exists():
            self.file_path.write_text("[]")

    def _read_data(self):
        with open(self.file_path, "r") as file:
            return json.load(file)

    def _write_data(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)
import json
import os
from ins_kit.ins_parent import ins_parent


class JSON(ins_parent):

    def __init__(self, file_path):
        self.file_path = file_path

    def _encode(self, data: dict, format=False) -> str:

        if format:
            return json.dumps(data, skipkeys=True,
                              allow_nan=True,
                              indent=6)
        else:
            return json.dumps(data)

    def _decode(self, data: str) -> dict:
        
        if data == None:
             return {}
        return json.loads(data)

    def _file_create(self, data):
        """Creates a new JSON file with the given data, ensuring keys start with underscores and adding comments."""
        # Preprocess data to add underscores to keys
        data = {f"_{key}": value for key, value in data.items()}

        # Add comments to the data (optional)
        data["_comment"] = "This is a comment"

        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def _file_read(self, file_path):
        """Reads the contents of the JSON file."""
        try:
            with open(file_path, 'r', encoding="utf8") as f:
                data = json.load(f)
            return data
        except FileNotFoundError as  err:
            
            print(f"File {file_path} not found{err}.")
            return {}

    def _file_write(self, file_path, data: dict):
        """Reads the contents of the JSON file."""
        old = self._file_read(file_path)
        if old == False:
            old: dict = {}
        old.update(data)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            json.dump(old, f, indent=4)

    def _update(self, data):
        """Updates the contents of the JSON file with the given data, ensuring keys start with underscores."""
        # Preprocess data to add underscores to keys
        data = {f"_{key}": value for key, value in data.items()}

        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

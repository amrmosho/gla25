import os
import shutil
from ins_kit.ins_parent import ins_parent


class Files(ins_parent):

    def _console(self, message):
        """Prints a message to the console."""
        print(message)

    def _include(self, file_path ,attrs={}):
        """Creates a file at the specified path with optional content."""
        try:
            ex = file_path.split(".")
            ui = {}
            fl = file_path[0]
            ck_path = file_path
            if fl == "/":
                ck_path = file_path[1:]
            if self._file_exists(ck_path):
                if ex[-1] == "js":
                    ui = {"_type": "script", "type": "text/javascript",
                          "src": f"{file_path}"}
                elif ex[-1] == "css":
                    ui = {"_type": "link", "rel": "stylesheet",
                          "media": "all", "href": f"{file_path}"}
                    
                   
                    
                self._console(f"File Included successfully: {file_path}")
                if len(attrs) >0:
                    ui.update(attrs)
                return self.ins._ui.tag(ui)
            else:
                self._console(f"Error Included file: {file_path}")

        except Exception as e:
            self._console(f"Error Included file: {e}")

    def _create_file(self, file_path, content=""):
        """Creates a file at the specified path with optional content."""
        try:
            with open(file_path, "w") as f:
                f.write(content)
            self._console(f"File created successfully: {file_path}")
        except Exception as e:
            self._console(f"Error creating file: {e}")

    def _create_folder(self, folder_path):
        """Creates a folder at the specified path."""
        try:
            os.makedirs(folder_path)
            self._console(f"Folder created successfully: {folder_path}")
        except OSError as e:
            if e.errno != e.errno.EEXIST:
                raise
            self._console(f"Folder already exists: {folder_path}")

    def _copy_file(self, source_file, destination_file):
        """Copies a file from source to destination."""
        try:
            shutil.copy2(source_file, destination_file)
            self._console(f"File copied successfully from {
                          source_file} to {destination_file}")
        except Exception as e:
            self._console(f"Error copying file: {e}")

    def _copy_folder(self, source_folder, destination_folder):
        """Copies a folder and its contents recursively."""
        try:
            shutil.copytree(source_folder, destination_folder)
            self._console(f"Folder copied successfully from {
                          source_folder} to {destination_folder}")
        except Exception as e:
            self._console(f"Error copying folder: {e}")

    def _delete_file(self, file_path):
        """Deletes a file."""
        try:
            os.remove(file_path)
            self._console(f"File deleted successfully: {file_path}")
        except FileNotFoundError:
            self._console(f"File not found: {file_path}")
        except OSError as e:
            self._console(f"Error deleting file: {e}")

    def _delete_folder(self, folder_path):
        """Deletes a folder and its contents recursively."""
        try:
            shutil.rmtree(folder_path)
            self._console(f"Folder deleted successfully: {folder_path}")
        except FileNotFoundError:
            self._console(f"Folder not found: {folder_path}")
        except OSError as e:
            self._console(f"Error deleting folder: {e}")

    def _file_exists(self, file_path):
        """Checks if a file exists."""
        return os.path.exists(file_path) and os.path.isfile(file_path)

    def _list_files(self, folder_path):
        """Returns a list of files in the specified folder."""
        try:
            files = [f for f in os.listdir(folder_path) if os.path.isfile(
                os.path.join(folder_path, f))]
            return files
        except FileNotFoundError:
            self._console(f"Folder not found: {folder_path}")
            return []

    def _list_folders_with_prefix(self, folder_path, prefix):
        """Returns a list of folders in the specified folder with the given prefix."""
        try:
            folders = [f for f in os.listdir(folder_path) if os.path.isdir(
                os.path.join(folder_path, f)) and f.startswith(prefix)]
            return folders
        except FileNotFoundError:
            self._console(f"Folder not found: {folder_path}")
            return []

    def _check_folder(self, file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

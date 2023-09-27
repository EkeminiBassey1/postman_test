import json
import os
import importlib.resources
import utils.api_json as file_api


class FolderAndFileManager:
    def __init__(self):
        self.folder_path = os.path.abspath("request_test_folder")

    def get_api_request_file(self):
        json_data = importlib.resources.read_text(file_api, 'api_response.json')

        print(json_data)

        data_dict = json.loads(json_data)
        return data_dict

    def write_into_file(self, file_name: str, content: str):
        with open(file_name, 'w') as file:
            json.dump(content, file)

    def check_if_file_exists(self):
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
            os.chdir(self.folder_path)
        else:
            os.chdir(self.folder_path)
            print(f"The directory '{self.folder_path}' already exists.")
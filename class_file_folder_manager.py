import json
import os


class FolderAndFileManager:
    def get_api_request_file(self):
        #data = importlib.resources.read_text()
        with open("collection_sync.json", 'r') as file:
            json_content = json.load(file)
        return json_content

    def write_into_file(self, file_name: str, content: str):
        request_folder = os.path.join(os.getenv("GITHUB_WORKSPACE"), "request_test_folder")
        os.makedirs(request_folder, exist_ok=True)
        os.chdir(request_folder)

        with open(file_name, 'w') as file:
            json.dump(content, file)
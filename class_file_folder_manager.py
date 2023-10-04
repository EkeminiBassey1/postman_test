import json
import os
import postman_collections as file_collection
import importlib.resources


class FolderAndFileManager:
    def get_api_request_file(self):
        data = json.load(importlib.resources.read_text(file_collection, "collection_sync.json"))
        print(data)

        with open("postman_collections/collection_sync.json", 'r') as file:
            json_content = json.load(file)
        return json_content

    def write_into_file(self, file_name: str, content: str):
        request_folder = os.path.join(os.getenv("GITHUB_WORKSPACE"), "request_test_folder")
        os.makedirs(request_folder, exist_ok=True)
        os.chdir(request_folder)

        with open(file_name, 'w') as file:
            json.dump(content, file)
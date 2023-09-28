import json


class FolderAndFileManager:
    def get_api_request_file(self):
        with open("api_response.json", 'r') as file:
            json_content = json.load(file)
        return json_content

    def write_into_file(self, file_name: str, content: str):
        with open(file_name, 'w') as file:
            json.dump(content, file)

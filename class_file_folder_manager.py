import json
import importlib.resources
import utils.api_json as file_api


class FolderAndFileManager:
    def get_api_request_file(self):
        json_data = importlib.resources.read_text(file_api, 'api_response.json')
        data_dict = json.loads(json_data)
        return data_dict

    def write_into_file(self, file_name: str, content: str):
        with open(file_name, 'w') as file:
            json.dump(content, file)
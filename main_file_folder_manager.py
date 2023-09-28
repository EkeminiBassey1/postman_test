from class_file_folder_manager import FolderAndFileManager

folder_file_manager = FolderAndFileManager()

data_dict = folder_file_manager.get_api_request_file()

for item in data_dict['collection']['item']:
    file_name = str(item['id']) + ".json"
    folder_file_manager.write_into_file(file_name, item)
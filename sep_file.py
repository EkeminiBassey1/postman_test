import json
import os

with open('api_response.json', 'r') as json_file:
    data = json.load(json_file)

if 'item' in data and isinstance(data['item'], list):
    items = data['item']

    os.makedirs('item_files', exist_ok=True)
    existing_item_files = os.listdir('item_files')
    next_index = len(existing_item_files)

    for item in items:
        item_filename = f'item_{next_index}.json'
        with open(os.path.join('item_files', item_filename), 'w') as item_file:
            json.dump(item, item_file, indent=4)
        print(f'Saved {item_filename}')
        next_index += 1

else:
    print('Invalid JSON format. The "item" key should exist and be a list.')

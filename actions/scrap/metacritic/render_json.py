import json

def render_json(filename,all_filtered_items,):
    output_file_name = f"{filename}_{len(all_filtered_items)}.json"
    with open(output_file_name, 'w') as output_file:
        json.dump(all_filtered_items, output_file, indent=2)
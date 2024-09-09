import json

def remove_duplicates(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    unique_data = []
    seen = set()

    for item in data:
        item_tuple = tuple(item.items())
        if item_tuple not in seen:
            seen.add(item_tuple)
            unique_data.append(item)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(unique_data, f, ensure_ascii=False, indent=4)

    duplicate_count = len(data) - len(unique_data)
    print(f"Removed {duplicate_count} duplicates")
    print(f"Total {len(unique_data)} unique items")
              
if __name__ == "__main__":
    # modify the file name
    input_file = 'canada.json'
    output_file = 'deduplicated_canada.json'
    remove_duplicates(input_file, output_file)

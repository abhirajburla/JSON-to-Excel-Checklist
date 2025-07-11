import json

try:
    with open('Mechanical.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print("JSON syntax is VALID")
    print(f"Total items in results: {len(data['results'])}")
    print(f"Expected total_items: {data['total_items']}")
    print(f"Found items: {data['found_items']}")
    print(f"Not found items: {data['not_found_items']}")
    print(f"Process ID: {data['process_id']}")
    print(f"Timestamp: {data['timestamp']}")
    
    if len(data['results']) >= 1350:
        print("File has 1350+ items as expected")
    else:
        print(f"File has {len(data['results'])} items (less than 1350)")
        
    if len(data['results']) == data['total_items']:
        print("Item count matches metadata")
    else:
        print(f"Item count mismatch: found {len(data['results'])}, expected {data['total_items']}")
        
except Exception as e:
    print(f"Error: {e}") 
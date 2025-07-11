#!/usr/bin/env python3
"""
JSON Validation Script
Validates JSON syntax and counts items in JSON files.
"""

import json
import sys
import os


def validate_json_file(file_path):
    """
    Validate JSON file syntax and count items.
    
    Args:
        file_path (str): Path to the JSON file
        
    Returns:
        dict: Validation results
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Count items
        item_count = 0
        if 'results' in data and isinstance(data['results'], list):
            item_count = len(data['results'])
        elif isinstance(data, list):
            item_count = len(data)
        else:
            item_count = 1
        
        # Check metadata
        metadata = {}
        if 'total_items' in data:
            metadata['total_items'] = data['total_items']
        if 'found_items' in data:
            metadata['found_items'] = data['found_items']
        if 'not_found_items' in data:
            metadata['not_found_items'] = data['not_found_items']
        if 'process_id' in data:
            metadata['process_id'] = data['process_id']
        if 'timestamp' in data:
            metadata['timestamp'] = data['timestamp']
        
        return {
            'valid': True,
            'item_count': item_count,
            'metadata': metadata,
            'error': None
        }
        
    except json.JSONDecodeError as e:
        return {
            'valid': False,
            'item_count': 0,
            'metadata': {},
            'error': f"JSON syntax error: {e}"
        }
    except FileNotFoundError:
        return {
            'valid': False,
            'item_count': 0,
            'metadata': {},
            'error': f"File not found: {file_path}"
        }
    except Exception as e:
        return {
            'valid': False,
            'item_count': 0,
            'metadata': {},
            'error': f"Unexpected error: {e}"
        }


def main():
    """
    Main function to validate JSON files.
    """
    if len(sys.argv) < 2:
        print("Usage: python validate_json.py <json_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    
    print(f"Validating JSON file: {file_path}")
    print("=" * 50)
    
    result = validate_json_file(file_path)
    
    if result['valid']:
        print("✅ JSON syntax is VALID")
        print(f"📊 Total items found: {result['item_count']}")
        
        if result['metadata']:
            print("\n📋 Metadata:")
            for key, value in result['metadata'].items():
                print(f"   {key}: {value}")
        
        # Check if item count matches metadata
        if 'total_items' in result['metadata']:
            if result['item_count'] == result['metadata']['total_items']:
                print(f"✅ Item count matches metadata ({result['item_count']})")
            else:
                print(f"⚠️  Item count mismatch: found {result['item_count']}, expected {result['metadata']['total_items']}")
        
        if result['item_count'] >= 1350:
            print(f"✅ File has 1350+ items ({result['item_count']})")
        else:
            print(f"⚠️  File has fewer than 1350 items ({result['item_count']})")
            
    else:
        print("❌ JSON syntax is INVALID")
        print(f"Error: {result['error']}")
        sys.exit(1)


if __name__ == "__main__":
    main() 
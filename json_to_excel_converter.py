#!/usr/bin/env python3
"""
JSON to Excel Converter
Converts JSON files containing checklist data to Excel format with specified columns.
"""

import json
import pandas as pd
import argparse
import os
import sys
from pathlib import Path


def load_json_data(json_file_path):
    """
    Load JSON data from file.
    
    Args:
        json_file_path (str): Path to the JSON file
        
    Returns:
        dict: Loaded JSON data
    """
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{json_file_path}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in '{json_file_path}': {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{json_file_path}': {e}")
        sys.exit(1)


def extract_data_from_json(data):
    """
    Extract relevant data from JSON structure.
    
    Args:
        data (dict): JSON data
        
    Returns:
        list: List of dictionaries containing the extracted data
    """
    extracted_data = []
    
    # Check if the JSON has a 'results' key (like in the Plumbing.json example)
    if 'results' in data and isinstance(data['results'], list):
        results = data['results']
    elif isinstance(data, list):
        # If the JSON is directly a list
        results = data
    else:
        # If it's a single object, wrap it in a list
        results = [data]
    
    for item in results:
        if isinstance(item, dict):
            # Extract the required fields
            row_data = {
                'Category': item.get('category', ''),
                'scope of work': item.get('scope_of_work', ''),
                'checklist': item.get('checklist', ''),
                'sector': item.get('sector', ''),
                'sheet number': item.get('sheet_number', ''),
                'spec section': item.get('spec_section', ''),
                'notes reasoning': item.get('reasoning', '')
            }
            extracted_data.append(row_data)
    
    return extracted_data


def create_excel_file(data, output_file_path):
    """
    Create Excel file from the extracted data.
    
    Args:
        data (list): List of dictionaries containing the data
        output_file_path (str): Path for the output Excel file
    """
    try:
        # Create DataFrame
        df = pd.DataFrame(data)
        
        # Create Excel writer object
        with pd.ExcelWriter(output_file_path, engine='openpyxl') as writer:
            # Write DataFrame to Excel
            df.to_excel(writer, sheet_name='Checklist Data', index=False)
            
            # Get the workbook and worksheet
            workbook = writer.book
            worksheet = writer.sheets['Checklist Data']
            
            # Auto-adjust column widths
            for column in worksheet.columns:
                max_length = 0
                column_letter = column[0].column_letter
                
                for cell in column:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(str(cell.value))
                    except:
                        pass
                
                # Set column width (with some padding)
                adjusted_width = min(max_length + 2, 50)  # Cap at 50 characters
                worksheet.column_dimensions[column_letter].width = adjusted_width
        
        print(f"Excel file created successfully: {output_file_path}")
        print(f"Total rows exported: {len(data)}")
        
    except Exception as e:
        print(f"Error creating Excel file: {e}")
        sys.exit(1)


def main():
    """
    Main function to handle command line arguments and execute the conversion.
    """
    parser = argparse.ArgumentParser(
        description='Convert JSON files to Excel format with specified columns',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python json_to_excel_converter.py Plumbing.json
  python json_to_excel_converter.py data.json -o output.xlsx
  python json_to_excel_converter.py input.json -o "My Checklist.xlsx"
        """
    )
    
    parser.add_argument(
        'json_file',
        help='Path to the input JSON file'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Output Excel file path (default: input_filename.xlsx)'
    )
    
    args = parser.parse_args()
    
    # Validate input file
    if not os.path.exists(args.json_file):
        print(f"Error: Input file '{args.json_file}' does not exist.")
        sys.exit(1)
    
    # Determine output file path
    if args.output:
        output_path = args.output
    else:
        # Use input filename with .xlsx extension
        input_path = Path(args.json_file)
        output_path = input_path.with_suffix('.xlsx')
    
    # Ensure output directory exists
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    print(f"Converting '{args.json_file}' to '{output_path}'...")
    
    # Load JSON data
    json_data = load_json_data(args.json_file)
    
    # Extract relevant data
    extracted_data = extract_data_from_json(json_data)
    
    if not extracted_data:
        print("Warning: No data found in the JSON file.")
        sys.exit(1)
    
    # Create Excel file
    create_excel_file(extracted_data, output_path)
    
    print("Conversion completed successfully!")


if __name__ == "__main__":
    main() 
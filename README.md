# JSON to Excel Converter

A Python script that converts JSON files containing checklist data to Excel format with specific columns.

## Features

- Converts JSON data to Excel (.xlsx) format
- Extracts specific columns: Category, scope of work, checklist, sector, sheet number, spec section, notes reasoning
- Auto-adjusts column widths for better readability
- Handles various JSON structures (with 'results' key or direct arrays)
- Command-line interface with flexible output naming

## Installation

1. Make sure you have Python 3.6+ installed
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Convert a JSON file to Excel (output will be named `input_filename.xlsx`):

```bash
python json_to_excel_converter.py Plumbing.json
```

### Specify Output File

Convert with a custom output filename:

```bash
python json_to_excel_converter.py Plumbing.json -o "My Checklist.xlsx"
```

### Examples

```bash
# Convert Plumbing.json to Plumbing.xlsx
python json_to_excel_converter.py Plumbing.json

# Convert with custom output name
python json_to_excel_converter.py data.json -o "Project Checklist.xlsx"

# Convert with spaces in filename
python json_to_excel_converter.py "input data.json" -o "Output File.xlsx"
```

## Expected JSON Structure

The script expects JSON files with one of these structures:

### Structure 1: With 'results' key (like Plumbing.json)
```json
{
  "process_id": "...",
  "results": [
    {
      "category": "Pre-Bid",
      "scope_of_work": "02 40 00 Demolition",
      "checklist": "Backfill any remaining holes...",
      "sector": "Industrial",
      "sheet_number": "",
      "spec_section": "",
      "reasoning": "Item not found in documents"
    }
  ]
}
```

### Structure 2: Direct array
```json
[
  {
    "category": "Pre-Bid",
    "scope_of_work": "02 40 00 Demolition",
    "checklist": "Backfill any remaining holes...",
    "sector": "Industrial",
    "sheet_number": "",
    "spec_section": "",
    "reasoning": "Item not found in documents"
  }
]
```

## Output Columns

The Excel file will contain these columns:
- **Category**: The category of the checklist item
- **scope of work**: The scope of work description
- **checklist**: The checklist item text
- **sector**: The sector information
- **sheet number**: Sheet number reference
- **spec section**: Specification section reference
- **notes reasoning**: Reasoning or notes about the item

## Error Handling

The script includes comprehensive error handling for:
- Missing input files
- Invalid JSON format
- File permission issues
- Excel creation errors

## Requirements

- Python 3.6+
- pandas >= 1.5.0
- openpyxl >= 3.0.0 
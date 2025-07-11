@echo off
echo JSON to Excel Converter
echo ======================
echo.

if "%~1"=="" (
    echo Usage: convert_json_to_excel.bat [JSON_FILE] [OUTPUT_FILE]
    echo.
    echo Examples:
    echo   convert_json_to_excel.bat Plumbing.json
    echo   convert_json_to_excel.bat data.json "My Output.xlsx"
    echo.
    pause
    exit /b 1
)

if "%~2"=="" (
    python json_to_excel_converter.py "%~1"
) else (
    python json_to_excel_converter.py "%~1" -o "%~2"
)

echo.
echo Press any key to exit...
pause >nul 
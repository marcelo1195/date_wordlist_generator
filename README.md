# Date Wordlist Generator

This program generates a wordlist of dates in various formats.

## Usage

Run the program from the command line:

python main.py --start YYYY/MM/DD --end YYYY/MM/DD --format FORMAT --output OUTPUT_FILE

Arguments:
- --start: Start date (optional, default is 2000-01-01)
- --end: End date (optional, default is 2030-12-31)
- --format: Date format (DDMMYY, MMDDYY, DDMMYYYY, or MMDDYYYY, default is DDMMYY)
- --output: Output file name (optional, default is date_wordlist.txt)

Example:
python main.py --start 01/01/2023 --end 31/12/2023 --format DDMMYYYY --output dates_2023.txt

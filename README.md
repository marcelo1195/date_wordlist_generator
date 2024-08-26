# Date Wordlist Generator

This program generates a wordlist of dates in various formats.

## Usage

Run the program from the command line:

python main.py --start YYYY-MM-DD --end YYYY-MM-DD --format FORMAT --output OUTPUT_FILE

Arguments:
- --start: Start date (optional, default is 2000-01-01)
- --end: End date (optional, default is 2030-12-31)
- --format: Date format (DD/MM/YY, MM/DD/YY, DD/MM/YYYY, or MM/DD/YYYY, default is DD/MM/YY)
- --output: Output file name (optional, default is date_wordlist.txt)

Example:
python main.py --start 2023-01-01 --end 2023-12-31 --format DD/MM/YYYY --output dates_2023.txt
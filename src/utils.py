
import argparse
from datetime import datetime

def parse_arguments():
  parser = argparse.ArgumentParser(description='Date Wordlist Generator')
  parser.add_argument('--start', type=str, help='Start date (DD/MM/YYYY)')
  parser.add_argument('--end', type=str, help='End date (DD/MM/YYYY)')
  parser.add_argument('--format', type=str, choices=['DDMMYY', 'MMDDYY', 'DDMMYYYY', 'MMDDYYYY'], default='DDMMYY', help='Date format')
  parser.add_argument('--output', type=str, default='date_wordlist.txt', help='Output file name')

  args = parser.parse_args()

  return {
      'start_date': datetime.strptime(args.start, '%d/%m/%Y') if args.start else None,
      'end_date': datetime.strptime(args.end, '%d/%m/%Y') if args.end else None,
      'format': args.format,
      'output_file': args.output
  }
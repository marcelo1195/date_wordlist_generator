# src/utils.py
import argparse
from datetime import datetime

def parse_arguments():
  parser = argparse.ArgumentParser(description='Date Wordlist Generator')
  parser.add_argument('--start', type=str, help='Start date (DD/MM/YYYY)')
  parser.add_argument('--end', type=str, help='End date (DD/MM/YYYY)')
  parser.add_argument('--format', type=str, choices=['DD/MM/YY', 'MM/DD/YY', 'DD/MM/YYYY', 'MM/DD/YYYY'], default='DD/MM/YY', help='Date format')
  parser.add_argument('--output', type=str, default='date_wordlist.txt', help='Output file name')

  return parser.parse_args()

def parse_date(date_string):
  return datetime.strptime(date_string, '%d/%m/%Y')
import argparse
from datetime import datetime

def parse_arguments():
    parser = argparse.ArgumentParser(description='Date Wordlist Generator')
    parser.add_argument('--start', type=str, help='Start date(YYYY-MM-DD)')
    parser.add_argument('--end', type=str, help='End date (YYYY-MM-DD)')
    parser.add_argument('--format', type=str, choices=['DD/MM/YY', 'MM/DD/YY', 'DD/MM/YYYY', 'MM/DD/YYYY'], default='DD/MM/YY', help='Date format')
    parser.add_argument('--output', type=str, default='date_wordlist.txt', help='Output file name')

    args = parser.parse_args()

    return {
        'start_date': datetime.strptime(args.start, '%Y-%m-%d') if args.start else None,
        'end_date': datetime.strptime(args.end, '%Y-%m-%d') if args.end else None,
        'format': args.format,
        'output_file': args.output
    }
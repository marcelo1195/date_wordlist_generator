# main.py
import os
import sys
from datetime import datetime

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

from src.utils import parse_arguments, parse_date
from src.generator import generate_dates

def main():
  args = parse_arguments()

  start_date = parse_date(args.start) if args.start else datetime(2000, 1, 1)
  end_date = parse_date(args.end) if args.end else datetime(2030, 12, 31)
  date_format = args.format
  output_file = args.output

  generated_dates = generate_dates(
      start_date=start_date,
      end_date=end_date,
      format=date_format,
      output_file=output_file
  )

  print(f"Generated {len(generated_dates)} dates.")

if __name__ == "__main__":
  main()
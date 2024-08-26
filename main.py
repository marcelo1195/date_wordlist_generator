import os
import sys
from datetime import datetime

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

from src.utils import parse_arguments
from src.generator import generate_dates

def main():
  args = parse_arguments()

  start_date = args.get('start_date') or datetime(2000, 1, 1)
  end_date = args.get('end_date') or datetime(2030, 12, 31)
  date_format = args.get('format', 'DD/MM/YY')
  output_file = args.get('output_file', 'date_wordlist.txt')

  generated_dates = generate_dates(
      start_date=start_date,
      end_date=end_date,
      format=date_format,
      output_file=output_file
  )

  print(f"Generated {len(generated_dates)} dates.")

if __name__ == "__main__":
  main()
# main.py
import os
import sys
from datetime import datetime
from src.utils import parse_arguments
from src.generator import generate_dates

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)
def main():
  # Parse command-line arguments
  args = parse_arguments()

  # Extract arguments with default values
  start_date = args['start_date'] or datetime(2000, 1, 1)
  end_date = args['end_date'] or datetime(2030, 12, 31)
  date_format = args['format']
  output_file = args['output_file']

  # Generate dates
  generated_dates = generate_dates(
      start_date=start_date,
      end_date=end_date,
      format=date_format,
      output_file=output_file
  )

  print(f"Generated {len(generated_dates)} dates.")
if __name__ == "__main__":
  main()
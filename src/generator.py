from datetime import  datetime, timedelta
import os
from src.file_handler import weite_to_file

def generate_dates(**kwargs):
    """
      Generate a list of dates between two dates in a specified format.

      :param start_date: Start date (default: 1900-01-01)
      :param end_date: End date (default: 2030-12-31)
      :param format: Date format (default: 'DD/MM/YY')
      :param output_file: Output file name (default: 'date_wordlist.txt')
      :return: List of formatted date strings
      """
    # Default kargs values
    start_date = kwargs.get('start_date', datetime(1900, 1, 1))
    end_date = kwargs.get('end_date', datetime(2030, 12, 31))
    date_format = kwargs.get('format', 'DDMMYY')
    output_file = kwargs.get('output_file', 'date_wordlist.txt')

    dates = []
    current_date = start_date
    while current_date <= end_date:
        print(f"Processing date: {current_date}")
        # Format the date according to the specified format
        if date_format == 'DDMMYY':
            formated_date = current_date.strftime('%d%m%y')
        elif date_format == 'MMDDYY':
            formated_date = current_date.strftime('%m%d%y')
        elif date_format == 'DDMMYYYY':
            formated_date = current_date.strftime('%d%m%Y')
        elif date_format == 'MMDDYYYY':
            formated_date = current_date.strftime('%m%d%Y')
        else:
            raise ValueError(f"Invalid date format: {date_format}")
        dates.append(formated_date)
        current_date += timedelta(days=1)

    print("Finished generating dates")

    # Ensure the output directory exists
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'output')
    os.makedirs(output_dir, exist_ok=True)

    # Create the full path for the output file
    output_path = os.path.join(output_dir, output_file)

    print(f"Attempting to write to file: {output_path}")
    weite_to_file(dates, output_path)
    print(f"File writing completed")

    print(f"Wordlist generated successfully. Output file: {output_file}")

    return dates
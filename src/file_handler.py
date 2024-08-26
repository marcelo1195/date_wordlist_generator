def weite_to_file(dates, filename):
    with open(filename, 'w') as f:
        for date in dates:
            f.write(f"{date}\n")
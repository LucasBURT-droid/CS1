import csv

def export_to_csv(filename, headers, *arrays):
    """
    Exports parallel arrays to a CSV file.

    Args:
        filename (str): The name of the CSV file to create.
        headers (list): A list of header names for each column.
        *arrays: Variable number of array arguments (lists or tuples).
               All arrays must have the same length.
    """
    if not arrays:
        raise ValueError("At least one array must be provided.")
    
    num_rows = len(arrays[0])
    for arr in arrays:
        if len(arr) != num_rows:
            raise ValueError("All arrays must have the same length.")
    
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)
        for i in range(num_rows):
            row = [arr[i] for arr in arrays]
            csvwriter.writerow(row)
import csv
import urllib.parse

# File containing KPI names and URL encoded queries
input_file = 'kpi_queries.txt'

# Function to create a CSV file for each KPI
def create_csv_for_kpi(kpi_name, query):
    # Decode the URL-encoded query (you can use it to fetch actual data later)
    decoded_query = urllib.parse.unquote(query)

    # Create a CSV file named after the KPI (like KPI_1.csv, KPI_2.csv)
    csv_filename = f'{kpi_name}.csv'

    # Write some example data to the CSV (replace this with real data fetching logic if needed)
    data = [
        ['timestamp', 'value'],   # Headers
        ['2024-09-30 10:00:00', 100],
        ['2024-09-30 11:00:00', 200],
        ['2024-09-30 12:00:00', 300],
    ]

    # Open the CSV file in write mode and add the data
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f'CSV file created for {kpi_name}: {csv_filename}')

# Read the input text file and process each line
with open(input_file, 'r') as file:
    for line in file:
        # Split the line by '|' to separate KPI name and query
        kpi_name, url_encoded_query = line.strip().split('|')

        # Create a CSV for each KPI
        create_csv_for_kpi(kpi_name, url_encoded_query)

print("CSV files created for all KPIs.")

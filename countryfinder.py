import csv
import geoip2.database
import pandas as pd

# Function to get country for an IP address
def get_country(ip_address):
    try:
        response = reader.country(ip_address)
        return response.country.name
    except geoip2.errors.AddressNotFoundError:
        return 'Unknown'

# Initialize GeoIP reader
reader = geoip2.database.Reader('GeoLite2-Country.mmdb')

# Open the input and output CSV files for IP address processing
with open('ip_addresses.csv', 'r', newline='') as input_file, open('ip_addresses_with_country.csv', 'w', newline='') as output_file:
    # Create CSV reader and writer objects
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)

    # Loop through each row in the input file
    for row in csv_reader:
        ip_address = row[0].split(':')[0]
        port = row[0].split(':')[1]
        timestamp = row[1]
        country = get_country(ip_address)
        csv_writer.writerow([f"{ip_address}:{port},{timestamp}", country])

# Read the CSV file with IP addresses and countries
with open('ip_addresses_with_country.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    countries = []
    visitors = []
    for row in reader:
        visitors.append(row[0])
        countries.append(row[1])

# Write the country names and visitors to a new CSV file with column headers
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Country', 'Visitors'])
    if len(countries) != len(visitors):
        print('Error: number of countries and visitors do not match')
    else:
        for i in range(len(countries)):
            writer.writerow([countries[i], visitors[i]])

# Read data from the generated output CSV file using pandas
data = pd.read_csv("output.csv")

# Print information about the DataFrame
print("Number of rows:", data.shape[0])
print("Number of columns:", data.shape[1])
print("Column names:", data.columns)

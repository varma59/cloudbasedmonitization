import pandas as pd

# Read the output.csv file
df_output = pd.read_csv('output.csv')

# Extract the country names
countries_output = df_output['Country']

# Create a dictionary to store the count of users for each country
user_count_output = {}
for country in countries_output:
    if country not in user_count_output:
        user_count_output[country] = 1
    else:
        user_count_output[country] += 1

# Determine the country with the highest number of users
highest_user_country_output = max(user_count_output, key=user_count_output.get)

# Define S3 storage costs for each country (example values, adjust as needed)
s3_storage_costs = {
    'India': 0.025,    # Example cost per GB for S3 storage in India
    'United States': 0.03,    # Example cost per GB for S3 storage in the United States
    'China': 0.02,    # Example cost per GB for S3 storage in China
    'Brazil': 0.025,    # Example cost per GB for S3 storage in Brazil
    'United Kingdom': 0.035,    # Example cost per GB for S3 storage in the United Kingdom
    'Japan': 0.04,    # Example cost per GB for S3 storage in Japan
    'Canada': 0.03,    # Example cost per GB for S3 storage in Canada
    'Germany': 0.035,    # Example cost per GB for S3 storage in Germany
    'Australia': 0.03,    # Example cost per GB for S3 storage in Australia
    'France': 0.035,    # Example cost per GB for S3 storage in France
    'Italy': 0.035,    # Example cost per GB for S3 storage in Italy
    'Spain': 0.035,    # Example cost per GB for S3 storage in Spain
    'Mexico': 0.025,    # Example cost per GB for S3 storage in Mexico
    'South Korea': 0.04,    # Example cost per GB for S3 storage in South Korea
    'Russia': 0.03,    # Example cost per GB for S3 storage in Russia
    'Netherlands': 0.035,    # Example cost per GB for S3 storage in the Netherlands
    'Sweden': 0.035,    # Example cost per GB for S3 storage in Sweden
    'Switzerland': 0.04,    # Example cost per GB for S3 storage in Switzerland
    'Singapore': 0.03,    # Example cost per GB for S3 storage in Singapore
    'South Africa': 0.025,    # Example cost per GB for S3 storage in South Africa
    # Add more country-specific S3 storage costs as needed
}

# Define CDN costs for each country (example values, adjust as needed)
cdn_costs = {
    'India': 0.1,    # Example cost per GB for CDN in India
    'United States': 0.15,    # Example cost per GB for CDN in the United States
    'China': 0.12,    # Example cost per GB for CDN in China
    'Brazil': 0.08,    # Example cost per GB for CDN in Brazil
    'United Kingdom': 0.14,    # Example cost per GB for CDN in the United Kingdom
    'Japan': 0.18,    # Example cost per GB for CDN in Japan
    'Canada': 0.13,    # Example cost per GB for CDN in Canada
    'Germany': 0.14,    # Example cost per GB for CDN in Germany
    'Australia': 0.12,    # Example cost per GB for CDN in Australia
    'France': 0.14,    # Example cost per GB for CDN in France
    'Italy': 0.13,    # Example cost per GB for CDN in Italy
    'Spain': 0.14,    # Example cost per GB for CDN in Spain
    'Mexico': 0.1,    # Example cost per GB for CDN in Mexico
    'South Korea': 0.15,    # Example cost per GB for CDN in South Korea
    'Russia': 0.1,    # Example cost per GB for CDN in Russia
    'Netherlands': 0.14,    # Example cost per GB for CDN in the Netherlands
    'Sweden': 0.14,    # Example cost per GB for CDN in Sweden
    'Switzerland': 0.15,    # Example cost per GB for CDN in Switzerland
    'Singapore': 0.12,    # Example cost per GB for CDN in Singapore
    'South Africa': 0.1,    # Example cost per GB for CDN in South Africa
    # Add more country-specific CDN costs as needed
}


# Check if costs are defined for the highest user country
if highest_user_country_output in s3_storage_costs and highest_user_country_output in cdn_costs:
    s3_cost = s3_storage_costs[highest_user_country_output]
    cdn_cost = cdn_costs[highest_user_country_output]

    # Determine where to host the data based on cost comparison
    if s3_cost < cdn_cost:
        print(f"For {highest_user_country_output}:")
        print(f"Hosting data in S3 is more cost-effective (S3 cost: {s3_cost}, CDN cost: {cdn_cost}).")
        print("Recommendation: Host data in S3.")
    else:
        print(f"For {highest_user_country_output}:")
        print(f"Using CDN is more cost-effective (S3 cost: {s3_cost}, CDN cost: {cdn_cost}).")
        print("Recommendation: Use CDN for content delivery.")
else:
    print(f"No cost information defined for {highest_user_country_output}. Please define costs for accurate recommendations.")

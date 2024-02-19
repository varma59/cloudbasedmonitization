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

# Sort the dictionary in descending order based on the count of users
sorted_user_count_output = dict(sorted(user_count_output.items(), key=lambda item: item[1], reverse=True))

# Display the top N countries with the highest number of users
N = 5
print(f"Top {N} countries with the highest number of users:")
for i, (country, count) in enumerate(sorted_user_count_output.items()):
    if i == N:
        break
    print(f"{i+1}. {country}: {count} users")

# Determine the country with the highest number of users and suggest a server
highest_user_country_output = max(user_count_output, key=user_count_output.get)
print(f"The country with the highest number of users is {highest_user_country_output}")
print("We recommend setting up a server in this country.")

# Language suggestion based on country
language_suggestions_output = {
    'India': 'Hindi',
    'United States': 'English',
    'China': 'Mandarin',
    # Add more country-language mappings as needed
}

if highest_user_country_output in language_suggestions_output:
    suggested_language_output = language_suggestions_output[highest_user_country_output]
    print(f"We recommend using the {suggested_language_output} language for your content in {highest_user_country_output}.")

# Royalty calculator based on country
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

# Sort the dictionary in descending order based on the count of users
sorted_user_count_output = dict(sorted(user_count_output.items(), key=lambda item: item[1], reverse=True))

# Display the top N countries with the highest number of users
N = 5
print(f"Top {N} countries with the highest number of users:")
for i, (country, count) in enumerate(sorted_user_count_output.items()):
    if i == N:
        break
    print(f"{i+1}. {country}: {count} users")

# Determine the country with the highest number of users and suggest a server
highest_user_country_output = max(user_count_output, key=user_count_output.get)
print(f"The country with the highest number of users is {highest_user_country_output}")
print("We recommend setting up a server in this country.")

# Language suggestion based on country
language_suggestions_output = {
    'India': 'Hindi',
    'United States': 'English',
    'China': 'Mandarin',
    'Brazil': 'Portuguese',
    'United Kingdom': 'English',
    'Japan': 'Japanese',
    'Canada': 'English',
    'Germany': 'German',
    'Australia': 'English',
    'France': 'French',
    'Italy': 'Italian',
    'Spain': 'Spanish',
    'Mexico': 'Spanish',
    'South Korea': 'Korean',
    'Russia': 'Russian',
    'Netherlands': 'Dutch',
    'Sweden': 'Swedish',
    'Switzerland': 'German, French, Italian',
    'Singapore': 'English, Mandarin, Malay, Tamil',
    'South Africa': 'Afrikaans, English',
    'Argentina': 'Spanish',
    'Turkey': 'Turkish',
    'Indonesia': 'Indonesian',
    'Saudi Arabia': 'Arabic',
    # Add more country-language mappings as needed
}

if highest_user_country_output in language_suggestions_output:
    suggested_language_output = language_suggestions_output[highest_user_country_output]
    print(f"We recommend using the {suggested_language_output} language for your content in {highest_user_country_output}.")

# Royalty calculator based on country
royalty_rates_output = {
    'India': 5,   # Example rate for India: 5 rupees per view
    'United States': 10,   # Example rate for the United States: 10 dollars per view
    'China': 3,   # Example rate for China: 3 yuan per view
    'Brazil': 2.5,  # Example rate for Brazil: 2.5 reais per view
    'United Kingdom': 8,  # Example rate for the United Kingdom: 8 pounds per view
    'Japan': 120,  # Example rate for Japan: 120 yen per view
    'Canada': 12,  # Example rate for Canada: 12 dollars per view
    'Germany': 6,  # Example rate for Germany: 6 euros per view
    'Australia': 15,  # Example rate for Australia: 15 dollars per view
    'France': 7,  # Example rate for France: 7 euros per view
    'Italy': 5,  # Example rate for Italy: 5 euros per view
    'Spain': 4,  # Example rate for Spain: 4 euros per view
    'Mexico': 1.5,  # Example rate for Mexico: 1.5 pesos per view
    'South Korea': 800,  # Example rate for South Korea: 800 won per view
    'Russia': 60,  # Example rate for Russia: 60 rubles per view
    'Netherlands': 9,  # Example rate for Netherlands: 9 euros per view
    'Sweden': 70,  # Example rate for Sweden: 70 kronor per view
    'Switzerland': 12,  # Example rate for Switzerland: 12 francs per view
    'Singapore': 15,  # Example rate for Singapore: 15 dollars per view
    'South Africa': 20,  # Example rate for South Africa: 20 rand per view
    # Add more country-royalty-rate mappings as needed
}

if highest_user_country_output in royalty_rates_output:
    royalty_rate_output = royalty_rates_output[highest_user_country_output]
    total_views_output = user_count_output[highest_user_country_output]
    total_earnings_output = total_views_output * royalty_rate_output
    print(f"Based on the royalty rate of {royalty_rate_output} per view in {highest_user_country_output}, your estimated earnings are {total_earnings_output} {royalty_rates_output[highest_user_country_output]}s.")
else:
    print(f"No royalty rate defined for {highest_user_country_output}. Please set up a rate for accurate calculations.")


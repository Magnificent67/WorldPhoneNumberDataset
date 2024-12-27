import csv
import random
import os
os.system('clear')

def load_data(filename):
    data = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for row in csv.DictReader(file):
                data.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        exit(1)
    return data

def generate_phone_number(data, country, city):
    for row in data:
        if row['Country'].lower() == country.lower() and row['PrimaryCityOrNote'].lower() == city.lower():
            local_code = random.choice(row['LocalAreaCode'].split(','))
            return f"{row['CountryCode']} {local_code} {random.randint(100, 999)}-{random.randint(1000, 9999)}"
    return None

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(current_dir, "dataset", "AllCountries.csv")
    data = load_data(filename)
    country = input("Enter country: ").strip()
    city = input("Enter city or note: ").strip()
    phone_number = generate_phone_number(data, country, city)
    print(phone_number if phone_number else "No matches found.")

if __name__ == "__main__":
    main()

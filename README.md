# WorldPhoneNumberDataset

This project provides a large and detailed dataset of phone codes for countries and regions worldwide. It also includes a Python script to generate realistic phone numbers based on user input.

---

## Features

- **Big Phone Code Database**: Includes multiple CSV files organized by regions (e.g., Africa, Europe, Asia, etc.).
- **Phone Number Generator**: A Python script generates random phone numbers based on country and city.
- **Easy to Use**: Simple and lightweight script with structured data.

---

## Note

This dataset does not include all countries and regions. Only a selection of countries and areas is available in the current version.

---

## Files

- `Africa.csv`: Phone codes for African countries.
- `Asia.csv`: Phone codes for Asian countries.
- `Europe.csv`: Phone codes for European countries.
- `NorthAmerica.csv`: Phone codes for North American countries.
- `LatinAmerica.csv`: Phone codes for Latin American countries.
- `Australia.csv`: Phone codes for Australia.
- `Balcans.csv`: Phone codes for Balkan countries.
- `AllCountries.csv`: A single file that combines the data from all the regional files above for convenience.
- `generate_phone_number.py`: Python script to generate phone numbers.

---

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/Magnificent67/WorldPhoneNumberDataset.git
   cd WorldPhoneNumberDataset
   ```

2. Run the script:
   ```bash
   python generate_phone_number.py
   ```

3. Enter the country and city when prompted. The script will generate a realistic phone number.

---

## Example

**Input:**
```
Enter country: United States
Enter city or note: Los Angeles
```

**Output:**
```
+1 213 555-1234
```

---

## Future Plans

- Add more regions and data for smaller areas.
- Improve the phone number generation logic.
- Add validation for user inputs.

---

## License

This project is open-source and available under the MIT License. Feel free to use and modify it.

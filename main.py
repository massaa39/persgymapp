"""
This is the main module for generating advice based on user data.
"""

import csv
import sys
from advice_generator import create_advice

def load_user_data(csv_file):
    """
    Load user data from a CSV file.

    Args:
        csv_file: The path of the CSV file.

    Returns:
        A list of dictionaries containing user data.
    """
    user_data = []

    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user_data.append(row)

    return user_data

def main():
    """
    The main function for generating advice based on user data.
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py [CSV_FILE]")
        sys.exit(1)

    csv_file = sys.argv[1]
    user_data = load_user_data(csv_file)

    for user in user_data:
        advice = create_advice(user['age'], user['beauty_goals'], user['preferred_seniority'], user['medical_history'], user['training_goals'], user['medical_conditions'])
        print(f"{user['name']}さんへのアドバイス: {advice}\n")


if __name__ == "__main__":
    main()


from clean_numbers import clean_and_save
import pandas as pd

def print_cleaned_numbers():
    df = pd.read_excel('cleaned_phone_numbers.xlsx')
    print(df)

if __name__ == "__main__":
    clean_and_save()
    print_cleaned_numbers()

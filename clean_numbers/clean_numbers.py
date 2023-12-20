import pandas as pd

def clean_numbers(phone_numbers):
    cleaned_numbers = []
    for i in phone_numbers:
        i = str(i)
        gg = "".join(c for c in i if c.isdecimal())
        cleaned_numbers.append(gg)

    return cleaned_numbers

def clean_and_save():
    df = pd.read_excel('phone_numbers.xlsx', sheet_name='Worksheet')
    cleaned_numbers = clean_numbers(df['phone_number'])
    cleaned_df = pd.DataFrame({'cleaned_phone_number': cleaned_numbers})
    cleaned_df.to_excel('cleaned_phone_numbers.xlsx', index=False)

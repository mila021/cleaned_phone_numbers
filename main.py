import pandas as pd

df = pd.read_excel('phone_numbers.xlsx', sheet_name='Worksheet')
cleaned_numbers = []
for i in df['phone_number']:
    i = str(i)
    gg = "".join(c for c in i if c.isdecimal())
    cleaned_numbers.append(gg)
  
cleaned_df = pd.DataFrame({'cleaned_phone_number': cleaned_numbers})
cleaned_df.to_excel('cleaned_phone_numbers.xlsx', index=False)

df = pd.read_excel('cleaned_phone_numbers.xlsx')
print(df)

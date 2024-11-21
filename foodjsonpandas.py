import pandas as pd
import json
import random as rand

# Filepath to your JSON data
filepath1 = r'C:/Users/김태헌/Desktop/FOODFIGHTER/files/archive/train.json'

# Load the JSON data into a pandas DataFrame
foodData = pd.read_json(filepath1)

# Filter the data for each cuisine and sample 20 rows
mexican_foods = foodData[foodData['cuisine'] == 'mexican']
mexican_foods_sample = mexican_foods.sample(n=20, replace=False, random_state=2)

korean_foods = foodData[foodData['cuisine'] == 'korean']
korean_foods_sample = korean_foods.sample(n=20, replace=False, random_state=2)

chinese_foods = foodData[foodData['cuisine'] == 'chinese']
chinese_foods_sample = chinese_foods.sample(n=20, replace=False, random_state=2)

japanese_foods = foodData[foodData['cuisine'] == 'japanese']
japanese_foods_sample = japanese_foods.sample(n=20, replace=False, random_state=2)

thai_foods = foodData[foodData['cuisine'] == 'thai']
thai_foods_sample = thai_foods.sample(n=20, replace=False, random_state=2)

italian_foods = foodData[foodData['cuisine'] == 'italian']
italian_foods_sample = italian_foods.sample(n=20, replace=False, random_state=2)

# List of food samples for each cuisine
cuisine_samples = [
    ('Mexican', mexican_foods_sample),
    ('Korean', korean_foods_sample),
    ('Chinese', chinese_foods_sample),
    ('Japanese', japanese_foods_sample),
    ('Thai', thai_foods_sample),
    ('Italian', italian_foods_sample)
]

# Write data to Excel file with multiple sheets
with pd.ExcelWriter('foodData123.xlsx', engine='openpyxl', mode='a') as writer:
    for cuisine_name, cuisine_data in cuisine_samples:
        # Directly write the sample dataframe for each cuisine to a new sheet
        cuisine_data.to_excel(writer, sheet_name=cuisine_name, index=False)












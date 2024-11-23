import pandas as pd


file_path = "C:/Users/김태헌/Desktop/FOODFIGHTER/foodData123.xlsx"
data = pd.ExcelFile(file_path)


cuisines = []
for sheet in data.sheet_names:
  df = data.parse(sheet)
  df['cuisine'] = sheet.lower()
  cuisines.append(df)


combined_data = pd.concat(cuisines, ignore_index=True)


combined_data['ingredients'] = combined_data['ingredients'].apply(eval)
exploded_data = combined_data.explode('ingredients')


ingredient_counts = exploded_data.groupby(['ingredients', 'cuisine']).size().reset_index(name='count')
total_counts = ingredient_counts.groupby('ingredients')['count'].sum().reset_index(name='total_count')
ingredient_counts = ingredient_counts.merge(total_counts, on='ingredients')
ingredient_counts['indigenous_index'] = ingredient_counts['count'] / ingredient_counts['total_count']
print(ingredient_counts.head())


output_file_path = "C:/Users/김태헌/Desktop/FOODFIGHTER/foodData123.xlsx"




#export to excel as a new sheet
with pd.ExcelWriter(output_file_path, mode='a', engine='openpyxl') as writer:
    ingredient_counts.to_excel(writer, sheet_name='Ingredient_Analysis', index=False)


print("Exported ingredient_counts to a new sheet named 'Ingredient_Analysis'")
import pandas as pd


file_path = "foodData123.xlsx"
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


output_file_path = "foodData123.xlsx"


def calculate_cuisine_scores(row):
    ingredients = eval(row['Ingredients'])  # Convert string back to list
    scores = []
    for cuisine in ingredient_counts['cuisine'].unique():
        score = ingredient_counts[(ingredient_counts['Ingredients'].isin(ingredients)) & 
                                  (ingredient_counts['cuisine'] == cuisine)]['indigenous_index'].sum()
        scores.append(score)
    return scores

# Apply function to calculate scores for each food
combined_data['cuisine_scores'] = combined_data.apply(calculate_cuisine_scores, axis=1)
print(combined_data[['cuisine', 'cuisine_scores']].head())  # Inspect the scores
import pandas as pd

file_path = "foodData123.xlsx"

data = pd.read_excel(file_path, sheet_name="Ingredient_Analysis")

num_ingredients = int(input("How many ingredients does your food have? "))

ingredient_list = [] 


for i in range(num_ingredients):
    ingredient = input(f"Enter ingredient {i + 1}: ").strip().lower()
    ingredient_list.append(ingredient)

print("Ingredients entered:", ingredient_list)



cuisine_scores = {
    "mexican": 0,
    "korean": 0,
    "italian": 0,
    "japanese": 0,
    "chinese": 0,
    "thai": 0
}

for ingredient in ingredient_list:
    ingredient_data = data[data["ingredients"] == ingredient]
    if not ingredient_data.empty:
        for _, row in ingredient_data.iterrows():
            cuisine = row["cuisine"]
            indigenous_index = row["indigenous_index"]
            cuisine_scores[cuisine] += indigenous_index
    else:
        print(f"Ingredient '{ingredient}' not found in the dataset.")

# Step 5: Determine the predicted cuisine
predicted_cuisine = max(cuisine_scores, key=cuisine_scores.get)  # Find the cuisine with the highest score
print("Cuisine scores:", cuisine_scores)
print(f"The predicted cuisine is: {predicted_cuisine.capitalize()}")
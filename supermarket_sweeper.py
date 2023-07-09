import requests
from googlesearch import search

city = input('enter the city that you live in: ')
city = city[0].upper() + city[1:400000].lower()
state = input('enter the state you live in(two-letter abbreviation): ').upper()

def get_nutritional_info(food):
    api_key = 'SvGG20PtAZxEctE8ZYSDmJ2f0DE4a1y6lXavsFEU'
    base_url = 'https://api.nal.usda.gov/fdc/v1/'

    search_url = f'{base_url}foods/search'

    params = {
        'api_key': api_key,
        'query': food,
 }
    response = requests.get(search_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['totalHits'] > 0:
            food_item = data['foods'][0]
            nutrients = food_item['foodNutrients']
            calories = None
            protein = None
            macronutrients = None
            fiber = None

            for nutrient in nutrients:
                if nutrient['nutrientName'] == 'Energy':
                    calories = nutrient['value']
                elif nutrient['nutrientName'] == 'Protein':
                    protein = nutrient['value']
                elif nutrient['nutrientName'] == 'Fiber, total dietary':
                    fiber = nutrient['value']
                elif nutrient['nutrientName'] == 'Carbohydrate, by difference' or nutrient[
                    'nutrientName'] == 'Total lipid (fat)':
                    macronutrients = nutrient['value']

            if calories is not None and protein is not None and macronutrients is not None:
                overall_healthiness = "Healthy" if protein >= calories*.1 or macronutrients >= calories*.2 or fiber >= calories*.014 else "Unhealthy"

                print('------------------------------------------')
                print('NUTRITIONAL FACTS: ')
                print('------------------------------------------')
                print(f"Food Item: {food}")
                print(f"Calories: {calories}")
                print(f"Protein: {protein}")
                print(f"Other Macronutrients: {macronutrients}")
                print(f"Fiber: {fiber}")
                print(f"Healthiness: {overall_healthiness}")
                print('------------------------------------------')

            else:
                print("Nutritional information not found.")
        else:
            print("No results found.")
    else:
        print("Failed to search for the food item.")

# Example usage
food_item = input("Enter the food item: ")
get_nutritional_info(food_item)

print(' ')
food_prefer = input('Would you prefer organic food that is slightly cheaper, high quality organic food, or cheaper food?(ch, h, c): ')


if food_prefer == 'c':
    query_cheap = f"VERY cheap {food_item} near {city}, {state}"
    num_results = 3

    search_results = search(query_cheap, num_results=num_results)

    for result_cheap in search_results:
        print(result_cheap)

if food_prefer == 'h':
    query_exp = f"high quality organic {food_item} near {city}, {state}"
    num_results = 3

    search_results = search(query_exp, num_results=num_results)

    for result_exp in search_results:
        print(result_exp)

if food_prefer == 'ch':
    query_exp_org = f"cheap healthy organic {food_item} near {city}, {state}"
    num_results = 3

    search_results = search(query_exp_org, num_results=num_results)

    for result_exp_org in search_results:
        print(result_exp_org)
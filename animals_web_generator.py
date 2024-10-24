import json

# Load the data from the JSON file
with open('animals_data.json', 'r') as f:
    animals = json.load(f)


# Iterate through each animal and print the specified fields
for animal in animals:
    print(f"Name {animal.get('name', 'N/A')}")


    # Get the diet from the characteristics
    diet = animal.get('characteristics', {}).get('diet')
    if diet:
        print(f"Diet: {diet}")


    # Get the first location from the locations list
    locations = animal.get('locations', [])
    if locations:
        print(f"Location: {locations[0]}")
    

    # Get the type from the characteristics
    animal_type = animal.get('characteristics', {}).get('type')
    if animal_type:
        print(f"Type: {animal_type}")
    
    # Print a new line for better readability
    print()
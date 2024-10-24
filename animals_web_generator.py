import json

# Load the data from the JSON file
with open('animals_data.json', 'r') as f:
    animals = json.load(f)

# Generate a string with the animals' data
output = "" # Initialize an empty string


# Iterate through each animal and print the specified fields
for animal in animals:
    output += f"Name: {animal.get('name', 'N/A')}\n"


    # Get the diet from the characteristics
    diet = animal.get('characteristics', {}).get('diet')
    if diet:
        output += f"Diet: {diet}\n"


    # Get the first location from the locations list
    locations = animal.get('locations', [])
    if locations:
        output += f"Location: {locations[0]}\n"
    

    # Get the type from the characteristics
    animal_type = animal.get('characteristics', {}).get('type')
    if animal_type:
        output += f"Type: {animal_type}\n"
    
    # Add a newline for separation between animals
    output += "\n"

# Read the content of the HTML template
with open('animals_template.html', 'r') as template_file:
    template_content = template_file.read()

# Replace the placeholder with the animals' data
final_content = template_content.replace('__REPLACE_ANIMALS_INFO__', output)

# Write the new HTML content to a new file
with open('animals.html', 'w') as output_file:
    output_file.write(final_content)

print("HTML file generated successfully: animals.html")

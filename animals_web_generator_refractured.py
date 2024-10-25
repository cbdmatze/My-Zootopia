import json

def get_skin_types(animals):
    """Extracts unique skin_type values from the animals list."""
    skin_types = set()
    for animal in animals:
        skin_type = animal.get('characteristics', {}).get('skin_type', 'Unknown')
        skin_types.add(skin_type)
    return list(skin_types)

def serialize_animal(animal_obj):
    """Serialize a single animal object to HTML format."""
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj.get("name", "N/A")}</div>\n'
    output += '  <p class="card__text">\n'
    output += '    <ul class="animal-details">\n'

    # Get the first location from the locations list
    locations = animal_obj.get('locations', [])
    if locations:
        output += f'      <li class="animal-detail"><strong>Location:</strong> {", ".join(locations)}</li>\n'

    # Get the type from the characteristics
    animal_type = animal_obj.get('characteristics', {}).get('type')
    if animal_type:
        output += f'      <li class="animal-detail"><strong>Type:</strong> {animal_type}</li>\n'

    # Get the diet from the characteristics
    diet = animal_obj.get('characteristics', {}).get('diet')
    if diet:
        output += f'      <li class="animal-detail"><strong>Diet:</strong> {diet}</li>\n'
    
    output += '    </ul>\n'
    output += '  </p>\n'
    output += '</li>\n'
    
    return output

def main():
    """Main function to load animal data, get skin_type, and generate HTML output."""
    # Load the data from the JSON file
    with open('animals_data.json', 'r') as f:
        animals = json.load(f)

    # Get available skin types
    skin_types = get_skin_types(animals)
    print("Available skin types:")
    for i, skin_type in enumerate(skin_types, 1):
        print(f"{i}. {skin_type}")

    # Get user selection
    selected_index = int(input("Enter the number corresponding to the desired skin type: ")) - 1
    selected_skin_type = skin_types[selected_index]

    # Filter animals by selected skin type
    filtered_animals = [
        animal for animal in animals
        if animal.get('characteristics', {}).get('skin_type', 'Unknown') == selected_skin_type
    ]

    # Generate HTML content for filtered animals
    output = ""
    for animal_obj in filtered_animals:
        output += serialize_animal(animal_obj)

    # Read the content of the HTML template
    with open('animals_template.html', 'r') as template_file:
        template_content = template_file.read()

    # Replace the placeholder with the filtered animals' data
    final_content = template_content.replace('__REPLACE_ANIMALS_INFO__', output)

    # Write the new HTML content to a new file
    with open('animals.html', 'w') as output_file:
        output_file.write(final_content)

    print("HTML file generated successfully: animals.html")

if __name__ == "__main__":
    main()

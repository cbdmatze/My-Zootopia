import json

def load_data(file_path, is_json=True, encoding='utf-8'):
    """
    Loads data from a file. Can load JSON or text data based on the flag.
    
    Args:
        file_path (str): The path of the file to load.
        is_json (bool): Flag to indicate whether the file is JSON. Default is True.
        encoding (str): Encoding format for reading the file. Default is 'utf-8'.
    
    Returns:
        dict/list/str: The loaded data, either as JSON or plain text.
    """
    with open(file_path, 'r', encoding=encoding) as f:
        if is_json:
            return json.load(f)  # Load JSON data
        else:
            return f.read()  # Load plain text data

def save_data(file_path, data, is_json=False, encoding='utf-8'):
    """
    Saves data to a file. Can save JSON or text data based on the flag.
    
    Args:
        file_path (str): The path of the file to save to.
        data (dict/list/str): The data to be saved.
        is_json (bool): Flag to indicate whether the data should be saved as JSON. Default is False.
        encoding (str): Encoding format for writing the file. Default is 'utf-8'.
    """
    with open(file_path, 'w', encoding=encoding) as f:
        if is_json:
            json.dump(data, f, ensure_ascii=False, indent=4)  # Save as JSON
        else:
            f.write(data)  # Save as plain text

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

def get_user_skin_type_choice(skin_types):
    """Prompts the user to select a skin type."""
    print("Available skin types:")
    for i, skin_type in enumerate(skin_types, 1):
        print(f"{i}. {skin_type}")

    selected_index = int(input("Enter the number corresponding to the desired skin type: ")) - 1
    return skin_types[selected_index]

def filter_animals_by_skin_type(animals, selected_skin_type):
    """Filters the animals by the selected skin type."""
    return [
        animal for animal in animals
        if animal.get('characteristics', {}).get('skin_type', 'Unknown') == selected_skin_type
    ]

def generate_html_content(filtered_animals):
    """Generates HTML content for the filtered animals."""
    output = ""
    for animal_obj in filtered_animals:
        output += serialize_animal(animal_obj)
    return output

def main():
    """Main function to orchestrate the animal data loading, filtering, and HTML generation."""
    # Load animal data from JSON
    animals = load_data('animals_data.json')

    # Get available skin types and allow user to select one
    skin_types = get_skin_types(animals)
    selected_skin_type = get_user_skin_type_choice(skin_types)

    # Filter animals by the selected skin type
    filtered_animals = filter_animals_by_skin_type(animals, selected_skin_type)

    # Generate HTML content for the filtered animals
    html_content = generate_html_content(filtered_animals)

    # Load the HTML template
    template_content = load_data('animals_template.html', is_json=False)

    # Replace the placeholder with the filtered animals' data
    final_content = template_content.replace('__REPLACE_ANIMALS_INFO__', html_content)

    # Save the final HTML output
    save_data('animals.html', final_content, is_json=False)

if __name__ == "__main__":
    main()

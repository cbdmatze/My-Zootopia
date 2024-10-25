import requests
import urllib.parse # New import to handle URL encoding

API_KEY = '7jwjjEP5ZPpj6pCCP7uYSQ==pDdefjc6dsHR98Ub'
API_URL = 'https://api.api-ninjas.com/v1/animals?name='

def fetch_animal_data(animal_name):
    """
    Fetches animal data from the API based on the search term (currently 'Fox').

    Args: animal_name (str): The name of the animal to search for.
    
    Returns:
        list: A list of dictionaries containing animal data. Returns an empty list if the API request fails.
        """
    headers = {'X-Api-Key': API_KEY}
    # Properly encode the animal_name to be safe for URLs
    url = API_URL + urllib.parse.quote(animal_name)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve data:", response.status_code)
        return []


def serialize_animal(animal_obj):
    """
    Serializes a single animal object into an HTML list item format.
    
    Args:
        animal_obj (dict): Dictionary containing information about a single animal.
        
    Returns:
        str: An HTML string representing the serialized animal information.
        """
    output = '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj.get("name", "N/A")}</div>\n'
    output += '<p class="card__text"><ul class="animal-details">\n'

    # Add location if available
    if 'locations' in animal_obj and animal_obj['locations']:
        output += f'<li><strong>Location:</strong> {animal_obj ["locations"][0]}</li>\n'

    # Add characteristics if available
    if 'characteristics' in animal_obj:
        characteristics = animal_obj['characteristics']
        if 'diet' in characteristics:
            output += f'<li><strong>Diet:</strong> {characteristics["diet"]}</li>\n'
        if 'type' in characteristics:
            output += f'<li><strong>Type:</strong> {characteristics["type"]}</li>\n'
        if 'skin_type' in characteristics:
            output += f'<li><strong>Skin Type:</strong> {characteristics["skin_type"]}<li>\n'
        
        output += '</ul></p></li>\n'
        return output


def generate_html(animal_data):
    """
    Generates an HTML file with the provided animal data, ebedding it in a predefined template.
    
    Args:
        animal_data (list): List of dictionaries, each containing details about an animal.
    """

    # Read the HTML template
    with open('animals_template.html', 'r') as template_file:
        template_content = template_file.read()

    # Generate serialized output for each animal
    output = ''.join(serialize_animal(animal) for animal in animal_data)

    # Replace the placeholder in the template with the serialized animal data
    final_content = template_content.replace('__REPLACE_ANIMALS_INFO__', output)

    # write the final HTML content to a new file
    with open('animals_API.html', 'w') as output_file:
        output_file.write(final_content)
    
    print("Website was successfully generated: animals_API.html")


def main():
    """
    Main function to run the animal data fetching, processing, and HTML generation.
    """
    # Prompt the user to enter an animal name
    animal_name = input("Enter the name of an animal: ")

    # Fetch data from the API
    animal_data = fetch_animal_data(animal_name)

    # Check if data was successfully retrieved before generating HTML
    if animal_data:
        generate_html(animal_data)
    else:
        print("No data available to generate HTML.")


if __name__ == "__main__":
    main()

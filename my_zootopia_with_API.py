
import os
import requests
import urllib.parse
from dotenv import load_dotenv  # Import dotenv

load_dotenv()  # Load environment variables from .env file

API_KEY = os.getenv("API_NINJAS_API_KEY")
API_URL = 'https://api.api-ninjas.com/v1/animals?name='

def fetch_animal_data(animal_name):
    """
    Fetches animal data from the API based on the search term.

    Args:
        animal_name (str): The name of the animal to search for.
    
    Returns:
        list: A list of dictionaries containing animal data. Returns an empty list if the API request fails.
    """
    headers = {'X-Api-Key': API_KEY}
    url = API_URL + urllib.parse.quote(animal_name)
    response = requests.get(url, headers=headers)
    
    # Ensure the response encoding is correct
    response.encoding = 'utf-8'  # Explicitly set response encoding to UTF-8

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

    if 'locations' in animal_obj and animal_obj['locations']:
        output += f'<li><strong>Location:</strong> {animal_obj["locations"][0]}</li>\n'

    if 'characteristics' in animal_obj:
        characteristics = animal_obj['characteristics']
        if 'diet' in characteristics:
            output += f'<li><strong>Diet:</strong> {characteristics["diet"]}</li>\n'
        if 'type' in characteristics:
            output += f'<li><strong>Type:</strong> {characteristics["type"]}</li>\n'
        if 'skin_type' in characteristics:
            output += f'<li><strong>Skin Type:</strong> {characteristics["skin_type"]}</li>\n'
    
    output += '</ul></p></li>\n'
    return output


def generate_html(animal_data, animal_name):
    """
    Generates an HTML file with the provided animal data, embedding it in a predefined template.

    Args:
        animal_data (list): List of dictionaries, each containing details about an animal.
        animal_name (str): The name of the animal searched for, used in error message if no data is found.
    """

    # Use UTF-8 encoding when reading the template
    with open('animals_template.html', 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()

    if animal_data:
        output = ''.join(serialize_animal(animal) for animal in animal_data)
    else:
        output = f'<h2 style="color: red; text-align: center;">The animal "{animal_name}" was not found... Please ensure your spelling is correct. 😎</h2>'

    final_content = template_content.replace('__REPLACE_ANIMALS_INFO__', output)

    # Use UTF-8 encoding when writing the HTML output
    with open('animals_API.html', 'w', encoding='utf-8') as output_file:
        output_file.write(final_content)
    
    print("Website was successfully generated: animals_API.html")


def main():
    """
    Main function to run the animal data fetching, processing, and HTML generation.
    """
    animal_name = input("Enter the name of an animal: ")
    animal_data = fetch_animal_data(animal_name)
    generate_html(animal_data, animal_name)


if __name__ == "__main__":
    main()

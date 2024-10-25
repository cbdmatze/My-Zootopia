

# My-Zootopia

**My-Zootopia** is a Python-based web generator that dynamically creates a webpage displaying details about animals. Users can search for animals by name, and My-Zootopia retrieves animal information directly from the [API Ninjas Animals API](https://api-ninjas.com/api/animals). This project leverages Python, HTML, CSS, and web scraping to provide a smooth, interactive experience.

## Features

1. **Dynamic Animal Search**: Users can enter any animal name, and My-Zootopia will retrieve information for that animal from the API, displaying it on a generated webpage.
2. **API Integration**: Automatically connects to the API Ninjas Animals API to fetch up-to-date information about animals.
3. **Error Handling for Unavailable Animals**: If an animal name is not found in the API (e.g., a nonexistent name), the website will display a friendly error message, like:
    ```
    <h2>The animal "goadohjasgfas" doesn't exist.</h2>
    ```
4. **Responsive Design**: Each animal’s information is organized into sections, making it easy to read and visually appealing.
5. **PEP 8 Conformity**: The Python code follows PEP 8 guidelines with clear, organized functions and docstrings for maintainability.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/My-Zootopia.git
   cd My-Zootopia
   ```
2. Install dependencies (especially `requests` for API calls):
   ```bash
   pip install requests
   ```
3. Replace the `API_KEY` variable in `animals_web_generator.py` with your own API key from [API Ninjas](https://api-ninjas.com/register).

## Usage

## Setup API Key

Before running the program, set your API key as an environment variable:

**Mac/Linux:**
```bash
export API_NINJAS_API_KEY="your_api_key_here"



1. **Run the Program**:
   Execute the Python script to begin the process:
   ```bash
   python my_zootopia.py.py

   or:

   python my_zootopia_with_API.py
   ```
2. **Enter an Animal Name**:
   After running the script, you’ll be prompted to enter an animal name. Type in the animal you’re interested in, for example:
   ```
   Enter the name of an animal: Fox
   ```
3. **View the Generated Webpage**:
   After entering a valid animal name, a webpage will be generated with the retrieved information. Open `animals.html` or 'animals_API.html'  in your browser to view it.

### Example

For instance, entering `Fox` will display various species and details about foxes, while an unknown name will result in:
   ```
   <h2>The animal "unknownanimal" doesn't exist.</h2>
   ```

## Code Structure

- **`animals_web_generator.py`**: Main script handling the API fetch, HTML generation, and user input.
  - **`fetch_animal_data(animal_name)`**: Retrieves data from the API based on user input.
  - **`serialize_animal(animal_obj)`**: Formats the data for each animal into HTML-friendly content.
  - **`generate_html(animal_data, animal_name)`**: Creates and saves the HTML webpage, incorporating a friendly error message if no animals are found.
- **`animals_template.html`**: Template file containing placeholders for animal data, which is filled by `generate_html`.
- **`styles.css`**: CSS file styling the generated webpage.

## Dependencies

- **requests**: For making HTTP requests to the Animals API.
  
Install dependencies with:
```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any bugs or enhancements.

---

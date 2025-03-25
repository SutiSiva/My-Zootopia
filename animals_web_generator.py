import json
import webbrowser
import os

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

def search_animals(animals_data, search_term):
    """Searches the animal data for a search term."""
    results = []
    for animal in animals_data:
        if search_term.lower() in animal['name'].lower():
            results.append(animal)
    return results

def generate_html(results):
    """Generates HTML for the found animals."""
    html_content = '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
    html_content += '<meta charset="UTF-8">\n'
    html_content += '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    html_content += '<title>Search Results</title>\n'
    html_content += '<style>\n'
    html_content += 'body { font-family: Arial, sans-serif; }\n'
    html_content += '.cards { list-style: none; padding: 0; }\n'
    html_content += '.cards__item { border: 1px solid #ccc; margin: 10px; padding: 10px; border-radius: 5px; }\n'
    html_content += '.card__title { font-weight: bold; }\n'
    html_content += '</style>\n'
    html_content += '</head>\n<body>\n'
    html_content += '<h1>Search Results</h1>\n'
    html_content += '<ul class="cards">\n'

    for animal in results:
        html_content += '<li class="cards__item">\n'
        html_content += f'<div class="card__title">{animal["name"]}</div>\n'
        html_content += '<p class="card__text">\n'
        html_content += f'<strong>Diet:</strong> {animal["characteristics"].get("diet", "N/A")}<br/>\n'
        html_content += f'<strong>Location:</strong> {", ".join(animal["locations"])}<br/>\n'
        html_content += f'<strong>Type:</strong> {animal["characteristics"].get("type", "N/A")}<br/>\n'
        html_content += '</p></li>\n'

    html_content += '</ul>\n</body>\n</html>'
    return html_content

def main():
    animals_data = load_data('animals_data.json')

    while True:
        # Prompt for search term
        search_term = input("Enter the name of the animal you want to search for (or type 'exit' to quit): ")

        if search_term.lower() == 'exit':
            print("Exiting the search.")
            break

        # Search for animals
        results = search_animals(animals_data, search_term)

        # Output results
        if results:
            print(f"Found animals for '{search_term}':")
            for animal in results:
                print(f"Name: {animal['name']}, Diet: {animal['characteristics'].get('diet', 'N/A')}, Location: {', '.join(animal['locations'])}, Type: {animal['characteristics'].get('type', 'N/A')}")

            # Generate HTML and write to file
            html_output = generate_html(results)
            with open('animals.html', 'w') as output_file:
                output_file.write(html_output)
            print(f"The search results have been saved to 'animals.html'.")

            # Open the HTML file in the default web browser
            webbrowser.open('file://' + os.path.realpath('animals.html'))
        else:
            print(f"No animals found for '{search_term}'. Please try again.")

if __name__ == "__main__":
    main()
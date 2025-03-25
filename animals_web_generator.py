import json


def load_data(filename):
    with open(filename, 'r') as handle:
        return json.load(handle)


def generate_website(animals_data):
    html_content = "<html><head><title>My Animal Repository</title></head><body>"
    html_content += "<h1>My Animal Repository</h1><ul>"

    for animal in animals_data:
        html_content += f"<li><h2>{animal['name']}</h2>"
        html_content += f"<p><strong>Diet:</strong> {animal['diet']}</p>"
        html_content += f"<p><strong>Location:</strong> {animal['location']}</p>"
        if 'type' in animal:
            html_content += f"<p><strong>Type:</strong> {animal['type']}</p>"
        html_content += "</li>"

    html_content += "</ul></body></html>"

    with open("animals.html", "w") as file:
        file.write(html_content)


if __name__ == "__main__":
    animals_data = load_data('animals_data.json')
    generate_website(animals_data)
    print("Website was successfully generated to the file animals.html.")""
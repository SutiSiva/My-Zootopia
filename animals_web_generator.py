import data_fetcher


def generate_website(animal_data, animal_name):
    if not animal_data:
        with open("animals.html", "w") as file:
            file.write(f"<h2>The animal '{animal_name}' doesn't exist.</h2>")
        return

    # Generate the HTML content for the animals
    html_content = "<h1>Animal Information</h1><ul>"
    for animal in animal_data:
        html_content += f"<li><h2>{animal['name']}</h2></li>"
        # Add more details as needed
    html_content += "</ul>"

    # Write to the HTML file
    with open("animals.html", "w") as file:
        file.write(html_content)


if __name__ == "__main__":
    animal_name = input("Please enter an animal: ")
    data = data_fetcher.fetch_data(animal_name)

    generate_website(data, animal_name)
    print("Website was successfully generated to the file animals.html.")
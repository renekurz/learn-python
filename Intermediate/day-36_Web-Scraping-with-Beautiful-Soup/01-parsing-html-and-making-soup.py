from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(f"soup.title: {soup.title}")
print(f"soup.title.name: {soup.title.name}")
print(f"soup.title.string: {soup.title.string}\n")

print(f"soup:\n{soup}\n")
print(f"soup.prettify():\n{soup.prettify()}\n")

print(f"soup.p: {soup.p}")
print(f"soup.find_all(name=\"p\"):\n{soup.find_all(name="p")}\n")

for tag in soup.find_all(name="p"):
    print(f"tag.getText():\n{tag.getText()}")

    # You can also get only the links, if you do this:
    # tag.get("href")
    # I don't have any links in my html file

print(f"\nsoup.find(name=\"h3\", id=\"best_film\"): {soup.find(name="h3", id="best_film")}\n")
print(f"soup.find(name=\"p\", class=\"second_best_film_description\"):\n{soup.find(name="p", class_="second_best_film_description")}")
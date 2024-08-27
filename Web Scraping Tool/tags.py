import requests
from bs4 import BeautifulSoup

with open("sample.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, "html.parser")

# print(soup.prettify())
# print(soup.title)
# print(soup.title.string)
# print(soup.title.string, type(soup.title.string))

# print(soup.div)
# print(soup.find_all("div"))
# print(soup.find_all("div")[0])
# print(type(soup.find_all("div")[0]))

# for link in soup.find_all("a"):
#     print(link.string)
#     print(link)
#     print(link.get("href"))

# for link in soup.find_all("a"):
#     print(link.get_text())

# s = soup.find(id = "link3")
# print(s)
# print("--------")
# print(s.get("href"))

# print(soup.select("div.italic"))
# print(soup.select("div.italic")[0])
# print(soup.select("span#italic"))

# return 1st span class
# print(soup.span.get("class"))

# print(soup.find(id = "italic"))

# print(soup.find(class_ = "italic"))

# for child in soup.find_all(class_ = "container"):
#     print(child)

# for parent in soup.find(class_="box").parents:
#     print(parent)
#     break

# Modifying
# cont = soup.find(class_ = "container")
# cont.name = "span"
# cont["class"] = "class1 class2"
# cont.string = "Content changed"
# print(cont)

# Add new tags
# ulTag = soup.new_tag("ul")

# liTag = soup.new_tag("li")
# liTag.string = "Home"
# ulTag.append(liTag)

# liTag = soup.new_tag("li")
# liTag.string = "About"
# ulTag.append(liTag)

# soup.html.body.insert(0, ulTag)

# with open("modified.html", "w") as f:
#     f.write(str(soup))

# cont = soup.find(class_ = "container")
# print(cont.has_attr("id")) #False
# print(cont.has_attr("class")) #True
# print(cont.has_attr("contenteditable")) #True


# def has_class_but_not_id(tag):
#     return tag.has_attr("class") and not tag.has_attr("id")

# result = soup.find_all(has_class_but_not_id)
# print(result)

def has_content(tag):
    return tag.has_attr("content")
result = soup.find_all(has_content)
print(result)
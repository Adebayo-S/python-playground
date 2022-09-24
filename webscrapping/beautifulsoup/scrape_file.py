from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# print(doc.prettify()) use prettify to print the html with the indentation
tag = doc.title # get the title tag (only gets the first occurence)
print(tag)
tag.string = "hello" # set the innerText to hello
tag = doc.find("a") # also gives the first occurence of an <a> tag
tags = doc.find_all("a") # gives all occurence of <a> tags
first_a_tag = doc.find_all("a")[0] # finds the first <a> tag
print(first_a_tag.find_all("b")) # prints all the <b> tags in the first <a> tag

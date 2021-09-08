title = input()
print(f"<h1>\n\t{title}\n</h1>")

content = input()
print(f"<article>\n\t{content}\n</article>")

comments = input()

while not comments == "end of comments":
    print(f"<div>\n\t{comments}\n</div>")
    comments = input()

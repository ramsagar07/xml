def main():
    import builtins as b
    import xml.etree.ElementTree as X
    import pandas as pd
    number = int(input("enter no of entries"))
    root = X.Element("movie_info")
    for i in range(0, number):
        book = X.SubElement(root, "movie")
        name = input("enter movie name")
        book.set("Name", name)
        director = input("enter director name")
        book.set("Director", director)
        hero = input("enter hero name")
        book.set("Hero", hero)
    tree = X.ElementTree(root)
    tree.write('movie.xml')
    data = pd.read_xml("movie.xml")
    b.print(data)


main()

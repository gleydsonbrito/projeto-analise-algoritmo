import xml.etree.ElementTree as et

tree = et.parse('brazil58.xml')
root = tree.getroot()

print(root.tag)

graph = {}

print(graph)


def load():
    i = 1
    for k in range(len(root)):
        print("Cidade: {}".format(i))
        for child in root[i-1]:
            print(child.attrib)
        i = i + 1


load()

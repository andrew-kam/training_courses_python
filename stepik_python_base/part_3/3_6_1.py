from xml.etree import ElementTree

input_str = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'
tree = ElementTree.fromstring(input_str)
colors = {'red': 0, 'green': 0, 'blue': 0}
# tree = ElementTree.fromstring(input())


def getchildren(root, level):
    level += 1
    for child in root:
        colors[child.attrib['color']] += level
        getchildren(child, level)


# print(tree.attrib['color'])
colors[tree.attrib['color']] += 1


getchildren(tree, 1)

print(*colors.values())

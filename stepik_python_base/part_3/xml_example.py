from xml.etree import ElementTree


tree = ElementTree.parse("example.xml")
root = tree.getroot()

print(root)
print(root.tag, root.attrib)

for child in root:
    print(child.tag, child.attrib)

print(root[0][0].text)

for element in root.iter('scores'):  # findall - только среди детей
    score_sum = 0
    for child in element:
        score_sum += float(child.text)
    print(score_sum)


'''
tree = ElementTree.parse("example.xml")
root = tree.getroot()
tree.write('example_copy2.xml')
'''

# tree = ElementTree.parse("example_modified.xml")
# tree = ElementTree.parse("example.xml")
# root = tree.getroot()
# greg = root[0]
# module1 = next(greg.iter("module1"))
# print(module1, module1.text)
# module1.text = str(float(module1.text) + 30)

# certificate = greg[2]
# certificate.set("type", "with distinction")

# description = ElementTree.Element("description")
# description.text = "Showed excellent skills during the course"
# greg.append(description)

# description = greg.find("description")
# greg.remove(description)

# tree.write("example_modified.xml")
# print(ElementTree.ElementTree.__doc__)














# use root = ElementTree.fromstring(string_xml_data) to parse from str

# print(root)
# print(root.tag, root.attrib)

# print(root[0][0].text)

# for child in root:
#     print(child.tag, child.attrib)

# for element in root.iter("scores"):  # .findall for children
#     score_sum = 0
#     for child in element:
#         score_sum += float(child.text)
#     print(score_sum)

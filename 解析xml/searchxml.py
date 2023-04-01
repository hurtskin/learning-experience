import xml.etree.cElementTree as ET
import STLink


def dict_to_list(temp_dict):
    temp_list = []
    for key, val in temp_dict.items():
        temp_list.append([key, val])
    return temp_list


def get_all(father):
    xml_strcture = []
    for child in father:
        attrib_list = dict_to_list(child.attrib)
        tag_name = child.tag
        xml_strcture.append([tag_name, attrib_list])

        children = get_all(child)
        if len(children) != 0:
            for item in children:
                xml_strcture.append(item)

    return xml_strcture


def get_xml_content(path):
    tree = ET.parse(path)
    root = tree.getroot()
    xml_structure = get_all(root)
    return xml_structure
    # tag = root.tag()
    # tag_name = list
    # attrib_list = list
    # temp = list
    # for tag in root:
    #     tag_name.append(list(tag.tag))
    #
    # return


if __name__ == '__main__':
    temp = get_xml_content("home.xml")
    print(temp)
    temp2 = []
    new_linklist = STLink.SList()
    for xml_tag in temp:
        print(xml_tag)
        new_linklist.append(xml_tag)

    length = new_linklist.length()
    print(length)
    for item in new_linklist.travel():
        print(item)





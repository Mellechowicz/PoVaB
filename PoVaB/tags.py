import defusedxml.ElementTree as ET

class Tags(dict):
    """
        Container for calculation tags
    """
    def __init__(self,vasprun):
        incar = ET.parse(vasprun).getroot().find('incar')
        for tag in incar.findall('i'):
            if 'name' not in tag.attrib:
                continue
            if 'type' in tag.attrib:
                self[tag.attrib['name']] = Tags.translate_xml2py(tag.attrib['type'],tag.text)

    @staticmethod
    def translate_xml2py(convert_type,value):
        if convert_type == 'int':
            return int(value)
        elif convert_type == 'logical':
            return True if 'T' in value else False
        else:
            return value

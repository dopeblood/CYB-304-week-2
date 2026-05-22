import xml.etree.ElementTree as ET

data = """
<student>
    <name>Ada</name>
    <department>Cybersecurity</department>
</student>
"""

root = ET.fromstring(data)

print(root.find('name').text)
import pandas as pd
import xml.etree.ElementTree as ET
root = ET.Element("Employee_Details")
book = ET.SubElement(root, "Employee")
name = ET.SubElement(book, "Name")
name.text = "Kiran"
place = ET.SubElement(book, "Place")
place.text = "Hyderabad"
salary = ET.SubElement(book, "Salary")
salary.text = "30,000/-"
book = ET.SubElement(root, "Employee")
name = ET.SubElement(book, "Name")
name.text = "Mahesh"
place = ET.SubElement(book, "Place")
place.text = "Banglore"
salary = ET.SubElement(book, "Salary")
salary.text = "80,000/-"
tree = ET.ElementTree(root)
tree.write("e.xml")
s = pd.read_xml('e.xml')
print(s)

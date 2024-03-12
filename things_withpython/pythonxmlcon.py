from xml.dom import minidom 
import os


root =  minidom.Document()

xml=  root.createElement('root')
root.appendChild(xml)
productchild = root.createElement('product')

productchild.setAttribute('name', 'geeks')

xml.appendChild(productchild)

childschild =root.createElement('tati')
childschild.setAttribute('type','killer')
productchild.appendChild(childschild)
chichild = root.createElement('big')

childschild.appendChild(chichild)
savepath= "xmlfile.xml"
xml_str= root.toprettyxml(indent="\t")

with open(savepath,"w") as f:
    f.write(xml_str)

print(productchild)
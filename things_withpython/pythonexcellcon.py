import pandas  as pd

data= pd.read_excel("excell.xlsx")

print(data.to_xml)
f= open('nik.xml','w')
f.write(str(data.to_xml))

f.close()



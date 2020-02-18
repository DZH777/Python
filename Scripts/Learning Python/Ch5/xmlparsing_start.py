# 
# Example file for parsing and processing XML
#
import xml.dom.minidom

def main():
  # use the parse() function to load and parse an XML file
  doc = xml.dom.minidom.parse("samplexml.xml")
  
  # print out the document node and the name of the first child tag
  print(doc.nodeName)
  print(doc.firstChild.tagName)
  
  # get a list of XML tags from the document and print each one
  skills = doc.getElementsByTagName("skill")
  print("%d skills: " % skills.length)
  for i, skill  in enumerate(skills):
    print("\t",i+1,skill.getAttribute("name"))

  # create a new XML tag and add it into the document
  newsSkill = doc.createElement("skill")
  newsSkill.setAttribute("name","Oracle")
  doc.firstChild.appendChild(newsSkill)

  skills = doc.getElementsByTagName("skill")
  print("%d skills: " % skills.length)
  for i, skill  in enumerate(skills):
    print("\t",i+1,skill.getAttribute("name"))

if __name__ == "__main__":
  main();


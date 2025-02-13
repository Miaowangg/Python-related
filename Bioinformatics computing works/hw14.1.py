import xml.etree.ElementTree as ET
import urllib.request

thefile = urllib.request.urlopen('http://www.uniprot.org/uniprot/Q9H400.xml')
document = ET.parse(thefile)
root = document.getroot()

ns = '{http://uniprot.org/uniprot}'

entry = root.find(ns + 'entry')

if entry is not None:
    
    for reference in entry.findall(ns + 'reference'):
        citation = reference.find(ns + 'citation')
        if citation is None:
            continue
        
        #title
        title_ele = citation.find(ns + 'title')
        if title_ele is not None:
            title = title_ele.text
        else: 'No title'

        #journal name
        journal = citation.get('name', 'No Journal')
        #date
        date = citation.get('date', 'No Date')
        #author list
        author_list = citation.find(ns + 'authorList')
        authors = []

        if author_list is not None:
            # person
            for person in author_list.findall(ns + 'person'):
                authors.append(person.get('name', 'Unknown Author'))
            
            # consortium
            for consortium in author_list.findall(ns + 'consortium'):
                authors.append(consortium.get('name', 'Unknown Consortium'))
      
        # Print out the results
        print("Title:", title)
        print("Journal:", journal)
        print("Date:", date)
        print("Authors:", ", ".join(authors))
        print()

''' HW 14.1 question
Write a program to pick out, and print, the references of 
a XML format UniProt entry, in a nicely formatted way.
'''












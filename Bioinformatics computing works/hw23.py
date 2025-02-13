import sqlite3
import sys

conn = sqlite3.connect('taxa.db3')
c = conn.cursor()

user_input = sys.argv[1]

#join
c.execute("""
    SELECT name.name, taxonomy.scientific_name 
    FROM taxonomy, name 
    WHERE taxonomy.tax_id = name.tax_id 
      AND name.name = ?;
""", (user_input,))

result = c.fetchone()
#print(result)

if result:
    print("Organism Name: {}".format(result[0]))
    print("Scientific Name: {}".format(result[1]))
else:
    print("No scientific name found for the given organism.")

conn.close()  



    



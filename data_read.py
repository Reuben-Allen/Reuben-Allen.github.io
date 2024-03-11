"""
This script contains functions to read and display 
gut metabolite data files in JSON format.
"""

import json
from pyscript import document

class Database():
    def __init__(self, filename):
        # initialize database from json file
        with open(filename, 'r') as openfile:
            self.metabolite_data = json.load(openfile)
        
        # obtain a list of different metabolites in the database
        self.metabolite_names = []
        for metabolite in self.metabolite_data["metabolites"]:
            if isinstance(metabolite["name"], list):
                for name in metabolite["name"]:
                    self.metabolite_names.append(name)
            else:
                self.metabolite_names.append(metabolite["name"])
        self.metabolite_CAS = [metabolite["CAS"] for metabolite in self.metabolite_data["metabolites"]]

        # declare variable to store search results
        self.result = 0

    def display(self):
        # return a list of items in the database
        display_str = ""
        for metabolite in self.metabolite_data["metabolites"]:
            if type(metabolite["name"]) == list:
                display_str = display_str + "{0} {1}".format(metabolite["name"][0],metabolite["CAS"]) + """
"""
            else:
                display_str = display_str + "{0} {1}".format(metabolite["name"],metabolite["CAS"]) + """
"""
        return display_str

    def info(self):
        # returns information about the metabolite stored in self.result

        functions = ""
        for i in self.result["functions/associations"]:
            functions = functions + "*" + i + """
"""
        producers = ""
        for j in sorted(self.result["producers"]):
            producers = producers + "*" + j + """
"""
        bibliography = ""
        for k in self.result["bibliography"]:
            bibliography = bibliography + "[{0}] \"{1}\" In: {2} ({3}). DOI: {4}".format(k,
                                                                self.result["bibliography"][k]["title"],
                                                                self.result["bibliography"][k]["journal"],
                                                                self.result["bibliography"][k]["year"],
                                                                self.result["bibliography"][k]["doi"],) + """
"""
        output_str = """

Metabolite: """ + ','.join(self.result["name"]) + """
CAS: """ + self.result["CAS"] + """
Class: """ + self.result["class"] + """

Functions/Associations: 
""" + functions +"""

Select Producers: 
""" + producers +"""

Sources: 
""" + bibliography
        return output_str

    def class_info(self):
        # return infromation about the metabolite class contained in self.result
        info = ""
        for x in self.result["information"]:
            info = info + "*" + x + """
"""
        bibliography = ""
        for k in self.result["bibliography"]:
            bibliography = bibliography + "[{0}] \"{1}\" In: {2} ({3}). DOI: {4}".format(k,
                                                                self.result["bibliography"][k]["title"],
                                                                self.result["bibliography"][k]["journal"],
                                                                self.result["bibliography"][k]["year"],
                                                                self.result["bibliography"][k]["doi"],) + """
"""
        output_str = """

Metabolite Class: """ + self.result["name"] + """

Information :
""" + info + """

Sources: 
""" + bibliography
        return output_str
    
    def search(self, query):
        # search the database based on CAS or name and display info. 
        # then stores the metabolite info for subsequent access.

        if query == "ls":
            return self.display()
        elif query.split("_")[0] == "class":
            class_query = query.split("_")[1]
            for metabolite_class in self.metabolite_data["classes"]:
                if class_query == metabolite_class["name"]:
                    self.result = metabolite_class
                    return self.class_info()
                else:
                    continue
            return "Class not found in database."
        elif query in self.metabolite_CAS:
            for metabolite in self.metabolite_data["metabolites"]:
                if query == metabolite["CAS"]:
                    self.result = metabolite
                    return self.info()
                else:
                    continue
        elif query in self.metabolite_names:
            for metabolite in self.metabolite_data["metabolites"]:
                if query in metabolite["name"]:
                    self.result = metabolite
                    return self.info()
                else:
                    continue
        else:
            return "Metabolite not found in database."

def search_input(event):
    input_text = document.querySelector("#english")
    english = input_text.value.lower()
    output_div = document.querySelector("#output")
    output_div.innerText = data.search(english)

if __name__=="__main__":
  data = Database("data/metabolite_database.json")

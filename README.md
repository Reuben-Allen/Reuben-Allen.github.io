# Microbiome-Gut-Brain Axis Metabolite Database
A database for the facile storage and retrieval of information about metabolites relevant to the microbiome-gut-brain axis.

### Usage
The database can be accessed primarily through the website <https://reuben-allen.github.io> by simple typing commands into the entry box and clicking the "Search" button. Any metabolite can be accessed according to its CAS ID or by name. For entry by name, the search is not case-sensetive, and certain metabolites will accept multiple name inputs (e.g. acetic acid may be retrieved by typing "acetic acid", "ethanoic acid", or "acetate"). Other commands are also available. For example, searching "ls" will provide a list of all the metabolites currently entered in the database. Additionally, different classes of metabolites can be searched for using the "class_" prefix (e.g. searching "class_short chain fatty acid" will retrienve info about this class in general). 

The database may also be accessed directly through the python script.

### Database structure
The metabolite information is stored in a efficient and human-interpretable format of JavaScript Object Notation (JSON, see <https://www.json.org/json-en.html> for more information). The overall organizational structure is as follows:
```
{
    "metabolites": [
        {
            "name": ["name1","name2"],
            "CAS": "CAS_ID",
            "class": "classname",
            "producers": ["Producer from source 1 [1]","Producer from source [2]"],
            "functions/associations": ["Info from source 1 [1].","Info from source 2 [2]"],
            "bibliography": {
                "1": {
                    "title":"Title1",
                    "journal":"Journal1",
                    "year":"year1",
                    "doi":"doi1"
                },
                "2": {
                    "title":"Title2",
                    "journal":"Journal2",
                    "year":"year2",
                    "doi":"doi2"
                }
            }
        },
            "name": ["name1","name2"],
            "CAS": "CAS_ID",
            "class": "classname",
            "producers": ["Producer from source 1 [1]","Producer from source [2]"],
            "functions/associations": ["Info from source 1 [1].","Info from source 2 [2]"],
            "bibliography": {
                "1": {
                    "title":"Title1",
                    "journal":"Journal1",
                    "year":"year1",
                    "doi":"doi1"
                },
                "2": {
                    "title":"Title2",
                    "journal":"Journal2",
                    "year":"year2",
                    "doi":"doi2"
                }
            }
        },
    ],
    "classes": [
        {
            "name": "classname",
            "information": ["Info from source 1 [1].","Info from source 2 [2]"],
            "bibliography": {
                "1": {
                    "title":"Title1",
                    "journal":"Journal1",
                    "year":"year1",
                    "doi":"doi1"
                },
                "2": {
                    "title":"Title2",
                    "journal":"Journal2",
                    "year":"year2",
                    "doi":"doi2"
                }
            }
        }
    ]
}
```

### Example
Let's say I wish to search a metabolite database titled "metabolite_database.json" for information about the saccarolytic fermentation product acetate directly with the python script.
```
# First load the data_read.py file into your python script
from data_read import Database

# Generate a class object for the database
data = Database("metabolite_database.json")

# View the results for acetate
print(data.search("acetate))
```

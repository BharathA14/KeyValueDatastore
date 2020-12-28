# KeyValueDatastore
## Table of contents
* [General info](#general-info)
* [Usage](#Usage)
* [Workflow](#workflow)

## General info
* This project is a simple Key-Value based datastore that supports the basic CRD(Create,Read and Delete) operations.
* Additional functionalities include a Time-to-live property (optional usage) where the user can set an expiry limit before which we must perform read and delete operations on the key. Basically, **Snapchat for CRD operations**. 
* Project does not have any additional dependencies apart from those packaged within the standard Python 3.6+ package. 

## Usage
```
from key_value import *

#Create an object 
x = CRD()

#Add a key-value to the JSON

x.create("Varun", 21)

#Read values 

x.read("Varun")

#Delete Values

x.delete("Varun")
```



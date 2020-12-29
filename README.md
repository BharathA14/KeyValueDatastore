# KeyValueDatastore
## Table of contents
* [General info](#general-info)
* [Usage](#Usage)
* [Workflow](#workflow)

## General info
* This project is a simple Key-Value based datastore that supports the basic CRD(Create,Read and Delete) operations.
* Additional functionalities include a Time-to-live property (optional usage) where the user can set an expiry limit before which we must perform read and delete operations on the key. 
* You need mongo configured on the device on which acts as the server. 

## Usage
```
from keyvalue

#Create an object 
x = keyvalue.CRD('keyValue','keyValuse')  '''The database and the collection name'''

#Add a key-value to the JSON

x.insert("Varun", 21)

#Read values 

x.read("Varun")

#Delete Values

x.delete("Varun")
```


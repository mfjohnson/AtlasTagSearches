# Overview
This project contains examples for how to manage Apache Atlas Tag Searches using the REST API.  The project is produced using Python 2.7.  Though you should be able to analyze the code and apply it for your preferred REST API query tool.
 
# Requirements
* Python 2.7 (I have only tested it on 2.7 running on both MacOS and Centos 7)
* Python packages:
  * requests
  * json
  
# Running the example
1. Modify the properties at the top of the SimpleAtlasTagSearch.py file
1. run the following command:
`python SimpleAtlasTagSearch.py`

If successful you will see a list of all entities assigned to TAG_NAME specified in the properties at the top of the program.
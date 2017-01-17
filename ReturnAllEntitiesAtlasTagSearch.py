import requests
import json

#------- MODIFY THESE PROPERTIES TO RUN THIS EXAMPLE ON YOUR ATLAS INSTANCE

ATLAS_DOMAIN="server1"  # The same http URL to access the Atlas UI
ATLAS_PORT="21000"      # The same port used to access the Atlas UI
TAG_NAME="CUSTOMER"     # The Atlas Tag to search for assigned entities

#-------------------------------------------------------------------------

def atlasGET( restAPI ) :
    url = "http://"+ATLAS_DOMAIN+":"+ATLAS_PORT+restAPI
    r= requests.get(url, auth=("admin", "admin"))
    return(json.loads(r.text));


results = atlasGET("/api/atlas/discovery/search/dsl?query={0}".format(TAG_NAME))
entityGuidList = results['results']

entityList = []
for entity in entityGuidList:
    guid = entity['instanceInfo']['guid']
    entityDetail = atlasGET("/api/atlas/entities/{0}".format(guid))
    entityList.append(entityDetail);

print json.dumps(entityList, indent=4, sort_keys=True)
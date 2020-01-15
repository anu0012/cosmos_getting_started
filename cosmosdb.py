import azure.cosmos.cosmos_client as cosmos_client
config = {
	    'ENDPOINT': 'https://YOUR_DB_NAME.documents.azure.com:443/',
	    'PRIMARYKEY': 'PRIMARY_KEY',
	    'DATABASE': 'CosmosDatabase'
	}

# Initialize the Cosmos client
client = cosmos_client.CosmosClient(url_connection=config['ENDPOINT'], auth={
                                    'masterKey': config['PRIMARYKEY']})

#create db
try:
    db = client.CreateDatabase({'id': config['DATABASE']})
    db_link = db['_self']
except Exception as e:
    # if DB is already there
    db_id = config['DATABASE']
    db_query = "select * from r where r.id = '{0}'".format(db_id)
    db = list(client.QueryDatabases(db_query))[0]
    db_link = db['_self']

# Create container options
options = {
    'offerThroughput': 10000
}

container_definition = {
    'id': collection_name
}

try:
    # Create a container
    container = client.CreateContainer(db_link, container_definition, options)
    coll_link = container['_self']
except Exception as e:
    # if collection is already there
    coll_id = collection_name
    coll_query = "select * from r where r.id = '{0}'".format(coll_id)
    coll = list(client.QueryContainers(db_link, coll_query))[0]
    coll_link = coll['_self']

#insert data
document = {
    'id': 1,
    'name': 'test_data',
    'description': 'Container Item'
}
client.CreateItem(coll_link, document)

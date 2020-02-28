import azure.cosmos.cosmos_client as cosmos_client

class CosmosClient:
    def __init__(self):
        self.config = {
            'ENDPOINT': 'your endpoint',
            'PRIMARYKEY': 'your cosmosdb primary key',
            'DATABASE': 'your db',
            'CONTAINER': 'your container'
        }
        options = {
            'offerThroughput': 400  
        }
        container_definition = {
            'id': self.config['CONTAINER']
        }

        # Initialize the Cosmos client
        self.client = cosmos_client.CosmosClient(url_connection=self.config['ENDPOINT'], auth={
            'masterKey': self.config['PRIMARYKEY']})

        self.db = {'id': 'your db', '_rid': '3WcMAA==', '_self': 'dbs/3WcMAA==/', '_etag': '"00008701-0000-0000-0000-5c17324f0000"', '_colls': 'colls/', '_users': 'users/', '_ts': 1545024079}

        self.container = {'id': 'your container', 'indexingPolicy': {'indexingMode': 'consistent', 'automatic': True, 'includedPaths': [{'path': '/*', 'indexes': [{'kind': 'Range', 'dataType': 'Number', 'precision': -1}, {'kind': 'Hash', 'dataType': 'String', 'precision': 3}]}], 'excludedPaths': []}, '_rid': '3WcMALwdAY4=', '_ts': 1545024080, '_self': 'dbs/3WcMAA==/colls/3WcMALwdAY4=/', '_etag': '"00008901-0000-0000-0000-5c1732500000"', '_docs': 'docs/', '_sprocs': 'sprocs/', '_triggers': 'triggers/', '_udfs': 'udfs/', '_conflicts': 'conflicts/'}

    def getLeaderBoard(self):
        options = {}
        options['enableCrossPartitionQuery'] = False
        options['maxItemCount'] = 100
        query = {'query': 'SELECT * FROM server s'}

        results = self.client.QueryItems(self.container['_self'], query, options)

        for result in results:
            print(result['message'])


    def pushData(self,username,highscore):
        data = self.client.CreateItem(self.container['_self'], {
            "username": str(username),
            "highscore": str(highscore),
            "message" : str(username) + " got " + str(highscore)
        })

        self.getLeaderBoard()
    
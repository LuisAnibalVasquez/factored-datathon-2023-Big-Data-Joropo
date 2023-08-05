import logging
from azure.eventhub import EventHubConsumerClient
import json

#Our connection string
connectionStr = 'Endpoint=sb://factored-datathon.servicebus.windows.net/;SharedAccessKeyName=datathon_group_1;SharedAccessKey=2GETvVt0FxyM0bo0Qau4inlmC/w3t4Uut+AEhAnAEgk=;EntityPath=factored_datathon_amazon_reviews_1'

#Access Data
consumerGroup = 'big_data_joropo'
eventhubName = 'factored_datathon_amazon_reviews_1'

#Starting the EventHub Client
client = EventHubConsumerClient.from_connection_string(connectionStr, consumerGroup, eventhub_name=eventhubName)

#Some log to see the events
logger = logging.getLogger("azure.eventhub")
logging.basicConfig(level=logging.INFO)

#Defining the event function
def onEvent(partitionContext, event):

    #Some logs
    logger.info("Received event from partition {}".format(partitionContext.partition_id))
    logger.info(event)

    #Saving the events (data) into a json
    event_data = event.body_as_json()
    with open("event_data_formated.json", "a") as f:
        f.write(json.dumps(event_data))
        f.write("\n")
    partitionContext.update_checkpoint(event)

#Opening with the EventHub client
with client:
    client.receive(on_event=onEvent)
import json
import os
from nightwatch import Nightwatch
from kafkawrapper import sendData

from dotenv import load_dotenv
load_dotenv()

nightwatch = Nightwatch()

def response(data, metadata):
    # send data to kafka
    send_data_to_kafka = os.environ.get('SEND_OUTPUT_TO_KAFKA')
    nightwatch.info('response handler: invoked - trigger source', metadata['trigger_source'])
    try:
        if send_data_to_kafka == 'true':
            nightwatch.info('response handler: sending data to kafka', data)
            if 'kafka_toic' in metadata:
                sendData(metadata['kafka_toic'], data, metadata)
    except Exception as e:
        nightwatch.error('response handler: send data to kafka - trigger source', metadata['trigger_source'])

    try:
        if metadata['trigger_source'] == 'api-gateway':
            nightwatch.info('response handler: trigger source', metadata['trigger_source'])
            return  {
                'statusCode': 200,
                'body': json.dumps({'data': data, 'source': metadata['trigger_source'] }),
                "headers": {
                    "Content-Type": "application/json"
                }
            }
        elif metadata['trigger_source'] == 'aws-service-kafka':
            return {'data': data, 'source': metadata['trigger_source'] }
            
        elif metadata['trigger_source'] == 'cli':
            nightwatch.info('response handler: trigger source', metadata['trigger_source'])
            return {'data': data, 'source': metadata['trigger_source'] }
        else:
            raise Exception("Unexpected trigger source.")

    except Exception as e:
        raise Exception(e)
import boto3
import uuid
import logging
import json

kinesis_client = boto3.client('kinesis', region_name='us-east-1')


def send_events(data: dict) -> None:

    try:
        kinesis_client.put_record(
            StreamName="risk-score",
            Data=bytes(json.dumps(data), 'utf-8'),
            PartitionKey=str(uuid.uuid4())
        )
    except Exception as e:
        logging.error(e)

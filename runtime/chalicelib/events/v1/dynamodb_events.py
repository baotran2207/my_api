

from chalice import Blueprint, Chalice

dynamodb_bp = Blueprint(__name__)

@dynamodb_bp.on_dynamodb_record(stream_arn='arn:aws:dynamodb:.../stream/2020')
def handle_ddb_message(event):
    for record in event:
        dynamodb_bp.log.debug("New: %s", record.new_image)
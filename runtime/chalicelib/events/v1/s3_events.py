
from chalice import Blueprint, Chalice


s3_bp = Blueprint(__name__)

@s3_bp.on_s3_event(bucket='mybucket-name',
                 events=['s3:ObjectCreated:*'])
def handle_s3_event(event):
    s3_bp.current_app.log.debug("Received event for bucket: %s, key: %s",
                  event.bucket, event.key)

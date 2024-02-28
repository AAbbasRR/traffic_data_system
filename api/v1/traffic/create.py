from flask import Blueprint, jsonify, request
from models import TrafficDataModel
from infra.persistance.db import session
from utils.validation import required_fields_exception
from datetime import datetime
import uuid

create_bp = Blueprint('create', __name__)


@create_bp.route('/', methods=['POST'])
@required_fields_exception(["user_id", "created_at", "page_url"])
def create_traffic():
    data = request.json
    user_id = data.get('user_id')
    created_at_str = data.get('created_at')
    created_at = datetime.strptime(created_at_str, '%Y-%m-%d %H:%M:%S')
    page_url = data.get('page_url')

    new_traffic_data = TrafficDataModel(
        request_id=str(uuid.uuid4()),
        user_id=user_id,
        created_at=created_at,
        page_url=page_url
    )
    session.add(new_traffic_data)
    session.commit()

    return jsonify({
        'message': 'Traffic data created successfully',
        "request_id": new_traffic_data.request_id
    }), 200

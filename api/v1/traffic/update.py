from flask import Blueprint, jsonify, request
from utils.validation import required_fields_exception
from models import TrafficDataModel
from infra.persistance.db import session
from datetime import datetime

update_bp = Blueprint('update', __name__)


@update_bp.route('/<string:request_id>', methods=['PUT'])
@required_fields_exception(["user_id", "created_at", "page_url"])
def update_traffic(request_id):
    data = request.json
    user_id = data.get('user_id')
    created_at_str = data.get('created_at')
    created_at = datetime.strptime(created_at_str, '%Y-%m-%d %H:%M:%S')
    page_url = data.get('page_url')

    traffic_data = session.query(TrafficDataModel).filter_by(request_id=request_id).first()
    if traffic_data:
        traffic_data.user_id = user_id
        traffic_data.created_at = created_at
        traffic_data.page_url = page_url
        session.commit()
        return jsonify({
            'message': 'Traffic data updated successfully',
            "request_id": traffic_data.request_id
        })
    else:
        return jsonify({'message': 'Record not found'}), 404

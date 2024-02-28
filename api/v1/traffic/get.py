from flask import Blueprint, jsonify
from models import TrafficDataModel
from infra.persistance.db import session
from datetime import datetime, timedelta
from sqlalchemy import func

get_bp = Blueprint('get', __name__)


@get_bp.route('/daily/<int:user_id>', methods=['GET'])
def get_traffic(user_id):
    now_time = datetime.now()
    last_24_hours = now_time - timedelta(hours=24)
    user_traffic = session.query(TrafficDataModel).filter(
        TrafficDataModel.user_id == user_id,
        TrafficDataModel.created_at < now_time,
        TrafficDataModel.created_at >= last_24_hours
    ).group_by(TrafficDataModel.page_url).with_entities(
        TrafficDataModel.page_url,
        func.count().label('page_count')
    ).all()
    result = {data[0]: data[1] for data in user_traffic}
    return jsonify(result)

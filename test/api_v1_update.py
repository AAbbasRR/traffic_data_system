import unittest
from flask import Flask, jsonify
from api.v1.traffic import update_bp
from models import TrafficDataModel
from infra.persistance.db import session
from datetime import datetime


class TestAPIUpdateTrafficView(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(update_bp, url_prefix='/api/v1/traffic')
        self.client = self.app.test_client()

    def test_update_traffic(self):
        mock_data = {
            'user_id': 1,
            'created_at': str(datetime.now().replace(microsecond=0)),
            'page_url': 'example.com/test'
        }

        created_traffic_data = session.query(TrafficDataModel).first()

        response = self.client.put(f'/api/v1/traffic/{created_traffic_data.request_id}', json=mock_data)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['message'], 'Traffic data updated successfully')
        self.assertEqual(data['request_id'], created_traffic_data.request_id)

    def test_required_fields_traffic(self):
        response = self.client.put('/api/v1/traffic/1')
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data, {
            "created_at": "This Field Is Required",
            "page_url": "This Field Is Required",
            "user_id": "This Field Is Required"
        })

    def test_not_found_traffic(self):
        mock_data = {
            'user_id': 1,
            'created_at': str(datetime.now().replace(microsecond=0)),
            'page_url': 'example.com/test'
        }

        response = self.client.put('/api/v1/traffic/1', json=mock_data)
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(data["message"], "Record not found")

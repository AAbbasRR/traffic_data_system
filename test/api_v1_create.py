import unittest
from flask import Flask, jsonify
from api.v1.traffic import create_bp
from models import TrafficDataModel
from infra.persistance.db import session
from datetime import datetime, timedelta


class TestAPICreateTrafficView(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(create_bp, url_prefix='/api/v1/traffic')
        self.client = self.app.test_client()

    def test_create_traffic(self):
        # Mock the request data
        mock_data = {
            'user_id': 1,
            'created_at': str(datetime.now().replace(microsecond=0) - timedelta(minutes=15)),
            'page_url': 'example.com'
        }

        response = self.client.post('/api/v1/traffic/', json=mock_data)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['message'], 'Traffic data created successfully')
        created_traffic_data = session.query(TrafficDataModel).filter_by(request_id=data["request_id"]).first()
        self.assertIsNotNone(created_traffic_data)
        self.client.post('/api/v1/traffic/', json=mock_data)

    def test_required_fields_traffic(self):
        response = self.client.post('/api/v1/traffic/')
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data, {
            "created_at": "This Field Is Required",
            "page_url": "This Field Is Required",
            "user_id": "This Field Is Required"
        })

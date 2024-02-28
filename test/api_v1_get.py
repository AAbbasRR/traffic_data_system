import unittest
from flask import Flask, jsonify
from api.v1.traffic import get_bp
from models import TrafficDataModel
from infra.persistance.db import session
from datetime import datetime


class TestAPIGetTrafficView(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(get_bp, url_prefix='/api/v1/traffic')
        self.client = self.app.test_client()
        self.count_user_1_objects = session.query(TrafficDataModel).filter_by(user_id=1).count()

    def get_user_1_traffic(self):
        response = self.client.get(f'/api/v1/traffic/daily/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['example.com'], self.count_user_1_objects)
        self.assertEqual(list(data.keys()), ["example.com"])

    def get_user_1_time_daily_traffic(self):
        user_1_data_object = session.query(TrafficDataModel).filter_by(user_id=1).first()
        user_1_data_object.created_at = datetime.strptime("2020-02-28 12:00:00", '%Y-%m-%d %H:%M:%S')
        session.commit()

        response = self.client.get(f'/api/v1/traffic/daily/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['example.com'], self.count_user_1_objects - 1)

    def get_user_2_traffic(self):
        response = self.client.get(f'/api/v1/traffic/daily/2')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data, {})

    def test_apis(self):
        self.get_user_1_traffic()
        self.get_user_1_time_daily_traffic()
        self.get_user_2_traffic()

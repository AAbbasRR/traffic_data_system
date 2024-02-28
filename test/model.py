import unittest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from decouple import config
from models.traffic_data import TrafficDataModel
from datetime import datetime
import uuid


class TestTrafficDataModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.clickhouse_user = config("CLICKHOUSE_USER", default="default")
        cls.clickhouse_password = config("CLICKHOUSE_PASSWORD", default="")
        cls.clickhouse_db = config("CLICKHOUSE_DB", default="default")
        conn_str = f'clickhouse://{cls.clickhouse_user}:{cls.clickhouse_password}@localhost/{cls.clickhouse_db}'
        cls.engine = create_engine(conn_str)
        Session = sessionmaker(bind=cls.engine)
        cls.session = Session()

    def create_and_select(self):
        request_id = str(uuid.uuid4())
        created_at = datetime.now().replace(microsecond=0)
        record = TrafficDataModel(request_id=request_id, created_at=created_at, user_id=1, page_url="example.com")
        self.session.add(record)
        self.session.commit()

        result = self.session.query(TrafficDataModel).filter_by(request_id=request_id).first()

        self.assertIsNotNone(result)
        self.assertEqual(result.created_at.replace(microsecond=0), created_at)

    def delete(self):
        request_id = str(uuid.uuid4())
        record = TrafficDataModel(request_id=request_id, created_at=datetime.now(), user_id=1, page_url="example.com")
        self.session.add(record)
        self.session.commit()

        self.session.delete(record)
        self.session.commit()

        result = self.session.query(TrafficDataModel).filter_by(request_id=request_id).first()

        self.assertIsNone(result)

    def test_functions(self):
        self.create_and_select()
        self.delete()

    @classmethod
    def tearDownClass(cls):
        test_records = cls.session.query(TrafficDataModel).all()

        for record in test_records:
            cls.session.delete(record)
            cls.session.commit()
        cls.session.close()

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from clickhouse_sqlalchemy import engines
from infra.persistance.db import database, engine

from datetime import datetime

Base = declarative_base()


class TrafficDataModel(Base):
    __tablename__ = 'traffic_data_model'
    __table_args__ = (
        engines.MergeTree(order_by=['request_id']),
        {'schema': database},
    )
    request_id = Column(String(36), primary_key=True)
    user_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.now(), key="created_at")
    page_url = Column(String)


try:
    TrafficDataModel.__table__.create(engine)
except Exception:
    pass

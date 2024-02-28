import unittest

from .model import TestTrafficDataModel
from .api_v1_create import TestAPICreateTrafficView
from .api_v1_update import TestAPIUpdateTrafficView
from .api_v1_get import TestAPIGetTrafficView

if __name__ == '__main__':
    unittest.main()

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from utils.load import save_to_csv
import pandas as pd
import os

class TestLoad(unittest.TestCase):
    def test_save_to_csv(self):
        df = pd.DataFrame({
            'title': ['A', 'B'],
            'price': [10.0, 20.0]
        })
        filename = 'test_output.csv'

        save_to_csv(df, filename)
        self.assertTrue(os.path.exists(filename))

        df_loaded = pd.read_csv(filename)
        self.assertTrue('title' in df_loaded.columns)
        os.remove(filename)

if __name__ == '__main__':
    unittest.main()

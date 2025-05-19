# remnant/tests/test_llm_service.py

import unittest
from remnant.services.llm_service import LLMService

class TestLLMService(unittest.TestCase):
    def setUp(self):
        self.llm = LLMService()

    def test_query_llm_mock(self):
        # Since real API keys may not be set, just test response type
        response = self.llm.query_llm("Hello")
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)

if __name__ == "__main__":
    unittest.main()

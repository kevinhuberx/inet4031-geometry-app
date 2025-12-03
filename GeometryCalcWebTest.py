import unittest
import GeometryCalcWeb as app

class TestWeb(unittest.TestCase):

	def setUp(self):
		app.app.testing = True
		self.app = app.app.test_client()

	def test_index(self):
		rv = self.app.get('/')
		self.assertEqual(rv.status, '200 OK')

if __name__ == '__main__':
	unittest.main()

import unittest
from hello import Storage

class TestSuite(unittest.TestCase):
  def test(self):
    storage = Storage()
    storage.populate(1234)
    score = storage.get_score()
    self.assertEqual(1234, score)

def main():
  unittest.main()

if __name__ == "__main__":
  main()

from django.test import TestCase

from api.models import Point

class PointTestCase(TestCase):
    def setUp(self):
        Point.objects.create(latitude=0., longitude=0.,
                             element_name="Null Island",
                             comment="All start here",
                             date="1900-01-01")

    def test_null_island_exist(self):
        """ This test is a shame  """
        points = Point.objects.filter(element_name="Null Island")
        self.assertNotEqual(len(points), 0)
    
    def test_atlantide_island_not_exist(self):
        """ This test is a shame  """
        points = Point.objects.filter(element_name="Atlantide")
        self.assertEqual(len(points), 0)

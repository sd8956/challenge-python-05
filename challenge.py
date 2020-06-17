import math


def square_area(side):
    """Returns the area of a square"""
    return side * side

def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    return base * height


def triangle_area(base, height):
    """Returns the area of a triangle"""
    return (base * height) / 2


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    return (diagonal_1 * diagonal_2) / 2


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    return ((base_major + base_minor) * height) / 2


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    return round((perimeter * apothem) / 2, 1)


def circumference_area(radius):
    """Returns the area of a circumference"""
    return round(math.pi,2) * (radius**2)


if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            # Initialize the needed values for the tests
            self.operations = {
                'square': {
                    'side': 5,
                    'result': 25
                },
                'rectangle': {
                    'base': 10,
                    'height': 5,
                    'result': 50
                },
                'triangle': {
                    'base': 5,
                    'height': 10,
                    'result': 25
                },
                'rhombus': {
                    'diagonal_1': 36,
                    'diagonal_2': 24,
                    'result': 432
                },
                'trapezoid': {
                    'base_minor': 7,
                    'base_major': 13,
                    'height': 6,
                    'result': 60
                },
                'regular_polygon': {
                    'perimeter': 30,
                    'apothem': 4.1,
                    'result': 61.5
                },
                'circumference': {
                    'radius': 10,
                    'result': 314
                }
            }


        def test_square_area(self):
            square = self.operations['square']
            
            self.assertEqual(square['result'], square_area(square['side']))
            

        def test_rectangle_area(self):
            rectangle = self.operations['rectangle']
            
            self.assertEqual(rectangle['result'], rectangle_area(rectangle['base'], rectangle['height']))


        def test_triangle_area(self):
            triangle = self.operations['triangle']
            
            self.assertEqual(triangle['result'],triangle_area(triangle['base'], triangle['height']))


        def test_rhombus_area(self):
            rhombus = self.operations['rhombus']
            
            self.assertEqual(rhombus['result'], rhombus_area(rhombus['diagonal_1'], rhombus['diagonal_2']))

        def test_trapezoid_area(self):
            trapezoid = self.operations['trapezoid']
            
            self.assertEqual(trapezoid['result'], trapezoid_area(trapezoid['base_minor'], trapezoid['base_major'], trapezoid['height']))

        def test_regular_polygon_area(self):
            regular_polygon = self.operations['regular_polygon']
            
            self.assertEqual(regular_polygon['result'], regular_polygon_area(regular_polygon['perimeter'], regular_polygon['apothem']))

        def test_circumference_area(self):
            circumference = self.operations['circumference']
            
            self.assertEqual(circumference['result'], circumference_area(circumference['radius']))

        def tearDown(self):
            del(self.operations)

    unittest.main()

from shapely.geometry import Point, LineString, Polygon

#point function
def create_point_geom(x_coord, y_coord):
    '''Create a shapely Point object'''
    return Point(x_coord, y_coord)

#test out the create_point_geom function
point1 = create_point_geom(0.0, 1.1)
print(point1)
print(point1.geom_type)

#line function
def create_line_geom(points):
    '''Create a shapely Linestring object'''
    assert type(points) is list, "Input should be a list!"
    assert len(points) >= 2, "LineString object requires at least 2 points"
    for point in points:
        assert type(point) == Point, "All list values should be Point objects"
    return LineString(points)

#test out the create_line_geom function
point2 = Point(45.2, 22.34)
point3 = Point(100.22, -3.20)
point_list = [point2, point3]
line1 = create_line_geom(point_list)

#polygon function
def create_poly_geom(points):
    '''Create a shapely Polygon object'''
    assert type(points) is list, 'Input should be a list'
    assert len(points) >=3, 'Polygon object requires at least 3 points'
    for point in points:
        assert type(point) == tuple, 'All values should be coordinate tuples'
    return Polygon(points)

#test out the create_poly_geom function
poly_points_list = [(45.2, 22.34),(100.22, -3.20),(70.0, 10.20)]

polygon1 = create_poly_geom(poly_points_list)
print(polygon1)


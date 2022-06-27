from shapely.geometry import Point, LineString, Polygon

def create_point_geom(x_coord, y_coord):
    return Point(x_coord, y_coord)

point1 = create_point_geom(0.0, 1.1)
print(point1)
print(point1.geom_type)

def create_line_geom(points):
    assert type(points) is list, "Input should be a list!"
    assert len(points) >= 2, "LineString object requires at least 2 points"
    for point in points:
        assert type(point) == Point, "All list values should be Point objects"
    return LineString(points)

point2 = Point(45.2, 22.34)
point3 = Point(100.22, -3.20)
point_list = [point2, point3]
line1 = create_line_geom(point_list)

def create_poly_geom(points):
    assert type(points) is list, 'Input should be a list'
    assert len(points) >=3, 'Polygon object requires at least 3 points'
    for point in points:
        assert type(point) == tuple, 'All values should be coordinate tuples'
    return Polygon(points)

poly_points_list = [(45.2, 22.34),(100.22, -3.20),(70.0, 10.20)]

polygon1 = create_poly_geom(poly_points_list)
print(polygon1)


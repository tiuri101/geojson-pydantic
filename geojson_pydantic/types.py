"""Types for geojson_pydantic models"""

from pydantic import conlist

BBox = conlist(float, min_items=4, max_items=8)
Position = conlist(float, min_items=2, max_items=4)

# Coordinate arrays
MultiPointCoords = conlist(Position, min_items=1)
LineStringCoords = conlist(Position, min_items=2)
MultiLineStringCoords = conlist(LineStringCoords, min_items=1)
LinearRing = conlist(Position, min_items=4)
PolygonCoords = conlist(LinearRing, min_items=1)
MultiPolygonCoords = conlist(PolygonCoords, min_items=1)

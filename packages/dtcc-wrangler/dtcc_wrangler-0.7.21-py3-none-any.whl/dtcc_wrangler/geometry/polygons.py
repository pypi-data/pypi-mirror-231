from shapely.geometry import Polygon
from typing import List, Tuple

from dtcc_model import Building, City
import shapely
from shapely.geometry import Point, Polygon, MultiPolygon, JOIN_STYLE
import shapely.ops
from shapely.validation import make_valid
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.csgraph import connected_components
from collections import defaultdict

from dtcc_wrangler.logging import debug, info, warning, error, critical


def merge_polygons_convexhull(p1, p2):
    mp = MultiPolygon([p1, p2])
    return mp.convex_hull


def merge_polygons_buffering(p1, p2, tol):
    b1 = p1.buffer(tol, 1, join_style=JOIN_STYLE.mitre)
    b2 = p2.buffer(tol, 1, join_style=JOIN_STYLE.mitre)
    m = b1.union(b2)
    m = m.buffer(-tol, 1, join_style=JOIN_STYLE.mitre)
    m = shapely.make_valid(m)
    if m.geom_type == "Polygon":
        return m
    else:
        return None


def merge_polygons_snapping(p1, p2, tol):
    coords = p2.exterior.coords[:]
    for idx, vertex in enumerate(coords):
        p = Point(vertex)
        nearest_point, _ = shapely.ops.nearest_points(p1.exterior, p)
        dist = p.distance(nearest_point)
        if dist > 0 and dist < tol:
            coords[idx] = nearest_point.coords[0]
    p2 = Polygon(coords)
    coords = p1.exterior.coords[:]
    for idx, vertex in enumerate(coords):
        p = Point(vertex)
        nearest_point, _ = shapely.ops.nearest_points(p2.exterior, p)
        dist = p.distance(nearest_point)
        if dist > 0 and dist < tol:
            coords[idx] = nearest_point.coords[0]
    p1 = Polygon(coords)

    m = p1.union(p2)
    m = make_valid(m)
    if m.geom_type == "Polygon":
        return m
    else:
        return None


def merge_polygons(p1, p2, tol):
    mp = p1.union(p2)
    # if mp.geom_type != "Polygon":
    #     info("Failed to merge polygons. Trying snapping")
    #     mp = merge_polygons_snapping(p1, p2, tol)
    if mp.geom_type != "Polygon":
        info("Failed to merge polygons. Trying buffering")
        mp = merge_polygons_buffering(p1, p2, tol)
        if mp is None:
            info("Failed to merge polygons. Falling back to convex hull")
            mp = merge_polygons_convexhull(p1, p2)
    return mp


def simplify_polygon(p: Polygon, tol):
    sp = p.simplify(tol)
    if sp.geom_type != "Polygon":
        sp = p.simplify(tol, preserve_topology=True)
    if sp.geom_type != "Polygon":
        sp = p
    return sp


def remove_slivers(p: Polygon, tol):
    p = p.buffer(tol, 1, join_style=JOIN_STYLE.mitre).buffer(
        -tol, 1, join_style=JOIN_STYLE.mitre
    )
    p = shapely.make_valid(p)
    return p


def remove_holes(p: Polygon):
    return Polygon(p.exterior)


def merge_multipolygon(multipolygon, tol=0.1):
    polygons = list(multipolygon.geoms)
    merged = []
    # orig_polygons = polygons.copy()
    if len(polygons) == 1:
        m = polygons[0]
    elif len(polygons) == 2:
        m = merge_polygons(polygons[0], polygons[1], tol)
    else:
        while len(polygons) > 0:
            p = polygons.pop()
            for i, p2 in enumerate(polygons):
                if p.intersects(p2.buffer(tol)):
                    p = merge_polygons(p, p2, tol)
                    polygons.pop(i)
                    polygons.append(p)
        merged.append(p)
        m = shapely.ops.unary_union(merged)
    m = make_valid(m)
    return m


def find_merge_candidates(polygons: List[Polygon], tol: float) -> List[List[int]]:
    """Find all polygons closer than _tolerance_ in a list of polygons and return a list of indices of polygons to be merged."""
    rtree = shapely.strtree.STRtree(polygons)
    merge_idxs = rtree.query(polygons, predicate="dwithin", distance=tol)
    merge_idxs = merge_idxs.T
    # keep = [m[0] != m[1] for m in merge_idxs]
    # merge_idxs = merge_idxs[keep]
    adj_matrix = lil_matrix(np.zeros((len(polygons), len(polygons))))
    for i, j in merge_idxs:
        adj_matrix[i, j] = 1
        adj_matrix[j, i] = 1
    # Find connected components using scipy.sparse.csgraph.connected_components
    _, labels = connected_components(adj_matrix, directed=False)
    polygon_indices = defaultdict(list)
    for idx, label in enumerate(labels):
        polygon_indices[label].append(idx)

    polygon_indices = [r for r in polygon_indices.values()]
    return polygon_indices


def merge_list_of_polygons(mcp: List[Polygon], tolerance=1e-2) -> Polygon:
    if len(mcp) == 1:
        return mcp[0]
    else:
        m = shapely.ops.unary_union(mcp)
        m = shapely.make_valid(m)
        if m.geom_type == "Polygon":
            return m
        else:
            m = merge_multipolygon(m, tolerance)
            if m.geom_type != "Polygon":
                warning("Failed to merge polygon list. Falling back to convex hull")
                m = m.convex_hull
            return m


def polygon_merger(
    polygons: List[Polygon], tolerance: float = 1e-2
) -> Tuple[List[Polygon], List[List[int]]]:
    """Merge all polygons closer than _tolerance_ in a list of polygons into a list of polygons and a list of indices of merged polygons."""
    merge_candidates = find_merge_candidates(polygons, tolerance)
    if len(merge_candidates) == len(polygons):
        # No polygons withon tolerance of each other
        return polygons, merge_candidates
    merge_candidate_polygons = []
    for mc in merge_candidates:
        merge_candidate_polygons.append([polygons[idx] for idx in mc])

    merged_polygons = []
    for mcp in merge_candidate_polygons:
        m = merge_list_of_polygons(mcp, tolerance)
        merged_polygons.append(m)

    return merged_polygons, merge_candidates

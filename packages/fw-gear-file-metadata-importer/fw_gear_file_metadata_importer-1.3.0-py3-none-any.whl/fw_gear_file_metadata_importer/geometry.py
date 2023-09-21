import math

import numpy as np
from numpy import ndarray

# This is used for type hints only


def compute_normal(orientation: ndarray) -> ndarray:
    """
    Computes the normal (cross product) of an image orientation vector

    :param orientation: Array of size 6 defining row and col vector in sequence
    :type orientation: ImageOrientationPatient tag value
    :return: A numpy 3D array representing the cross product of the column and row vector
    :rtype: numpy.array
    """
    rv = np.array(orientation[0:3])
    cv = np.array(orientation[3:6])
    return np.cross(rv, cv)


def compute_axis_from_pair(p1: ndarray, p2: ndarray) -> ndarray:
    """
    Computes the unit vector connecting p1 to p2
    :param p1: First point
    :param p2: 2nd point
    :return: Unit vector connecting the points
    """
    if p1 is None or p2 is None:
        return None
    assert len(p1) == len(p2)
    axis = np.subtract(p2, p1)
    # Compute magnitude of the vector connecting the origins
    mag = math.fabs(np.linalg.norm(axis))
    # if mag is valid, normalize to return unit vector
    if mag > 0.001:
        axis /= mag
    else:
        # This means the points are nearly degenerate and we should
        # not use them
        axis = None
    return axis


def compute_axis_from_origins(position_list: ndarray) -> ndarray:
    """
    Compute the axis that connects the first pair of non degenerate slice locations

    :param position_list: Numpy array of 3D slice locations
    :return: 3D unit axis connecting the first non degenerate pair of locations
    """
    if len(position_list) < 2:
        return None
    p0 = position_list[0]
    next_index = 1
    # Check first pair
    axis: object = compute_axis_from_pair(p0, position_list[next_index])
    # While the two origins are degenerate...
    while axis is None:
        # Sample the pair of the next origin and the first one
        next_index = next_index + 1
        if next_index >= len(position_list):
            # Need to break if we reach end of list
            break
        axis = compute_axis_from_pair(p0, position_list[next_index])
    return axis


def compute_slice_locations_from_origins(
    origin_list: ndarray, ortho_axis: ndarray = None
) -> ndarray:
    """
    Computes slice positions along an axis connecting a sequence of origins

    :param      origin_list   List of 3D slice origins
    :param      ortho_axis   Unit vector along which locations are computed
    :return:    Array of scalar slice positions computed along axis connecting their origins
    :rtype:     numpy.array
    """
    n = len(origin_list)
    axis = ortho_axis
    if axis is None:
        # Compute axis connecting the origins of the positions
        axis = compute_axis_from_origins(origin_list)
    # Convert slice positions to numpy array
    if not isinstance(origin_list, ndarray):
        origin_list = np.asarray(origin_list)
    # Reshape array as n 3D coordinates
    origin_list = origin_list.reshape((n, 3))
    # Compute dot product of axis against each 3D coordinate
    return np.dot(origin_list, axis)


def compute_slice_spacing_from_locations(slice_locations: ndarray) -> float:
    """
    Compute a scalar slice spacing from the vector of slice locations. If spacing
    is non uniform, the modal spacing is returned

    :param slice_locations: Vector of slice location (position along slice axis)
    :type slice_locations: ndarray
    :return: Scalar slice spacing between locations (mode value if they are not equal)
    :rtype: float
    """
    vdiff = np.diff(slice_locations).round(decimals=2)
    slice_spacing = None
    if len(vdiff) < 1:
        return slice_spacing
    min, max = vdiff.min(), vdiff.max()
    if np.isclose(min, max, atol=0.01):
        slice_spacing = min
    else:
        # Return None to indicate non uniform slice spacing
        slice_spacing = None
    return slice_spacing


def is_uniform(v: (list[float] | ndarray), decimals=2) -> bool:
    """
    Returns whether the input array has uniform values within a tolerance

    :param decimals: Number of significant digits after decimal
    :type decimals: int
    :param v: List or array of values
    :param atol: Tolerance for test of equality
    :return: Whether the input vector has uniform values
    """
    if not isinstance(v, ndarray):
        v = np.asarray(v).round(decimals=decimals)
    else:
        v = v.round(decimals=decimals)
    n_dims = len(v.shape)
    if n_dims == 1:
        vdiff = np.diff(v)
        return np.isclose(vdiff.min(), vdiff.max())
    else:
        v0 = v[0]
        for index in range(1, len(v)):
            v1 = v[index]
            if not np.array_equal(v0, v1):
                return False
        return True


def compute_affine(
    axes: list[list[float]], origin: list[float], spacing: list[float]
) -> ndarray:
    """
    Computes the affine transform relating a grid to its coordinates (x,y,z)

    :param axes: List of coordinate unit vectors in the row,col,slice(optional) dimension
    :type axes: numpy array [3][3]
    :param origin: Coordinates (x,y,z) of the grid origin (0,0,0)
    :type origin: numpy array [3]
    :param spacing: Regular scalar spacing between the col, row, and slices (optional)
    :type spacing: numpy array[3]
    :return: 4x4 affine matrix
    :rtype:
    """
    matrix = np.zeros((4, 4))
    # Not a bug in row vs col: Look closely at doc for this function
    ro = np.asarray(axes[0])
    co = np.asarray(axes[1])
    slice_axis = np.cross(ro, co)
    if len(axes) > 2:
        slice_axis = np.asarray(axes[2])
    # Not a bug in row vs col: Look closely at doc for this function
    col_spacing = spacing[0]
    row_spacing = spacing[1]
    slice_spacing = 1
    if len(spacing) > 2:
        slice_spacing = spacing[2]
    matrix[:, 0] = np.asarray(
        (ro[0] * col_spacing, ro[1] * col_spacing, ro[2] * col_spacing, 0)
    )
    matrix[:, 1] = np.asarray(
        (co[0] * row_spacing, co[1] * row_spacing, co[2] * row_spacing, 0)
    )
    matrix[:, 2] = np.asarray(
        (
            slice_axis[0] * slice_spacing,
            slice_axis[1] * slice_spacing,
            slice_axis[2] * slice_spacing,
            0,
        )
    )
    matrix[:, 3] = np.asarray((origin[0], origin[1], origin[2], 1.0))
    return matrix

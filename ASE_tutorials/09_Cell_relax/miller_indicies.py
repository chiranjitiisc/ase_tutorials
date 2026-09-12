import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def miller_plane(hkl=(1, 1, 1), a=1.0):

    h, k, l = hkl

    if (h, k, l) == (0, 0, 0):
        raise ValueError("(000) is not a valid Miller index.")

    # ---------------------------------------------------------
    # Miller plane equation
    #
    #       h*x/a + k*y/a + l*z/a = 1
    #
    # For example:
    # (100): x = a
    # (110): x + y = a
    # (111): x + y + z = a
    # ---------------------------------------------------------

    # Eight corners of the cubic unit cell
    corners = np.array([
        [0, 0, 0],
        [a, 0, 0],
        [a, a, 0],
        [0, a, 0],
        [0, 0, a],
        [a, 0, a],
        [a, a, a],
        [0, a, a]
    ], dtype=float)

    # Edges of the cube
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]

    # ---------------------------------------------------------
    # Find where the Miller plane intersects the cube edges
    # ---------------------------------------------------------

    plane_normal = np.array([h, k, l], dtype=float)

    points = []

    for i, j in edges:

        p1 = corners[i]
        p2 = corners[j]

        # Value of plane equation at the two endpoints
        f1 = np.dot(plane_normal, p1 / a) - 1
        f2 = np.dot(plane_normal, p2 / a) - 1

        # If one endpoint lies exactly on the plane
        if abs(f1) < 1e-10:
            points.append(p1)

        if abs(f2) < 1e-10:
            points.append(p2)

        # If the plane crosses the edge
        if f1 * f2 < 0:

            t = -f1 / (f2 - f1)

            point = p1 + t * (p2 - p1)

            points.append(point)

    # Remove duplicate points
    unique_points = []

    for p in points:

        if not any(
            np.linalg.norm(p - q) < 1e-8
            for q in unique_points
        ):
            unique_points.append(p)

    points = np.array(unique_points)

    if len(points) < 3:
        print(f"The ({h}{k}{l}) plane does not cut this particular unit cell.")
        print("Try another Miller index.")
        return

    # ---------------------------------------------------------
    # Order the points around the polygon
    # ---------------------------------------------------------

    center = points.mean(axis=0)

    normal = plane_normal / np.linalg.norm(plane_normal)

    # Find two vectors lying inside the plane
    if abs(normal[0]) < 0.9:
        reference = np.array([1.0, 0.0, 0.0])
    else:
        reference = np.array([0.0, 1.0, 0.0])

    u = np.cross(normal, reference)
    u = u / np.linalg.norm(u)

    v = np.cross(normal, u)
    v = v / np.linalg.norm(v)

    # Calculate angle of each point around the center
    angles = np.arctan2(
        np.dot(points - center, v),
        np.dot(points - center, u)
    )

    points = points[np.argsort(angles)]

    # ---------------------------------------------------------
    # Plot
    # ---------------------------------------------------------

    fig = plt.figure(figsize=(9, 8))

    ax = fig.add_subplot(
        111,
        projection="3d"
    )

    # ---------------------------------------------------------
    # Draw cube
    # ---------------------------------------------------------

    for i, j in edges:

        ax.plot(
            [corners[i, 0], corners[j, 0]],
            [corners[i, 1], corners[j, 1]],
            [corners[i, 2], corners[j, 2]],
            linewidth=1.5
        )

    # ---------------------------------------------------------
    # Draw cube corner atoms
    # ---------------------------------------------------------

    ax.scatter(
        corners[:, 0],
        corners[:, 1],
        corners[:, 2],
        s=70
    )

    # ---------------------------------------------------------
    # Draw Miller plane
    # ---------------------------------------------------------

    plane = Poly3DCollection(
        [points],
        alpha=0.45
    )

    ax.add_collection3d(plane)

    # ---------------------------------------------------------
    # Draw [hkl] normal direction
    # ---------------------------------------------------------

    normal_start = np.array([0.5, 0.5, 0.5])

    # Make arrow visible
    arrow_length = 0.65

    arrow = normal * arrow_length

    ax.quiver(
        normal_start[0],
        normal_start[1],
        normal_start[2],
        arrow[0],
        arrow[1],
        arrow[2],
        linewidth=3,
        arrow_length_ratio=0.15
    )

    # ---------------------------------------------------------
    # Axis labels
    # ---------------------------------------------------------

    ax.set_xlabel("x", fontsize=13)
    ax.set_ylabel("y", fontsize=13)
    ax.set_zlabel("z", fontsize=13)

    ax.set_xlim(0, a)
    ax.set_ylim(0, a)
    ax.set_zlim(0, a)

    ax.set_box_aspect((1, 1, 1))

    # ---------------------------------------------------------
    # Title
    # ---------------------------------------------------------

    ax.set_title(
        f"Miller Plane ({h}{k}{l})\n"
        f"Normal Direction [{h}{k}{l}]",
        fontsize=16
    )

    plt.tight_layout()
    plt.show()


# =============================================================
# CHANGE THE MILLER INDICES HERE
# =============================================================

miller_plane((2, 1, 1))
import pyvista as pv
import numpy as np
import json
import argparse
from pythreejs import Geometry

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="Input filename")
args = parser.parse_args()
argDict = vars(args)


f = open(argDict["input"])


parsed_data = json.load(f)

position_attribute = parsed_data["vertices"]
normal_attribute = parsed_data["normals"]
uv_attribute = parsed_data["uvs"]
faces = parsed_data["triangles"]


def convert_threejs_to_pyvista(geometry):
    # Extract vertex positions
    positions = np.array(geometry["vertices"])

    # Extract face indices
    indices = np.hstack(geometry["triangles"])
    cells = {pv.CellType.TRIANGLE: indices}

    # Extract vertex normals (optional)
    normals = None
    if "normals" in geometry:
        normals = np.array(geometry["normals"])

    # Extract UV coordinates (optional)
    uvs = None
    if "uvs" in geometry:
        uvs = np.array(geometry["uvs"])

    # Create PyVista mesh
    mesh = pv.UnstructuredGrid(cells, positions).extract_surface()

    if normals is not None:
        mesh.point_data["normals"] = normals

    if uvs is not None:
        mesh.point_data["texture_coords"] = uvs

    return mesh


# @Working with Pyvista Examples

# from pyvista import examples

# figfig = examples.download_foot_bones()

# vertex_positions = np.array(figfig.points)
# triangle_indices = np.hstack(figfig.faces)

# points = np.array(figfig.points)
# faces = np.hstack(figfig.faces.reshape(-1, 4)[:, 1:])

# cells = {pv.CellType.TRIANGLE: faces}
# print(faces)
# /@Working with Pyvista Examples

pyvista_mesh = convert_threejs_to_pyvista(parsed_data)

p = pv.Plotter()
p.add_mesh(pyvista_mesh, color="lightblue", opacity=1)
p.show()

# BufferGeometry2Pyvista
This script extracts all the required data from a Three.js BufferGeometry and converts it to a Pyvista Mesh

### How it works : 
⚠️Asumming you have already extracted the required data from your Threejs Buffer Geometry ⚠️

⚠️You can check the [threejsbfextract.js](threejsbfextract.js) to check how I extracted it. ⚠️

This script will extract and use the **vertices**, **normals**, **uvs**, and **faces/triangles** extracted from the Threejs Buffer Geometry and use it to build a new mesh in Pyvista so you can use and play with it.


### Requirements : 
```
pyvista
numpy
```

### Usage 
```
usage: 3jsBG2Pyvista.py [-h] [-i INPUT]

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input filename in Json
```

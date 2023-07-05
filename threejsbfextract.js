// In my case, The Threejs Buffer Geometry is *dataSelected*
// Exporting Geo Data
const geo = dataSelected.geometry;
const positions = geo.attributes.position.array;

// Get the vertex normals from the geometry (if available)
const normals = geo.attributes.normal ? geo.attributes.normal.array : null;

// Get the UV coordinates from the geometry (if available)
const uvs = geo.attributes.uv ? geo.attributes.uv.array : null;

// Get the triangle indices from the geometry
const indices = geo.index ? geo.index.array : null;

// Convert the vertex positions to a nested array of [x, y, z] coordinates
const vertices = [];
for (var i = 0; i < positions.length; i += 3) {
  vertices.push([positions[i], positions[i + 1], positions[i + 2]]);
}

// Convert the vertex normals to a nested array of [x, y, z] coordinates (if available)
const normalsArray = [];
if (normals) {
  for (var i = 0; i < normals.length; i += 3) {
    normalsArray.push([normals[i], normals[i + 1], normals[i + 2]]);
  }
}

// Convert the UV coordinates to a nested array of [u, v] coordinates (if available)
const uvsArray = [];
if (uvs) {
  for (var i = 0; i < uvs.length; i += 2) {
    uvsArray.push([uvs[i], uvs[i + 1]]);
  }
}

// Convert the triangle indices to a nested array of triangle indices (if available)
const triangles = [];
if (indices) {
  for (var i = 0; i < indices.length; i += 3) {
    triangles.push([indices[i], indices[i + 1], indices[i + 2]]);
  }
}

// Create an object that contains all the exported data
const exportData = {
  vertices: vertices,
  normals: normalsArray,
  uvs: uvsArray,
  faces: triangles,
};

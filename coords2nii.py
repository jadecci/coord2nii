import argparse
import nibabel as nib
import csv
import numpy as np
import numpy.matlib as matlib
from scipy.interpolate import interpn

## Usage & arguments parsing
parser = argparse.ArgumentParser(description="Converts MNI coordinates to a binary nifti volume")
parser.add_argument("input", type=str, nargs=1,
                    help=".csv file containing a set of coordinates per row")
parser.add_argument("output", type=str, nargs=1,
                    help="output file name (.nii or .nii.gz)")
parser.add_argument("--template", type=str, nargs=1, dest="template",
                    default="MNI152_T1_2mm_brain.nii.gz",
                    help="a nifti volume in MNI space, which determines the resolution of the output")
parser.add_argument("--type", type=str, nargs=1, dest="type",
                    default="XYZ", help="type of coordinates (XYZ/LAS or RAS)")
args = parser.parse_args()

### Set-up
template = nib.load(args.template)
vox2ras = template.get_sform()
data = template.get_data()

### Collect coordinates
with open(args.input[0], "r") as f:
    reader = csv.reader(f)
    coords = np.array(list(reader), dtype=float)
coords = coords.T

### Coordinates conversions
# convert to RAS coordinates if necessary
if args.type == "XYZ" or args.type == "LAS":
    coords[0, :] = - coords[0, :]

# convert to voxel coordinates
ras_centered = coords - matlib.repmat(vox2ras[0:3, 3], coords.shape[1], 1).T
vox_coords = np.linalg.inv(vox2ras[0:3, 0:3]) @ ras_centered

# find nearest voxels for the coordinates
grid_pts = [range(data.shape[0]), range(data.shape[1]), range(data.shape[2])]
linear_ind = np.arange(np.prod(data.shape)).reshape(data.shape)
vox_ind = interpn(grid_pts, linear_ind, vox_coords.T, 'nearest')

### Nifti generation
# write a value of 1 to each voxel
vol = np.zeros(data.shape)
vol[np.unravel_index(vox_ind.astype(int), data.shape)] = 1

# save volume
img = nib.Nifti1Image(vol, template.affine, template.header)
nib.save(img, args.output[0])

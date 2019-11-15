# MNI coordinates to nifti volume conversion

The script `coords2nii.py` takes in a csv file with a set of MNI coordinates each row, and creates a nifti volume where each voxel correponsinding to a
set of coordinates is assigned a value of 1. By default, the volume is generated in 2mm MNI space.

To see usage of the script: `python3 coords2nii.py -h`

## Example

To run an example, use `python3 coords2nii.py example_coord.csv example_coord.nii.gz`

You can compare `example_coord.nii.gz` and `example_coord_check.nii.gz`; they should be identical.

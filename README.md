# MNI coordinates to nifti volume conversion

The script `coords2nii.py` takes in a csv file with a set of MNI coordinates each row, and creates a nifti volume where each voxel correponsinding to a
set of coordinates is assigned a value of 1. By default, the volume is generated in 2mm MNI space.

Note that this script is only tested in Python 3 and might not work in Python 2.

To see usage of the script: `python3 coords2nii.py -h`

## Coordinates type

By default, the script assumes that the coordinates are in XYZ/LAS orientation, following the peak coordinates from NeuroSynth. Set `--type RAS` if
you are sure your coordinates are in RAS orientation.

## Example

To run an example, use `python3 coords2nii.py example_coord.csv example_coord.nii.gz` in the command line

You can compare `example_coord.nii.gz` and `example_coord_check.nii.gz`; they should be identical.

#!/bin/bash
for fold in {0..4}
do
    echo "=== Starting Fold $fold ==="
    nnUNetv2_train 009 3d_fullres $fold
done
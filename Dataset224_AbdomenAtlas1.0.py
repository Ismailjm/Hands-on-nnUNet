from nnunetv2.dataset_conversion.generate_dataset_json import generate_dataset_json
from batchgenerators.utilities.file_and_folder_operations import *
import shutil

if __name__ == "__main__":
    # Adjust this to the root where your RawData folder is
    base_dir = "/home/ismail/projet_PFE/Hands-on-nnUNet/nnUNetFrame/dataset/RawData"
    dataset_id = 9  # choose any unused ID
    dataset_name = f"Dataset{dataset_id:03d}_AbdomenBTCV"
    output_dir = (
        "/home/ismail/projet_PFE/Hands-on-nnUNet/nnUNetFrame/dataset/nnUNet_raw"
    )

    dataset_path = join(output_dir, dataset_name)
    maybe_mkdir_p(dataset_path)  # nnU-Net needs this even if subfolders already exist

    imagesTr = join(dataset_path, "imagesTr")
    labelsTr = join(dataset_path, "labelsTr")
    imagesTs = join(dataset_path, "imagesTs")

    shutil.copytree(join(base_dir, "imagesTr"), imagesTr)
    shutil.copytree(join(base_dir, "labelsTr"), labelsTr)
    shutil.copytree(join(base_dir, "imagesTs"), imagesTs)

    # Your custom label dictionary (same as above)
    labels = {
        "background": 0,
        "spleen": 1,
        "kidney_right": 2,
        "kidney_left": 3,
        "gall_bladder": 4,
        "esophagus": 5,
        "liver": 6,
        "stomach": 7,
        "aorta": 8,
        "postcava": 9,
        "vein_portal_splenic": 10,
        "pancreas": 11,
        "adrenal_gland_right": 12,
        "adrenal_gland_left": 13,
    }

    # Create dataset.json
    generate_dataset_json(
        dataset_path,
        {
            0: "nonCT"
        },  # this was a mistake we did at the beginning and we keep it like that here for consistency
        labels,
        len(subfiles(labelsTr, suffix=".nii.gz")),
        ".nii.gz",
        None,
        dataset_name,
        overwrite_image_reader_writer="NibabelIOWithReorient",
    )

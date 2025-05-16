import os


def main():

    def rename_imagesTr(folder_path):
        for count, file in enumerate(sorted(os.listdir(folder_path))):
            dst = f"img_{str(count).zfill(3)}_0000.nii.gz"
            src = f"{folder_path}/{file}"
            dst = f"{folder_path}/{dst}"
            os.rename(src, dst)

    def rename_labelsTr(folder_path):
        for count, file in enumerate(sorted(os.listdir(folder_path))):
            dst = f"img_{str(count).zfill(3)}.nii.gz"
            src = f"{folder_path}/{file}"
            dst = f"{folder_path}/{dst}"
            os.rename(src, dst)


    def rename_imageTs(folder_path):
        for count, file in enumerate(sorted(os.listdir(folder_path))):
            dst = f"img_{str(count+30).zfill(3)}_0000.nii.gz"
            src = f"{folder_path}/{file}"
            dst = f"{folder_path}/{dst}"
            os.rename(src, dst)

    labelsTr_path = "nnUNetFrame/dataset/RawData/labelsTr"
    imagesTr_path = "nnUNetFrame/dataset/RawData/imagesTr"
    imagesTs_path = "nnUNetFrame/dataset/RawData/imagesTs"

    rename_imagesTr(imagesTr_path)
    rename_labelsTr(labelsTr_path)
    rename_imageTs(imagesTs_path)


if __name__ == "__main__":
    main()

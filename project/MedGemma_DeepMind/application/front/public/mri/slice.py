import cv2
import numpy as np
import os
import nibabel as nib
from pathlib import Path

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent.resolve()
BASE_DIR = SCRIPT_DIR  # mri directory

TO_SLICE = [
    str(BASE_DIR / "0"),
    str(BASE_DIR / "1")
]
SEG = {
    str(BASE_DIR / "0.seg"): str(BASE_DIR / "0"),
    str(BASE_DIR / "1.seg"): str(BASE_DIR / "1")
}
DIFFERENCE = str(BASE_DIR / "difference")

def extract_files():
    for slice_path in TO_SLICE:
        # Load the NIfTI file
        img = nib.load(os.path.join(slice_path, "mri_file.nii"))
        data = img.get_fdata()

        for i in range(154):
            slice = data[i]
            min_val, max_val = np.min(slice), np.max(slice)
            if max_val - min_val > 0:
                slice = (slice - min_val) / (max_val - min_val) * 255
            else:
                slice = np.zeros_like(slice)
            slice = slice.astype(np.uint8)
            name = os.path.join(slice_path, f"slice_{i:03d}.jpg")
            cv2.imwrite(name, slice)
        
        print(f"Saved slices for {slice_path} to disk.")

    for seg_path, orig_path in SEG.items():
        # Generate jpg of the slice with the segmentation as red on top
        segmentation = nib.load(os.path.join(seg_path, "mri_file.nii")).get_fdata()
        segmentation = (segmentation > 0).astype(np.float32)

        orig_data = nib.load(os.path.join(orig_path, "mri_file.nii")).get_fdata()
        for i in range(154):
            orig_slice = orig_data[i]
            seg_slice = segmentation[i]

            # Normalize original slice
            min_val, max_val = np.min(orig_slice), np.max(orig_slice)
            orig_slice = (orig_slice - min_val) / (max_val - min_val) * 255
            orig_slice = orig_slice.astype(np.uint8)

            # Create a color image with red segmentation
            color_image = cv2.cvtColor(orig_slice, cv2.COLOR_GRAY2BGR)
            color_image[seg_slice > 0] = [0, 0, 255]
            name = os.path.join(seg_path, f"slice_{i:03d}.jpg")
            cv2.imwrite(name, color_image)

    os.makedirs(DIFFERENCE, exist_ok=True)
    seg_0_path = str(BASE_DIR / "0.seg" / "mri_file.nii")
    seg_1_path = str(BASE_DIR / "1.seg" / "mri_file.nii")
    seg_0 = nib.load(seg_0_path).get_fdata()
    seg_1 = nib.load(seg_1_path).get_fdata()

    # Calculate the difference
    diff = np.abs(seg_1 - seg_0)

    # Load the original MRI data for 1
    orig_data = nib.load(str(BASE_DIR / "1" / "mri_file.nii")).get_fdata()

    for i in range(154):
        orig_slice = orig_data[i]
        diff_slice = diff[i]

        # Normalize original slice
        min_val, max_val = np.min(orig_slice), np.max(orig_slice)
        orig_slice = (orig_slice - min_val) / (max_val - min_val) * 255
        orig_slice = orig_slice.astype(np.uint8)

        # Create a color image with red difference
        color_image = cv2.cvtColor(orig_slice, cv2.COLOR_GRAY2BGR)
        color_image[diff_slice > 0] = [0, 0, 255]
        
        name = os.path.join(DIFFERENCE, f"slice_{i:03d}.jpg")
        cv2.imwrite(name, color_image)

    print("Saved difference slices to disk.")
    return True


if __name__ == "__main__":
    try:
        extract_files()
    except Exception as e:
        print(f"Error during extraction: {e}")
        raise e
    else:
        print("Extraction completed successfully.")

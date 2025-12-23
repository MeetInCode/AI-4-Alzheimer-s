'''
Code to handle segmentation tasks
'''

import subprocess
import os
import nibabel as nib
import numpy as np
import glob
import shutil
from pathlib import Path

def run_segmentation(id):
    """
    Run segmentation using the remote nnU-Net endpoint
    
    Args:
        id (str): The MRI ID (e.g., "0" or "1")
    """
    # Define input and output file paths (relative to application directory)
    from pathlib import Path
    application_dir = Path(__file__).parent.parent
    input_file = str(application_dir / "front" / "public" / "mri" / id / "mri_file.nii")
    output_file = str(application_dir / "front" / "public" / "mri" / f"{id}.seg" / "mri_file.nii")
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Path to the test_remote_endpoint script (relative to project root)
    project_root = application_dir.parent
    script_path = str(project_root / "nnunet-inference" / "test_remote_endpoint.py")
    
    # Construct the command
    command = [
        "python", 
        script_path,
        "--input_file", input_file,
        "--output_file", output_file
    ]
    
    try:
        print(f"Running segmentation for ID {id}...")
        print(f"Input: {input_file}")
        print(f"Output: {output_file}")
        
        # Run the command
        result = subprocess.run(command, 
                              capture_output=True, 
                              text=True, 
                              check=True)
        
        print("Segmentation completed successfully!")
        print(result.stdout)
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Error running segmentation: {e}")
        print(f"stderr: {e.stderr}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
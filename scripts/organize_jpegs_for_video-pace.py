import os
import sys


BASE_PATH = "CHANGE ME"


def organize_ucf_jpegs(path: str):
    """Organize the UCF dataset for the video-pace repository.

    The pre-extracted RGB frames are organized as follows:

        jpegs_256/
            v_ApplyEyeMakeup_g01_c01/
                frame000001.jpg
                frame000002.jpg
                ...
            v_ApplyEyeMakeup_g01_c02/
                frame000001.jpg
                frame000002.jpg
                ...
            ...

    This function will organize the dataset into the following format:
        
        jpegs_256/
            ApplyEyeMakeup/
                v_ApplyEyeMakeup_g01_c01/
                    frame000001.jpg
                    frame000002.jpg
                    ...
                v_ApplyEyeMakeup_g01_c02/
                    frame000001.jpg
                    frame000002.jpg
                    ...
                ...
            ...
    """
    if BASE_PATH == "CHANGE ME":
        print("Please change the BASE_PATH variable to the path of the jpegs_256 folder.")
        sys.exit(1)

    # Iterate through the directories
    for root, _, files in os.walk(path):
        for name in files:
            if name.endswith(".jpg"):
                # Get the class name
                class_name = root.split("/")[-1]
                group_name = class_name.split("_")[1]

                # Create the new path
                new_path = os.path.join(path, group_name, class_name)

                # Create the new directory if it doesn't exist
                if not os.path.exists(new_path):
                    os.makedirs(new_path)
                    print(f"Created {new_path}...")
                
                # Move the file
                os.rename(os.path.join(root, name), os.path.join(new_path, name))


if __name__ == "__main__":
    organize_ucf_jpegs(BASE_PATH)

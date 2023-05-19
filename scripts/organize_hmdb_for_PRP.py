import os


def organize_hmdb():
    """Organize the HMDB51 dataset for the PRP repository.

    The HMDB51 dataset is stored in rar files, so this function will extract the rar files and organize the dataset into this structure:

        HMDB51/
            video/
                brush_hair/
                    BrushingHair_g01_c01.avi
                    BrushingHair_g01_c02.avi
                    ...
                cartwheel/
                    Cartwheeling_g01_c01.avi
                    Cartwheeling_g01_c02.avi
                    ...
                ...
    """
    # Assert that the HMDB folder exists
    if not os.path.exists(os.path.join(os.path.dirname(__file__), "HMDB51")):
        print("The HMDB51 folder does not exist.")
        print("Please download the HMDB51 dataset and place it in the datasets folder.")
        print("If you have already downloaded the dataset, please make sure this script and the HMDB51 folder are in the same directory.")

    # Get the path to the HMDB dataset from the current filepath
    hmdb_path = os.path.join(os.path.dirname(__file__), "HMDB51")

    # Get the list of rars in the folder
    rars = sorted(os.listdir(hmdb_path))

    # Get the path to the video folder
    video_dir_path = os.path.join(hmdb_path, "video")

    # Create a video folder in the HMDB dataset
    if not os.path.exists(video_dir_path):
        os.mkdir(video_dir_path)
        print("Creating new video folder...")

    # Iterate through the rars
    i = 0
    for rar in rars:
        i += 1
        print(f"Extracting {rar} ({i}/{len(rars)})...")
        # Get the path to the rar
        rar_path = os.path.join(hmdb_path, rar)

        # Extract the rar
        os.system(f"unrar x -idq {rar_path} {video_dir_path}")

        # Delete the rar
        os.remove(rar_path)


if __name__ == "__main__":
    organize_hmdb()

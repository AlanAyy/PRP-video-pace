import os


def organize_ucf():
    """Organize the UCF101 dataset for the PRP repository.

    The dataset is organized as follows:

        UCF101/
            v_ApplyEyeMakeup_g01_c01.avi
            v_ApplyEyeMakeup_g01_c02.avi
            v_ApplyLipstick_g01_c01.avi
            v_ApplyLipstick_g01_c02.avi
            ...

    This function will organize the dataset into the following format:

        UCF101/
            video/
                ApplyEyeMakeup/
                    v_ApplyEyeMakeup_g01_c01.avi
                    v_ApplyEyeMakeup_g01_c02.avi
                    ...
                ApplyLipstick/
                    v_ApplyLipstick_g01_c01.avi
                    v_ApplyLipstick_g01_c02.avi
                    ...
                ...
    """
    # Assert that the UCF folder exists
    if not os.path.exists(os.path.join(os.path.dirname(__file__), "UCF101")):
        print("The UCF101 folder does not exist.")
        print("Please download the UCF101 dataset and place it in the datasets folder.")
        print("If you have already downloaded the dataset, please make sure this script and the UCF101 folder are in the same directory.")

    # Get the path to the UCF dataset from the current filepath
    ucf_path = os.path.join(os.path.dirname(__file__), "UCF101")

    # Get the list of videos in the folder
    videos = os.listdir(ucf_path)

    # Get the path to the video folde
    video_dir_path = os.path.join(ucf_path, "video")

    # Create a video folder in the UCF dataset
    if not os.path.exists(video_dir_path):
        os.mkdir(video_dir_path)
        print("Creating new video folder...")

    # Iterate through the videos
    for video in videos:
        # Get the path to the video
        video_path = os.path.join(ucf_path, video)

        # Get the name of the action
        action = video.split("_")[1]

        # Get the path to the action folder
        action_path = os.path.join(video_dir_path, action)

        # Create the action folder if it does not exist
        if not os.path.exists(action_path):
            os.mkdir(action_path)
            print(f"Creating new folder for action: {action}...")

        # Get the path to the new video
        new_video_path = os.path.join(action_path, video)

        # Move the video to the action folder
        os.rename(video_path, new_video_path)
    print("Done!")


if __name__ == "__main__":
    organize_ucf()

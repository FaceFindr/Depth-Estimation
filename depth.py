import argparse
import cv2
import numpy as np

def get_depth_plane(depth_value):
    if depth_value < 86:
        return 'back'
    elif depth_value < 171:
        return 'middle'
    else:
        return 'front'

if __name__ == '__main__':
    depth_parser = argparse.ArgumentParser()
    depth_parser.add_argument('--img-path', type=str, required=True)
    args = depth_parser.parse_args()

    depth_map = cv2.imread(args.img_path, cv2.IMREAD_GRAYSCALE)

    avg_depth = np.mean(depth_map)

    depth_plane = get_depth_plane(avg_depth)

    print(f"Depth plane of the image: {depth_plane}")
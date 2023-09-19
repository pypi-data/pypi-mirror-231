"""
Adds ZoeDepth predictions to a nerfstudio-style dataset.
"""
import json
import os
import time

import numpy as np
import torch
from PIL import Image

_transforms_keys = ["fl_x", "fl_y", "cx", "cy", "w", "camera_model", "k1", "k2", "p1", "p2", "frames"]
_zoe_models = ["ZoeD_N", "ZoeD_K", "ZoeD_NK"]


def load_transforms(dataset_path: str) -> dict:
    """Load transforms.json and check that it conforms to the nerfstudio format"""
    transforms_fname = os.path.join(dataset_path, "transforms.json")
    if not os.path.exists(transforms_fname):
        raise ValueError(f"{transforms_fname} does not exist")
    with open(transforms_fname, "r") as f:
        transforms = json.load(f)
    for key in _transforms_keys:
        if key not in transforms:
            raise ValueError(f"{transforms_fname} does not contain key {key}")
    return transforms


def add_zoedepth_to_dataset(dataset_path: str, zoe_model_name: str, device: torch.device) -> None:
    # Load frames (i.e., images) for the dataset
    transforms = load_transforms(dataset_path)
    frame_paths = [frame["file_path"] for frame in transforms["frames"]]
    frame_paths = [
        os.path.join(dataset_path, frame_path) if not frame_path.startswith("/") else frame_path
        for frame_path in frame_paths
    ]
    frame_pils = [Image.open(frame_path).convert("RGB") for frame_path in frame_paths]
    print(f"Loaded {len(frame_pils)} frames for dataset {dataset_path}")

    # Load ZoeDepth model
    if zoe_model_name not in _zoe_models:
        raise ValueError(f"Unknown ZoeDepth model {zoe_model_name}")
    zoe = torch.hub.load("isl-org/ZoeDepth", zoe_model_name, pretrained=True)
    zoe = zoe.eval()
    zoe = zoe.to(device)
    print(f"Loaded {zoe_model_name} model to {device}")

    # Run ZoeDepth on frames, nerfstudio assumes millimeters in float16 or float32
    # https://docs.nerf.studio/en/latest/quickstart/data_conventions.html#depth-images
    start_time = time.perf_counter()
    depths = [zoe.infer_pil(pil) for pil in frame_pils]
    depths_mm = [depth * 1000 for depth in depths]
    duration = time.perf_counter() - start_time
    print(f"Predicted {len(depths)} depth images in {duration:.2f}s")

    # Save depth images
    depth_dir = os.path.join(dataset_path, "depth")
    os.makedirs(depth_dir, exist_ok=True)
    if os.listdir(depth_dir):
        raise ValueError(f"{depth_dir} is not empty. Please delete existing depth images.")

    for frame_path, depth in zip(frame_paths, depths_mm):
        # Remove extension and use PNG
        frame_fname = os.path.splitext(os.path.basename(frame_path))[0] + ".png"
        depth_fname = os.path.join(depth_dir, frame_fname)

        # save as float32 png
        assert depth.dtype == np.float32
        depth_pil = Image.fromarray(depth)
        depth_pil.save(depth_fname)


    # Update transforms.json with depth frames


if __name__ == "__main__":
    device_ = "cuda" if torch.cuda.is_available() else "cpu"
    add_zoedepth_to_dataset(
        "/home/william/workspace/vqn/f3rm-public-release/datasets/f3rm/panda/scene_001", "ZoeD_N", device_
    )

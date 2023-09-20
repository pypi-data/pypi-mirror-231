from geda.data_providers.base import DataProvider
from typing import Literal
from PIL import Image
from geda.utils.files import read_txt_file
import glob
import os


class BaseSegmentationDataset:
    def __init__(
        self,
        root: str,
        split: Literal["train", "val", "test"],
        data_provider: DataProvider,
    ):
        self.split = split
        self.ids = data_provider.split_ids[split]
        self.images_paths = data_provider.filepaths["images"][split]
        self.masks_paths = data_provider.filepaths["masks"][split]
        self.root = root

    def get_raw_data(self, idx) -> tuple[Image.Image, Image.Image]:
        image_fpath = self.images_paths[idx]
        mask_fpath = self.masks_paths[idx]
        image = Image.open(image_fpath).convert("RGB")
        mask = Image.open(mask_fpath)
        return image, mask

    def __len__(self):
        return len(self.images_paths)


class BaseClassificationDataset:
    def __init__(
        self,
        root: str,
        split: Literal["train", "val", "test"],
        data_provider: DataProvider,
    ):
        self.split = split
        self.ids = data_provider.split_ids[split]
        self.images_paths = data_provider.filepaths["images"][split]
        self.labels_paths = data_provider.filepaths["labels"][split]
        self.root = root

    def get_raw_data(self, idx: int) -> tuple[Image.Image, int]:
        image_fpath = self.images_paths[idx]
        label_fpath = self.labels_paths[idx]
        image = Image.open(image_fpath).convert("RGB")
        label = int(read_txt_file(label_fpath)[0])
        return image, label

    def __len__(self):
        return len(self.images_paths)

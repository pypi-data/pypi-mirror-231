from geda.data_providers.mnist import MNISTDataProvider
from geda.datasets.base import BaseClassificationDataset
from typing import Literal


class MNISTClassificationDataset(BaseClassificationDataset):
    def __init__(self, root: str, split: Literal["train", "test"]):
        data_provider = MNISTDataProvider(root)
        super().__init__(root, split, data_provider)


if __name__ == "__main__":
    from geda.utils.config import ROOT

    root = str(ROOT / "data" / "DUTS")
    ds = MNISTClassificationDataset(root, "train")
    ds = MNISTClassificationDataset(root, "test")

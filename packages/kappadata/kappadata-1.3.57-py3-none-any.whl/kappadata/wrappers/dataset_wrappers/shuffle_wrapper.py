import numpy as np

from kappadata.datasets.kd_subset import KDSubset


class ShuffleWrapper(KDSubset):
    def __init__(self, dataset, seed=None):
        self.seed = seed
        if seed is not None:
            rng = np.random.default_rng(seed=seed)
        else:
            rng = np.random
        indices = np.arange(len(dataset), dtype=np.int64)
        rng.shuffle(indices)
        super().__init__(dataset=dataset, indices=indices)

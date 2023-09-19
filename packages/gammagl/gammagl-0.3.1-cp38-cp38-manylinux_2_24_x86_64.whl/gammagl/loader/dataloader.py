from collections.abc import Mapping, Sequence
from typing import List, Optional, Union

# import torch.utils.data
# from torch.utils.data.dataloader import default_collate

from gammagl.data import BatchGraph, Graph, Dataset
import tensorlayerx as tlx


class Collater:
    def __init__(self, follow_batch, exclude_keys):
        self.follow_batch = follow_batch
        self.exclude_keys = exclude_keys

    def __call__(self, batch):
        elem = batch[0]
        if isinstance(elem, Graph):
            return BatchGraph.from_data_list(batch, self.follow_batch,
                                        self.exclude_keys)
        # elif isinstance(elem, torch.Tensor):
        #     return default_collate(batch)
        elif isinstance(elem, float):
            return tlx.convert_to_tensor(batch, dtype=tlx.float32)
        elif isinstance(elem, int):
            return tlx.convert_to_tensor(batch, dtype=tlx.int64)
        elif isinstance(elem, str):
            return batch
        elif isinstance(elem, Mapping):
            return {key: self([data[key] for data in batch]) for key in elem}
        elif isinstance(elem, tuple) and hasattr(elem, '_fields'):
            return type(elem)(*(self(s) for s in zip(*batch)))
        elif isinstance(elem, Sequence) and not isinstance(elem, str):
            return [self(s) for s in zip(*batch)]

        raise TypeError(f'DataLoader found invalid type: {type(elem)}')

    def collate(self, batch):  # Deprecated...
        return self(batch)


class DataLoader(tlx.dataflow.DataLoader):
    r"""A data loader which merges data objects from a
    :class:`gammagl.data.Dataset` to a mini-batch.
    Data objects can be either of type :class:`~gammagl.data.Graph` or
    :class:`~gammagl.data.HeteroGraph`.

    Parameters
    ----------
    dataset: Dataset
        The dataset from which to load the data.
    batch_size: int, optional
        How many samples per batch to load.
        (default: :obj:`1`)
    shuffle: bool, optional
        If set to :obj:`True`, the data will be
        reshuffled at every epoch. (default: :obj:`False`)
    follow_batch: List[str], optional
        Creates assignment batch
        vectors for each key in the list. (default: :obj:`None`)
    exclude_keys: List[str], optional
        Will exclude each key in the
        list. (default: :obj:`None`)
    **kwargs: optional
        Additional arguments of
        :class:`torch.utils.data.DataLoader`.
    """
    def __init__(
        self,
        dataset: Union[Dataset, List[Graph]],
        batch_size: int = 1,
        shuffle: bool = False,
        follow_batch: Optional[List[str]] = None,
        exclude_keys: Optional[List[str]] = None,
        **kwargs,
    ):

        if 'collate_fn' in kwargs:
            del kwargs['collate_fn']

        # Save for PyTorch Lightning:
        self.follow_batch = follow_batch
        self.exclude_keys = exclude_keys

        super().__init__(
            dataset,
            batch_size,
            shuffle,
            collate_fn=Collater(follow_batch, exclude_keys),
            **kwargs,
        )
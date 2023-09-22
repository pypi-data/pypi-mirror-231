import torch
import umap

from utils.soft_dtw import SoftDTW


def plot_umap(
        data,
        train_data,
        train_labels,
):
    loss_fct = SoftDTW()

    labels = torch.zeros(len(data))

    for idx, ts in enumerate(data):
        ts = ts.reshape(1, 1, ts.size(0))
        dtw = loss_fct(ts, train_data)
        arg_min = dtw.argmin()
        labels[idx] = train_labels[arg_min]

    mapper = umap.UMAP(
        n_neighbors=15,
        min_dist=0.1,
    ).fit(data.detach().cpu())

    umap.plot.points(mapper, labels=labels, background='black')

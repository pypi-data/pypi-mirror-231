"""
Utils module

The code from this file comes from:
    * https://github.com/taikiinoue45/PaDiM
"""
import torch
import numpy as np
import pandas as pd
import torch.nn.functional as F

from numpy import ndarray as NDArray
from skimage import measure
from sklearn.metrics import auc, roc_auc_score, roc_curve
from torch import Tensor


def embeddings_concat(x0: Tensor, x1: Tensor) -> Tensor:
    b0, c0, h0, w0 = x0.size()
    _, c1, h1, w1 = x1.size()
    s = h0 // h1
    x0 = F.unfold(x0, kernel_size=(s, s), dilation=(1, 1), stride=(s, s))
    x0 = x0.view(b0, c0, -1, h1, w1)
    z = torch.zeros(b0, c0 + c1, x0.size(2), h1, w1).to(x0.device)
    for i in range(x0.size(2)):
        z[:, :, i, :, :] = torch.cat((x0[:, :, i, :, :], x1), 1)
    z = z.view(b0, -1, h1 * w1)
    z = F.fold(z, kernel_size=(s, s), output_size=(h0, w0), stride=(s, s))
    return z


def mean_smoothing(amaps: Tensor, kernel_size: int = 21) -> Tensor:
    mean_kernel = torch.ones(1, 1, kernel_size, kernel_size) / kernel_size ** 2
    mean_kernel = mean_kernel.to(amaps.device)
    return F.conv2d(amaps, mean_kernel, padding=kernel_size // 2, groups=1)


def compute_roc_score(predictions, ground_truth) -> float:
    num_data = len(predictions)

    amaps = np.stack(predictions)
    y_trues = np.stack(ground_truth)

    y_scores = amaps.max(1).max(1)
    y_trues = y_trues.any(axis=1).any(axis=1)

    # Save roc_curve.csv
    # keys = [f"threshold_{i}" for i in range(len(thresholds))]
    # roc_df = pd.DataFrame({"key": keys, "fpr": fprs, "tpr": tprs, "threshold": thresholds})
    # roc_df.to_csv("roc_curve.csv", index=False)

    # Update test_dataset.csv
    # pred_csv = pd.merge(
    #     pd.DataFrame({"stem": stems, "y_score": y_scores, "y_true": y_trues}),
    #     pd.read_csv("test_dataset.csv"),
    #     on="stem",
    # )
    # for i, th in enumerate(thresholds):
    #     pred_csv[f"threshold_{i}"] = pred_csv["y_score"].apply(lambda x: 1 if x >= th else 0)
    # pred_csv.to_csv("test_dataset.csv", index=False)



    return roc_auc_score(y_trues, y_scores)


def compute_pro_score(amaps: NDArray, masks: NDArray) -> float:

    df = pd.DataFrame([], columns=["pro", "fpr", "threshold"])
    binary_amaps = np.zeros_like(amaps, dtype=np.bool)

    max_step = 200
    min_th = amaps.min()
    max_th = amaps.max()
    delta = (max_th - min_th) / max_step

    for th in tqdm(np.arange(min_th, max_th, delta), desc="compute pro"):
        binary_amaps[amaps <= th] = 0
        binary_amaps[amaps > th] = 1

        pros = []
        for binary_amap, mask in zip(binary_amaps, masks):
            for region in measure.regionprops(measure.label(mask)):
                axes0_ids = region.coords[:, 0]
                axes1_ids = region.coords[:, 1]
                TP_pixels = binary_amap[axes0_ids, axes1_ids].sum()
                pros.append(TP_pixels / region.area)

        inverse_masks = 1 - masks
        FP_pixels = np.logical_and(inverse_masks, binary_amaps).sum()
        fpr = FP_pixels / inverse_masks.sum()

        df = df.append({"pro": mean(pros), "fpr": fpr, "threshold": th}, ignore_index=True)

    df.to_csv("pro_curve.csv", index=False)
    return auc(df["fpr"], df["pro"])


def denormalize(img: NDArray) -> NDArray:

    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    img = (img * std + mean) * 255.0
    return img.astype(np.uint8)

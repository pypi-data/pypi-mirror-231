"""Set-based classification metrics"""
import numpy as np


def precision(y_true: set, y_pred: set) -> float:
    """Set-based precision"""
    if not y_pred:
        return np.nan
    tp = len(y_pred & y_true)
    fp = len(y_pred - y_true)
    return tp / (tp + fp)


def recall(y_true: set, y_pred: set) -> float:
    """Set-based recall"""
    if not y_true:
        return np.nan
    tp = len(y_pred & y_true)
    fn = len(y_true - y_pred)
    return tp / (tp + fn)

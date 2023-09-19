#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The `Collections` utility provides methods to deal with Collections (lists, dictionaries, arrays, ...)

@author: hoelken
"""

import numpy as np
from typing import Callable, Iterable


class Collections:
    """
    Static utility for handling collections.
    """

    @staticmethod
    def chunker(seq: list, size: int) -> list:
        """
        Generates chunks (slices) from a given sequence

        ### Params
        - seq: the list to chunk
        - size: the size of the chunks

        ### Returns
        A list of lists where each list has the
            length of the requested chunk size (maybe except the last one)
        """
        if size < 1:
            return [seq]
        return [seq[pos:pos + size] for pos in range(0, len(seq), size)]

    @staticmethod
    def indexed_chunks(seq: list, size: int) -> dict:
        """
        Generates indexed chunks (slices) from a given sequence
        ### Params
        - seq: List the list to chunk
        - size: Integer the size of the chunks

        ### Returns
         A dictionary with the index as key and the corresponding chunk as value.
            The length of the value arrays is the requested chunk size (maybe except the last one)
        """
        idx = 0
        indexed_chunks = {}
        for chunk in Collections.chunker(seq, size):
            indexed_chunks[idx] = chunk
            idx += 1
        return indexed_chunks

    @staticmethod
    def as_float_array(orig) -> np.array:
        """
        Creates a copy of the orig and converts all values to `float32`

        ### Params
        - orig: an object that can be converted to a list

        ### Params
        Array with float values converted from the orig
        """
        return np.array(list(orig), dtype=np.float32)

    @staticmethod
    def as_int_array(orig) -> np.array:
        """
        Creates a copy of the orig and converts all values to `int`

        ### Params
        - orig: an object that can be converted to a list

        ### Params
        Array with int values converted from the orig
        """
        return np.array(list(orig), dtype=int)

    @staticmethod
    def bin(orig: np.array, binning: list, method: Callable = np.mean) -> np.array:
        """
        Bins along a given set of axis.

        ### Params
        - orig: The original numpy array
        - binning: A list of binning values.
            - Length of the list must match the number of axis (i.e. the length of the `orig.shape`).
            - Per axis set `1` for no binning, `-1` for bin all and any positive number
                  to specify the bin size along the axis.
        - method: The function to apply to the bin (e.g. np.max for max pooling, np.mean for average)
        ### Returns
        The binned array
        """
        if np.all(np.array(binning) == 1):
            # no binning whatsoever, return original
            return orig

        if len(orig.shape) != len(binning):
            raise Exception(f"Shape {orig.shape} and number of binning axis {binning} don't match.")

        data = orig
        for ax in range(len(binning)):
            data = Collections.bin_axis(data, binning[ax], axis=ax, method=method)
        return data

    @staticmethod
    def bin_axis(data: np.array, binsize: int, axis: int = 0, method: Callable = np.mean):
        """
       Bins an array along a given axis.

       ### Params
       - data: The original numpy array
       - axis: The axis to bin along
       - binsize: The size of each bin
       - method: The function to apply to the bin (e.g. np.max for max pooling, np.mean for average)

       ### Returns
       The binned array
       """
        if binsize < 0:
            return np.array([method(data, axis=axis)])

        dims = np.array(data.shape)
        argdims = np.arange(data.ndim)
        argdims[0], argdims[axis] = argdims[axis], argdims[0]
        data = data.transpose(argdims)
        data = [method(np.take(data, np.arange(int(i * binsize), int(i * binsize + binsize)), 0), 0)
                for i in np.arange(dims[axis] // binsize)]
        data = np.array(data).transpose(argdims)
        return data

    @staticmethod
    def flatten_sort(lists: Iterable) -> list:
        """Flattens a list of lists and sorts the result"""
        result = Collections.flatten(lists)
        result.sort()
        return result

    @staticmethod
    def flatten(lists: Iterable) -> list:
        """Flattens a list of lists and sorts the result"""
        result = []
        for entry in lists:
            if isinstance(entry, (list, type(np.array))):
                result.extend(Collections.flatten(entry))
            else:
                result.append(entry)
        return result

    @staticmethod
    def remove_sigma_outliers(data: np.array, s: float = 5) -> np.array:
        """
        Removes outliers from the data set.

        :param data: The data to clean
        :param s: the factor of sigma to clean for. Default is 5 Sigma (99.99994%)
        :return: A cleaned copy of the dataset
        """
        copy = data.copy()
        mean_val = np.mean(data)
        sigma = s * np.std(data)
        copy[np.where(np.abs(data - mean_val) > sigma)] = mean_val
        return copy

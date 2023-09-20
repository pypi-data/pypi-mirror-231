"""
mean_offset
Dr Zheng & Dr Jiang, 2023-09-20

Find the rough offset of two astronomical photometric images of the same sky area with dither.

In preparation, compute the axis mean as mean_x and mean_y, as the feature of the image.
Fit the mean_x|y with an order 2 polynomial, then use it to normalize the mean_x|y,
in order to remove the background slope and the value difference.

Then compare mean from two images, one axis by one axis. 
We try to pan the data, divide one by another, we use the std of the result as the similarity index.
If the offset is the best, the result should be the  constant 1, but this happens only when comparing the same image.
The similarity index will drop sharply at the matched offset.
But a global trend will bring some trouble, with bigger offset, the common pixel will be fewer, and the std will decrease.
So we perform a moving average normalization on the std curve.
"""


import numpy as np


def mean_xy(img):
    """
    Compute the mean_x|y of the image and normalize it with a order-2 polynomial.
    :param img: 2-d image
    :returns: mean_x, mean_y
    """
    # size
    ny, nx = img.shape
    xrange = range(nx)
    yrange = range(ny)
    # get the raw mean
    mean_x0 = img.mean(axis=0)
    mean_y0 = img.mean(axis=1)
    # poly fit
    xc = np.polyfit(xrange, mean_x0, 2)
    yc = np.polyfit(yrange, mean_y0, 2)
    # normalize
    mean_x = mean_x0 / np.polyval(xc, xrange)
    mean_y = mean_y0 / np.polyval(yc, yrange)
    # end
    return mean_x, mean_y


def mean_offset1d(m1, m2, max_d=250, con_w=25, with_std=False):
    """
    Find the best offset
    :param m1, m2: mean of one axis (x or y) of image 1&2
    :param max_d: the max trial offset distance
    :param con_w: the width of the mean smooth width
    :param with_std: if true, return std curve and the best offset
    :returns: the best offset found, and std curve
    """
    # a function do offset divide and return the std
    def offset_div(i):
        if i > 0:
            d = m1[i:] / m2[:-i]
        elif i < 0:
            d = m1[:i] / m2[-i:]
        else:
            d = m1 / m2
        dm = np.mean(d)
        ds = np.std(d / dm)
        return ds
    
    # step range from -n to n
    drange = range(-max_d, max_d+1)
    # compute the std of each offset
    divstd = np.array([offset_div(i) for i in drange])
    # a mean smooth is used as the normalize factor
    # to remove the global trend
    core = np.ones(con_w)/con_w
    smoothed = np.convolve(divstd, core, mode="same")
    # the border was removed
    smoothed[:con_w] = np.nan
    smoothed[-con_w:] = np.nan
    divstd1 = divstd / smoothed
    # the minumum is the best offset
    p = np.nanargmin(divstd1) - max_d
    return (p, divstd, divstd1) if with_std else p

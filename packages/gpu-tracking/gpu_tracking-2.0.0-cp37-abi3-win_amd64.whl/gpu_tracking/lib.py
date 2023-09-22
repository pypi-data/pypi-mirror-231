from gpu_tracking import *
import pandas as pd
import numpy as np
import uuid
from .generated import *


def tiff_to_simple(src, dst):
    """
    Convert a tifffile to a "simple format" file that can be read by gpu_tracking.
    """
    try:
        import tifffile
    except:
        "Could not import tifffile. try 'pip install tifffile' to get the package"
    data = tifffile.imread(src).squeeze()
    ndim = len(data.shape)
    writer = SimpleFormatWriter(dst, data.shape)
    if ndim == 1:
        writer.write1(data)
    elif ndim == 2:
        writer.write2(data)
    elif ndim == 3:
        writer.write3(data)
    elif ndim == 4:
        writer.write4(data)
    elif ndim == 5:
        writer.write5(data)
    elif ndim == 6:
        writer.write6(data)
    else:
        raise ValueError("Can't write array with dimension greater than 6")
    
def czi_to_simple(src, dst):
    """
    Convert a czifile to a "simple format" file that can be read by gpu_tracking.
    """
    try:
        import czifile
    except:
        "Could not import czifile. try 'pip install czifile' to get the package"
    data = czifile.imread(src).squeeze()
    ndim = len(data.shape)
    writer = SimpleFormatWriter(dst, data.shape)
    if ndim == 1:
        writer.write1(data)
    elif ndim == 2:
        writer.write2(data)
    elif ndim == 3:
        writer.write3(data)
    elif ndim == 4:
        writer.write4(data)
    elif ndim == 5:
        writer.write5(data)
    elif ndim == 6:
        writer.write6(data)
    else:
        raise ValueError("Can't write array with dimension greater than 6")

def link(to_link: pd.DataFrame, search_range, memory):
    """
    Performs optimal (as opposed to greedy) nearest neighbor linking on the provided dataframe.
    
    Returns:
        pandas.DataFrame: The input dataframe with an additional column "particle", which denotes which
        particles are identical throughout frames.

    Args:
        to_link: A pandas dataframe with atleast the columns "frame", "y" and "x" and optionally "z".
        
        search_range: The upper cutoff distance for nearest neighbor linking. Currently limited to isotropic linking.
        
        memory: The number of frames that a particle is allowed to disappear before reappearing, for the purposes of linking.\
        memory = 5 means that a particle can be gone for 5 frames, reappearing in the 6th and still be linked to the\
        track it had built previously. If it had reappeared in the 7th, it would instead have been considered a new\
        particle. Defaults to 0, and has no effect if search_range is not set.
    
    """
    
    if "z" in to_link:
        to_link_np = to_link[["frame", "y", "x", "z"]].to_numpy()
    else:
        to_link_np = to_link[["frame", "y", "x"]].to_numpy()
        
    to_link_np = to_link_np.as_type("float32")
    result = link_rust(to_link_np, search_range, memory)
    output = to_link.copy()
    output["particle"] = result

    return output

def connect(to_link1: pd.DataFrame, to_link2: pd.DataFrame, search_range, merge = True):
    """
    Does linking on a frame-by-frame basis between two dataframes from different detection runs.
    This has multiple uses, such colocalizing associating detections in two separate channels,
    or evaluating a tracking algorithm by "connect"ing the predicted positions to ground truth
    detections or detections from another algorithm.

    Returns:
        pandas.DataFrame: A merged dataframe containing all the detections from the two\
        input dataframes with an additional column "connect particle", that associates detections
        from the two input dataframes. Detections that are present in, for example, dataframe 1
        but not dataframe 2 will show as having NaN for all the "_y" suffixed columns, whereas the
        inverse shows as NaNs in the "_x" suffixed columns

    Args:
        to_link1: First input dataframe
        to_link2: Second input dataframe
        search_range: The search range for linking. See :ref:`link <link>`
        merge: Whether to return a merged dataframe. Defaults to True. If False, instead returns
        the input dataframes with "connect particle" as an additional column in both.
    
    """
    def figure_out_columns(columns):
        cols = []
        frame_col = None
        if "frame" in columns:
            frame_col = 0
            cols.append("frame")
        if "z" in columns:
            pos_cols = [i + len(cols) for i in range(3)]
            cols += ["y", "x", "z"]
        else:
            pos_cols = [i + len(cols) for i in range(2)]
            cols += ["y", "x"]
        return (cols, frame_col, pos_cols)

    cols1, frame_col1, pos_cols1 = figure_out_columns(to_link1.columns)
    to_link_np1 = to_link1[cols1].to_numpy()
    
    cols2, frame_col2, pos_cols2 = figure_out_columns(to_link2.columns)
    to_link_np2 = to_link2[cols2].to_numpy()
   
    to_link_np1 = to_link_np1.astype("float32")
    to_link_np2 = to_link_np2.astype("float32")
    result = connect_rust(to_link_np1, to_link_np2, search_range, frame_col1, frame_col2, pos_cols1, pos_cols2)

    if not merge:
        return result
    else:
        output1 = pd.concat([to_link1.copy()] * (len(result[0]) // len(to_link1)))
        output1["connect particle"] = result[0]
        output2 = pd.concat([to_link2.copy()] * (len(result[1]) // len(to_link2)))
        output2["connect particle"] = result[1]
        return output1.merge(output2, how = "outer", on = "connect particle")


# def mean_from_file(path, channel = None):
#     """
#     Takes the average across frames of the provided video returns a numpy array with the result.
    
#     Args:
#         path: The file path to the video to mean
#         channel: In the case of .vsi / .ets files, the channel to mean.
    
#     Returns:
#         video: The numpy array containing the average of all frames in the video.
#     """
#     return mean_from_file_rust(path, channel)

def load(path, frames = None, channel = None):
    """
    Loads a tiff or .vsi / .ets a the provided path and returns it as a 3-dimensional numpy array.
    
    Args:
        path: The file path to the video to mean
        frames: A sequence that specifies what frames from the video to load. For example, to only load the first 50 frames of a video, frames = range(50) can be supplied.
        channel: In the case of .vsi / .ets files, the channel to mean.
    
    Returns:
        video: The numpy array containing the average of all frames in the video.
    """
    return load_rust(path, frames, channel) 
    

def annotate_image(image, tracked_df, figax = None, r = None, frame = None, imshow_kw = {}, circle_kw = {}, subplot_kw = {}):
    import matplotlib.pyplot as plt

    circle_kw = {"fill": False, **circle_kw}
    if frame is not None:
        subset_df = tracked_df[tracked_df["frame"] == frame]
    else:
        subset_df = tracked_df
    
    if r is None and not "r" in subset_df:
        r = 5
        print(f"Using default r of {r}")
    if figax is None:
        fig, ax = plt.subplots(**subplot_kw)
    else:
        fig, ax = figax
    ax.imshow(image, **imshow_kw)

    for _idx, row in subset_df.iterrows():
        if r is None:
            inner_r = row["r"]
        else:
            inner_r = r
        x, y = row["x"], row["y"]
        ax.add_patch(plt.Circle((x, y), inner_r, **circle_kw))
    return (fig, ax)

def annotate_image_plotly(image, tracked_df, r = None, frame = None, imshow_kw = {}, circle_color = "white", color_scale = "viridis", circle_kw = {}):
    from plotly import express as px
    
    if frame is not None:
        subset_df = tracked_df[tracked_df["frame"] == frame]
    else:
        subset_df = tracked_df
    
    if r is None and "r" not in subset_df:
        r = 5
        print(f"Using default r of {r}")
    fig = px.imshow(image, color_continuous_scale = color_scale, **imshow_kw)

    for _idx, row in subset_df.iterrows():
        if r is None:
            inner_r = row["r"]
        else:
            inner_r = r
        x, y = row["x"], row["y"]
        fig.add_shape(
            type = "circle", xref = "x", yref = "y",
            x0 = x - inner_r, y0 = y - inner_r,
            x1 = x + inner_r, y1 = y + inner_r,
            line_color = circle_color, line_width = 1, **circle_kw
        )
    return fig

def annotate_video(video, tracked_df, frame = 0, **kwargs):
    image = video[frame]
    return annotate_image(image, tracked_df, frame = frame, **kwargs)

def annotate_file(path, tracked_df, ets_channel = 0, frame = 0, **kwargs):
    image = load(path, ets_channel = ets_channel, keys = [frame])[0]
    return annotate_image(image, tracked_df, frame = frame, **kwargs)

def unique_particle_ids(df, column = "particle"):
    id = uuid.uuid4()
    df[column] = df[column].as_type("str") + id
    

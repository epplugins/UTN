# This work © 2024 by Edgardo Palazzo (epalazzo@fra.utn.edu.ar)
# is licensed under CC BY-NC-SA 4.0

# Librería de funciones para cálculos sencillos de electromagnetismo.

import numpy as np
import matplotlib.pyplot as plt


# TODO: remove warnings divide by zero.
def plotE(X,Y,Z,Ei,Ej,Ek, E, axs = [], figsize=(8,8), title = ''):
    """Shows a 3D plot of a frame

    Parameters
    ----------
    image : numpy array
        L x L image
    axs : matplotlib axes object
    figsize: tuple
        matplotlib parameter
    x0,y0 : int
        For displaying the correct coordinates.
    title : string
        Plot title

    Returns
    -------
    matplotlib axes object
    """

    w = 4
    num = 9j
    Y, X = np.mgrid[-w:w:num, -w:w:num]
    Z = 0*X
    Ei, Ej, Ek = E(X,Y,Z)
    mE = np.sqrt(Ei**2 + Ej**2)

    fig, axs = plt.subplots(1, 1, figsize=(4, 4))

    #  Varying density along a streamline
    # axs.streamplot(X, Y, U, V, density=[0.5, 1])
    # axs.set_title('Varying Density')

    # # Varying color along a streamline
    strm = axs.streamplot(X, Y, Ei, Ej, color=mE, linewidth=1, cmap='inferno')
    fig.colorbar(strm.lines)
    axs.set_title('Varying Color')

    # if not axs:
    #     fig = plt.figure(figsize=figsize)
    #     axs = fig.add_subplot(111, projection='3d', facecolor=(1, 1, 1))

    # return axs
    return True




# def potentialPeaksSingle(frame, nFrame, peaks = [], singleuse = False, **params):
#     """Finds all blobs that are potential spots in a single frame.

#     Parameters
#     ----------
#     frame :

#     nFrame : int
#         Frame number.

#     peaks : pandas.DataFrame

#     singleuse : bool
#         To be used for a single frame, instead of processing a full MRC movie.

#     Other parameters
#     ----------------
#     See potentialPeaks().

#     Returns
#     -------
#     pandas.DataFrame
#         Multi array .. to be completed.
#     """

#     ###################
#     # Parameters tunning
#     # Hardcoded parameters for different functions.
#     # Possible tunning using params.

#     firstBinaryThresholdShare = params.get('firstBinaryThresholdShare', 0.95) # Threshold keeps only upper 5% intensities, default value
#     sigmaGaussGradient = params.get('sigmaGaussGradient', 3.0) # Edge highlighting
#     finalBinaryThresholdShare = params.get('finalBinaryThresholdShare', 0.998) # discards proportion of pixels below
#     expandR = params.get('expandR', 1) #factor to expand area for refinning centroids
#     radiusMultiplier = params.get('radiusMultiplier', 1)
#     perimWidth = params.get('perimWidth', 5)  #pixels to enlarge perimeter area for background removal
#     removeoutliers = params.get('removeoutliers', False)  #pixels to enlarge perimeter area for background removal

#     #parameters of blobsFindLaplacianOfGaussian
#     min_sigma = params.get('min_sigma', 15.5)
#     max_sigma= params.get('max_sigma', 20)
#     num_sigma= params.get('num_sigma', 1)
#     threshold= params.get('threshold', 0.1)
#     overlap= params.get('overlap', 0.0005)

#     # Others
#     xyref = params.get('xyref', [np.nan, np.nan])       #tuple (x,y) : coordinates of center in frame of reference.
#     top_center = params.get('top_center', 1.0)   # Intensity top percentage of pixels analized for centroid adjustments, in centerBlob.
#     gpuenabled = params.get('gpuenabled', True)

#     #end parameters tunning
#     ########################

#     firstBinaryThresholded = binQuantThr(frame, firstBinaryThresholdShare)
#     gaussianGradientArray = edgesHighlightingGradient(firstBinaryThresholded, sigmaGaussGradient)
#     arrayErosionHard = erosionHardEdges(gaussianGradientArray)
#     finalBinaryThresholded = binQuantThr(arrayErosionHard, finalBinaryThresholdShare)

#     blobs_log = blobsFindLaplacianOfGaussian(finalBinaryThresholded, min_sigma,
#                                              max_sigma, num_sigma, threshold, overlap)
#     blobs_log = centerBlob(frame, blobs_log, expandR, top_center, nFrame)
#     #Adding deltas to blobs_log: columns 4 and 5 now have the displacements
#     #from the frame of reference.
#     if blobs_log.shape[0]>0:
#         if np.any(np.isnan(xyref)):
#             correction = [np.nan, np.nan]
#         else:
#             xyn = autocenter(inFrame)
#             correction = xyn-xyref

#         deltas = np.array([correction]*blobs_log.shape[0])
#         blobs_log = np.concatenate([blobs_log,deltas],1)

#     else:
#         blobs_log = np.array([]).reshape([0,6])

#     # each row of blobs_log at this point:
#     # [x, y , radius, intensity, dx, dy]

#     # The next function takes:
#     # blobs_log, a list with some info about the blobs of the
#     # current frame,
#     # and modifies peaks, a pandas dataframe with info about
#     # all peaks in all frames so far.
#     if singleuse:
#         blobs_out = np.array([]).reshape([0,11])
#         for blob in blobs_log:
#             r, intensity, background, background_var, fitted, fit_error = singleBlobIntensityIntegration(blob, radiusMultiplier, frame, perimWidth, removeoutliers)
#             blobs_out = np.append(blobs_out, [[nFrame, blob[0], blob[1], blob[4], blob[5],
#                r, intensity, background, background_var, fitted, fit_error]], axis=0)
#         return blobs_out
#     else:
#         listBlobsIntensities(blobs_log, peaks, nFrame, frame, perimWidth,
#                          radiusMultiplier, removeoutliers)
#         return peaks


# This work © 2024 by Edgardo Palazzo (epalazzo@fra.utn.edu.ar)
# is licensed under CC BY-NC-SA 4.0

# Librería de funciones para cálculos sencillos de electromagnetismo.

import numpy as np
import matplotlib.pyplot as plt


# TODO: remove warnings divide by zero. Return axs, add
# more control over plotting parameters.
# Add examples in the docstring.
def plotE(E, dx, **params):
    """
    Muestra las líneas de campo en 2D.

    Parameters
    ----------
    E : function
        Una función de un campo vectorial (3 variables que devuelve 3 componentes).
    dx : float
        Se produce una grilla con -dx <= x <= dx. Si dy = 0,
        se usan los mismos intervalos para esa variable: -dx <= y <= dx.
    dy : float
        Cuando no son 0, la grilla puede tener distintas magnitudes en cada dimensión.
    w : integer
        Cantidad de particiones de cada dimensión en la grilla.
    axs : matplotlib axes object

    *Además de los parámetros de matplotlib y streamplot, por ejemplo:*
    figsize : tuple
    title : string
    """

    dy = params.get('dy', 0)
    w = params.get('w', 100)

    figsize = params.get('figsize', (4,4))
    title = params.get('title', 'Líneas de campo')
    linewidth = params.get('linewidth', 0.4)
    density = params.get('density', 0.7)

    # Convirtiendo w a número complejo se incluye el extremo del intervalo en mgrid.
    w = w * 1j
    if (dy==0):
        dy = dx
    Y, X = np.mgrid[-dx:dx:w, -dy:dy:w]
    Z = 0*X
    Ei, Ej, Ek = E(X,Y,Z)
    # Módulo de E:
    mE = np.sqrt(Ei**2 + Ej**2)

    fig, axs = plt.subplots(1, 1, figsize=figsize)

    strm = axs.streamplot(X, Y, Ei, Ej, color='b',
                        linewidth=linewidth, density=density)
    axs.set_title(title)
    axs.set_xlabel('$x$ [m]')
    axs.set_ylabel('$y$ [m]')


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

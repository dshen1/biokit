""".. rubric:: Hinton plot

:author: Thomas Cokelaer
"""


__all__ = ['hinton']


def hinton(df, fig=1, shrink=2, method='square', bgcolor='grey',
        cmap='gray_r', binarise_color=True):
    """Hinton plot (simplified version of correlation plot)

    :param df: the input data as a dataframe or list of items (list, array). See
        :class:`~biokit.viz.corrplot.Corrplot` for details.
    :param fig: in which figure to plot the data
    :param shrink: factor to increase/decrease sizes of the symbols
    :param method: set the type of symbols for each coordinates. (default to square). See
        :class:`~biokit.viz.corrplot.Corrplot` for more details.
    :param bgcolor: set the background and label colors as grey
    :param cmap: gray color map used by default
    :param binarise_color: use only two colors. One for positive values and one for
        negative values.

    .. plot::
        :include-source:
        :width: 80%

        from biokit.viz import hinton
        df = np.random.rand(20, 20) - 0.5
        hinton(df)


    .. note:: Idea taken from a matplotlib recipes
        http://matplotlib.org/examples/specialty_plots/hinton_demo.html
        but solely using the implementation within :class:`~biokit.viz.corrplot.Corrplot`

    .. seealso:: :class:`biokit.viz.corrplot.Corrplot`

    .. note:: Values must be between -1 and 1. No sanity check performed.
    """
    from biokit.viz import corrplot
    c = corrplot.Corrplot(df)
    c.plot(colorbar=False, cmap=cmap, fig=fig,
            method=method, axisbg=bgcolor,
            shrink=shrink, label_color=bgcolor, binarise_color=binarise_color)





#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Artificial Intelligence & Data Science Studio                                       #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.12                                                                             #
# Filename   : /studioai/visual/visualizer.py                                                      #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/studioai                                           #
# ------------------------------------------------------------------------------------------------ #
# Created    : Saturday August 26th 2023 06:25:27 am                                               #
# Modified   : Monday September 18th 2023 05:24:42 am                                              #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2023 John James                                                                 #
# ================================================================================================ #
"""Wrapper for several Seaborn plotting functions."""
from __future__ import annotations
from dataclasses import dataclass
from typing import List, Union
import math
import logging

import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from studioai.visual.base import Canvas, Colors
from studioai.visual.base import Visualizer as VisualizerABC
from studioai.data.dataclass import DataClass

# ------------------------------------------------------------------------------------------------ #
logger = logging.getLogger(__name__)


# ------------------------------------------------------------------------------------------------ #
#                                            PALETTES                                              #
# ------------------------------------------------------------------------------------------------ #
@dataclass
class Palettes(DataClass):
    blues: str = "Blues"
    blues_r: str = "Blues_r"
    mako: str = "mako"
    bluegreen: str = "crest"
    paired: str = "Paired"
    dark: str = "dark"
    colorblind: str = "colorblind"
    darkblue = sns.dark_palette("#69d", reverse=False, as_cmap=False)
    darkblue_r = sns.dark_palette("#69d", reverse=True, as_cmap=False)
    winter_blue = sns.color_palette(
        [Colors.cool_black, Colors.police_blue, Colors.teal_blue, Colors.pale_robin_egg_blue],
        as_cmap=True,
    )
    blue_orange = sns.color_palette(
        [Colors.russian_violet, Colors.dark_cornflower_blue, Colors.meat_brown, Colors.peach],
        as_cmap=True,
    )


# ------------------------------------------------------------------------------------------------ #
#                                            CANVAS                                                #
# ------------------------------------------------------------------------------------------------ #


@dataclass
class SeabornCanvas(Canvas):
    """SeabornCanvas class encapsulating figure level configuration."""

    width: int = 12  # The maximum width of the canvas
    height: int = 4  # The height of a single row.
    maxcols: int = 2  # The maximum number of columns in a multi-plot visualization.
    color = Colors().dark_blue
    palette = Palettes().blues_r  # Seaborn palette or matplotlib colormap
    style: str = "whitegrid"  # A Seaborn aesthetic
    saturation: float = 0.5
    fontsize: int = 10
    fontsize_title: int = 16
    colors: Colors = Colors()
    palettes: Palettes = Palettes()

    def get_figaxes(
        self, nplots: int = 1, figsize: tuple = None
    ) -> SeabornCanvas:  # pragma: no cover
        """Configures the figure and axes objects.

        Args:
            nplots (int): The number of plots to be rendered on the canvas.
            figsize (tuple[int,int]): Plot width and row height.
        """
        figsize = figsize or (self.width, self.height)

        if nplots == 1:
            fig, axes = plt.subplots(figsize=figsize)
        else:
            nrows = math.ceil(nplots / self.maxcols)
            ncols = min(self.maxcols, nplots)

            fig = plt.figure(layout="constrained", figsize=figsize)
            gs = GridSpec(nrows=nrows, ncols=ncols, figure=fig)

            axes = []
            for idx in range(nplots):
                row = int(idx / ncols)
                col = idx % ncols

                if idx < nplots - 1:
                    ax = fig.add_subplot(gs[row, col])
                else:
                    ax = fig.add_subplot(gs[row, col:])
                axes.append(ax)

        return fig, axes


# ------------------------------------------------------------------------------------------------ #
class Visualizer(VisualizerABC):  # pragma: no cover
    """Wrapper for Seaborn plotizations."""

    def __init__(self, canvas: SeabornCanvas = SeabornCanvas()):
        super().__init__(canvas)

    def lineplot(
        self,
        data: Union[pd.DataFrame, np.ndarray] = None,
        x: str = None,
        y: str = None,
        hue: str = None,
        title: str = None,
        ax: plt.Axes = None,
        *args,
        **kwargs,
    ) -> None:
        """Draw a line plot with possibility of several semantic groupings.

        The relationship between x and y can be shown for different subsets of the data using the
        hue, size, and style parameters. These parameters control what visual semantics are used to
        identify the different subsets. It is possible to show up to three dimensions independently
        by using all three semantic types, but this style of plot can be hard to interpret and is
        often ineffective. Using redundant semantics (i.e. both hue and style for the same variable)
        can be helpful for making graphics more accessible.

        Args:
            data (Union[pd.DataFrame, np.ndarray]): Input data structure. Either a long-form
                collection of vectors that can be assigned to named variables or a wide-form dataset
                that will be internally reshaped
            x,y (str): Keys in data.
            hue (str): Grouping variable that will produce lines with different colors. Can be either categorical or numeric, although color mapping will behave differently in latter case.
            title (str): Title for the plot. Optional
            ax: (plt.Axes): A matplotlib Axes object. Optional. If not provide, one will be obtained from the canvas.


        """
        palette = self._canvas.palette if hue is not None else None
        data = data if data is not None else self._data

        if ax is None:
            fig, ax = self._canvas.get_figaxes()

        sns.lineplot(
            data=data,
            x=x,
            y=y,
            hue=hue,
            ax=ax,
            palette=palette,
            *args,
            **kwargs,
        )
        if title is not None:
            ax.set_title(title)

    def scatterplot(
        self,
        data: Union[pd.DataFrame, np.ndarray] = None,
        x: str = None,
        y: str = None,
        hue: str = None,
        title: str = None,
        ax: plt.Axes = None,
        *args,
        **kwargs,
    ) -> None:
        """Draw a scatter plot with possibility of several semantic groupings.

        The relationship between x and y can be shown for different subsets of the data using the
        hue, size, and style parameters. These parameters control what visual semantics are used to
        identify the different subsets. It is possible to show up to three dimensions independently
        by using all three semantic types, but this style of plot can be hard to interpret and is
        often ineffective. Using redundant semantics (i.e. both hue and style for the same variable)
        can be helpful for making graphics more accessible.

        Args: Args:
            data (Union[pd.DataFrame, np.ndarray]): Input data structure. Either a long-form
                collection of vectors that can be assigned to named variables or a wide-form dataset
                that will be internally reshaped
            x,y (str): Keys in data.
            hue (str): Grouping variable that will produce lines with different colors. Can be either categorical or numeric, although color mapping will behave differently in latter case.
            title (str): Title for the plot. Optional
            ax: (plt.Axes): A matplotlib Axes object. Optional. If not provide, one will be obtained from the canvas.


        """
        palette = self._canvas.palette if hue is not None else None
        data = data if data is not None else self._data

        if ax is None:
            fig, ax = self._canvas.get_figaxes()

        sns.scatterplot(
            data=data,
            x=x,
            y=y,
            hue=hue,
            ax=ax,
            palette=palette,
            *args,
            **kwargs,
        )
        if title is not None:
            ax.set_title(title)

    def histogram(
        self,
        data: Union[pd.DataFrame, np.ndarray] = None,
        x: str = None,
        y: str = None,
        hue: str = None,
        stat: str = "density",
        element: str = "bars",
        fill: bool = True,
        title: str = None,
        ax: plt.Axes = None,
        *args,
        **kwargs,
    ) -> None:
        """Draw a scatter plot with possibility of several semantic groupings.

        The relationship between x and y can be shown for different subsets of the data using the
        hue, size, and style parameters. These parameters control what visual semantics are used to
        identify the different subsets. It is possible to show up to three dimensions independently
        by using all three semantic types, but this style of plot can be hard to interpret and is
        often ineffective. Using redundant semantics (i.e. both hue and style for the same variable)
        can be helpful for making graphics more accessible.

        Args:
            data (Union[pd.DataFrame, np.ndarray]): Input data structure. Either a long-form
                collection of vectors that can be assigned to named variables or a wide-form dataset
                that will be internally reshaped
            x,y (str): Keys in data.
            hue (str): Grouping variable that will produce lines with different colors. Can be either categorical or numeric, although color mapping will behave differently in latter case.
            title (str): Title for the plot. Optional
            stat (str): Aggregate statistics for each bin. Optional. Default is 'density'.
                See https://seaborn.pydata.org/generated/seaborn.histplot.html for valid values.
            element (str): Visual representation of the histogram statistic. Only relevant with univariate data. Optional. Default is 'bars'. fill (bool): If True, fill in the space under the histogram. Only relevant with univariate data.
            ax: (plt.Axes): A matplotlib Axes object. Optional. If not provide, one will be obtained from the canvas.


        """
        palette = self._canvas.palette if hue is not None else None
        data = data if data is not None else self._data

        if ax is None:
            fig, ax = self._canvas.get_figaxes()

        sns.histplot(
            data=data,
            x=x,
            y=y,
            hue=hue,
            stat=stat,
            element=element,
            fill=fill,
            ax=ax,
            palette=palette,
            *args,
            **kwargs,
        )
        if title is not None:
            ax.set_title(title)

    def boxplot(
        self,
        data: Union[pd.DataFrame, np.ndarray] = None,
        x: str = None,
        y: str = None,
        hue: str = None,
        title: str = None,
        ax: plt.Axes = None,
        *args,
        **kwargs,
    ) -> None:
        """Draw a box plot to show distributions with respect to categories.

        A box plot (or box-and-whisker plot) shows the distribution of quantitative data in a way
        that facilitates comparisons between variables or across levels of a categorical variable.
        The box shows the quartiles of the dataset while the whiskers extend to show the rest of the
        distribution, except for points that are determined to be “outliers” using a method that is
        a function of the inter-quartile range.

        Args:
            data (Union[pd.DataFrame, np.ndarray]): Input data structure. Either a long-form
                collection of vectors that can be assigned to named variables or a wide-form dataset
                that will be internally reshaped
            x,y (str): Keys in data.
            hue (str): Grouping variable that will produce lines with different colors. Can be either categorical or numeric, although color mapping will behave differently in latter case.
            title (str): Title for the plot. Optional
            ax: (plt.Axes): A matplotlib Axes object. Optional. If not provide, one will be obtained from the canvas.


        """
        palette = self._canvas.palette if hue is not None else None
        data = data if data is not None else self._data

        if ax is None:
            fig, ax = self._canvas.get_figaxes()

        sns.boxplot(
            data=data,
            x=x,
            y=y,
            hue=hue,
            ax=ax,
            palette=palette,
            *args,
            **kwargs,
        )
        if title is not None:
            ax.set_title(title)

    def countplot(
        self,
        data: Union[pd.DataFrame, np.ndarray] = None,
        x: str = None,
        y: str = None,
        hue: str = None,
        orient: str = None,
        title: str = None,
        ax: plt.Axes = None,
        *args,
        **kwargs,
    ) -> None:
        """Show the counts of observations in each categorical bin using bars.

        A count plot can be thought of as a histogram across a categorical, instead of quantitative, variable. The basic API and options are identical to those for barplot(), so you can compare counts across nested variables.

        Args:
            data (Union[pd.DataFrame, np.ndarray]): Input data structure. Either a long-form
                collection of vectors that can be assigned to named variables or a wide-form dataset
                that will be internally reshaped
            x,y (str): Keys in data.
            hue (str): Grouping variable that will produce lines with different colors. Can be either categorical or
                numeric, although color mapping will behave differently in latter case.
            orient (str): 'v' or 'h'. Orientation of the plot (vertical or horizontal). This is usually
                inferred based on the type of the input variables, but it can be used to resolve ambiguity
                when both x and y are numeric or when plotting wide-form data.
            title (str): Title for the plot. Optional
            ax: (plt.Axes): A matplotlib Axes object. Optional. If not provide, one will be obtained from the canvas.


        """
        palette = self._canvas.palette if hue is not None else "Blues_r"
        data = data if data is not None else self._data
        total = len(data)
        if orient is None:
            if x is None and y is not None:
                orient = "h"
            else:
                orient = "v"

        if ax is None:
            fig, ax = self._canvas.get_figaxes()

        sns.countplot(
            data=data,
            x=x,
            y=y,
            hue=hue,
            ax=ax,
            palette=palette,
            *args,
            **kwargs,
        )
        if orient == "v":
            for p in ax.patches:
                x = p.get_bbox().get_points()[:, 0]
                y = p.get_bbox().get_points()[1, 1]
                ax.annotate(
                    text=f"{round(y,0)}\n({round(y/total*100,1)}%)",
                    xy=(x.mean(), y),
                    ha="center",
                    va="bottom",
                )
        else:
            for p in ax.patches:
                x = p.get_x() + p.get_width() / 2
                y = p.get_y() + p.get_height() / 2
                ax.annotate(
                    text=f"{round(p.get_width(),0)} ({round(p.get_width()/total*100,1)}%)",
                    xy=(x, y),
                    va="center",
                )

        if title is not None:
            ax.set_title(title)

    def barplot(
        self,
        data: Union[pd.DataFrame, np.ndarray] = None,
        x: str = None,
        y: str = None,
        hue: str = None,
        orient: str = None,
        title: str = None,
        ax: plt.Axes = None,
        *args,
        **kwargs,
    ) -> None:
        """Show point estimates and errors as rectangular bars.

        A bar plot represents an estimate of central tendency for a numeric variable with the height of each
        rectangle and provides some indication of the uncertainty around that estimate using error bars. Bar
        plots include 0 in the quantitative axis range, and they are a good choice when 0 is a meaningful
        value for the quantitative variable, and you want to make comparisons against it.

        Args:
            data (Union[pd.DataFrame, np.ndarray]): Input data structure. Either a long-form
                collection of vectors that can be assigned to named variables or a wide-form dataset
                that will be internally reshaped
            x,y (str): Keys in data.
            hue (str): Grouping variable that will produce lines with different colors. Can be either categorical or numeric, although color mapping will behave differently in latter case.
            orient (str): 'v' or 'h'. Orientation of the plot (vertical or horizontal). This is usually
                inferred based on the type of the input variables, but it can be used to resolve ambiguity
                when both x and y are numeric or when plotting wide-form data.
            title (str): Title for the plot. Optional
            ax: (plt.Axes): A matplotlib Axes object. Optional. If not provide, one will be obtained from the canvas.

        """
        palette = self._canvas.palette if hue is not None else None
        data = data if data is not None else self._data

        if ax is None:
            fig, ax = self._canvas.get_figaxes()

        sns.barplot(
            data=data,
            x=x,
            y=y,
            hue=hue,
            ax=ax,
            palette=palette,
            *args,
            **kwargs,
        )

        if title is not None:
            ax.set_title(title)

        if hue is not None:
            plt.legend(loc="upper right")

    def kdeplot(
        self,
        data: Union[pd.DataFrame, np.ndarray] = None,
        x: str = None,
        y: str = None,
        hue: str = None,
        title: str = None,
        ax: plt.Axes = None,
        *args,
        **kwargs,
    ) -> None:
        """Plot univariate or bivariate distributions using kernel density estimation.

        A kernel density estimate (KDE) plot is a method for visualizing the distribution of
        observations in a dataset, analogous to a histogram. KDE represents the data using a
        continuous probability density curve in one or more dimensions.

        Args:
            data (Union[pd.DataFrame, np.ndarray]): Input data structure. Either a long-form
                collection of vectors that can be assigned to named variables or a wide-form dataset
                that will be internally reshaped
            x,y (str): Keys in data.
            hue (str): Grouping variable that will produce lines with different colors. Can be either categorical or numeric, although color mapping will behave differently in latter case.
            title (str): Title for the plot. Optional
            ax: (plt.Axes): A matplotlib Axes object. Optional. If not provide, one will be obtained from the canvas.


        """
        palette = self._canvas.palette if hue is not None else None
        data = data if data is not None else self._data

        if ax is None:
            fig, ax = self._canvas.get_figaxes()

        sns.kdeplot(
            data=data,
            x=x,
            y=y,
            hue=hue,
            ax=ax,
            palette=palette,
            *args,
            **kwargs,
        )
        if title is not None:
            ax.set_title(title)

    def ecdfplot(
        self,
        data: Union[pd.DataFrame, np.ndarray] = None,
        x: str = None,
        y: str = None,
        hue: str = None,
        title: str = None,
        ax: plt.Axes = None,
        *args,
        **kwargs,
    ) -> None:
        """Plot empirical cumulative distribution functions.

        An ECDF represents the proportion or count of observations falling below each unique value
        in a dataset. Compared to a histogram or density plot, it has the advantage that each
        observation is visualized directly, meaning that there are no binning or smoothing
        parameters that need to be adjusted. It also aids direct comparisons between multiple
        distributions. A downside is that the relationship between the appearance of the plot and
        the basic properties of the distribution (such as its central tendency, variance, and the
        presence of any bimodality) may not be as intuitive.

        Args:
            data (Union[pd.DataFrame, np.ndarray]): Input data structure. Either a long-form
                collection of vectors that can be assigned to named variables or a wide-form dataset
                that will be internally reshaped
            x,y (str): Keys in data.
            hue (str): Grouping variable that will produce lines with different colors. Can be either categorical or numeric, although color mapping will behave differently in latter case.
            title (str): Title for the plot. Optional
            ax: (plt.Axes): A matplotlib Axes object. Optional. If not provide, one will be obtained from the canvas.

        """
        palette = self._canvas.palette if hue is not None else None
        data = data if data is not None else self._data

        if ax is None:
            fig, ax = self._canvas.get_figaxes()

        sns.ecdfplot(
            data=data,
            x=x,
            y=y,
            hue=hue,
            ax=ax,
            palette=palette,
            *args,
            **kwargs,
        )
        if title is not None:
            ax.set_title(title)

    def violinplot(
        self,
        data: Union[pd.DataFrame, np.ndarray] = None,
        x: str = None,
        y: str = None,
        hue: str = None,
        title: str = None,
        ax: plt.Axes = None,
        *args,
        **kwargs,
    ) -> None:
        """Draw a combination of boxplot and kernel density estimate.

        A violin plot plays a similar role as a box and whisker plot. It shows the distribution of
        quantitative data across several levels of one (or more) categorical variables such that those
        distributions can be compared. Unlike a box plot, in which all of the plot components correspond to
        actual datapoints, the violin plot features a kernel density estimation of the underlying
        distribution.

        Args:
            data (Union[pd.DataFrame, np.ndarray]): Input data structure. Either a long-form
                collection of vectors that can be assigned to named variables or a wide-form dataset
                that will be internally reshaped
            x,y (str): Keys in data.
            hue (str): Grouping variable that will produce lines with different colors. Can be either categorical or numeric, although color mapping will behave differently in latter case.
            title (str): Title for the plot. Optional
            ax: (plt.Axes): A matplotlib Axes object. Optional. If not provide, one will be obtained from the canvas.


        """
        palette = self._canvas.palette if hue is not None else None
        data = data if data is not None else self._data

        if ax is None:
            fig, ax = self._canvas.get_figaxes()

        sns.violinplot(
            data=data,
            x=x,
            y=y,
            hue=hue,
            ax=ax,
            palette=palette,
            *args,
            **kwargs,
        )
        if title is not None:
            ax.set_title(title)

    def regplot(
        self,
        data: Union[pd.DataFrame, np.ndarray] = None,
        x: str = None,
        y: str = None,
        title: str = None,
        ax: plt.Axes = None,
        *args,
        **kwargs,
    ) -> None:
        """Plot data and a linear regression model fit.

        Args:
            data (Union[pd.DataFrame, np.ndarray]): Input data structure. Either a long-form
                collection of vectors that can be assigned to named variables or a wide-form dataset
                that will be internally reshaped
            x,y (str): Keys in data.
            title (str): Title for the plot. Optional
            ax: (plt.Axes): A matplotlib Axes object. Optional. If not provide, one will be obtained from the canvas.


        """
        data = data if data is not None else self._data

        if ax is None:
            fig, ax = self._canvas.get_figaxes()

        sns.regplot(
            data=data,
            x=x,
            y=y,
            ax=ax,
            fit_reg=True,
            color=self._canvas.colors.dark_blue,
            *args,
            **kwargs,
        )
        if title is not None:
            ax.set_title(title)

    def pdfcdfplot(
        self,
        data: Union[pd.DataFrame, np.ndarray] = None,
        x: str = None,
        y: str = None,
        title: str = None,
        ax: plt.Axes = None,
        *args,
        **kwargs,
    ) -> None:
        """Renders a combination of the probabiity density and cumulative distribution functions.

        This visualization provides the probability density function and cumulative distribution
        function in a single plot with shared x-axis.

        Args:
            data (Union[pd.DataFrame, np.ndarray]): Input data structure. Either a long-form
                collection of vectors that can be assigned to named variables or a wide-form dataset
                that will be internally reshaped
            x,y (str): Keys in data.numeric, although color mapping will behave differently in latter case.
            title (str): Title for the plot. Optional
            ax: (plt.Axes): A matplotlib Axes object. Optional. If not provide, one will be obtained from the canvas.



        """
        data = data if data is not None else self._data

        if ax is None:
            fig, ax1 = self._canvas.get_figaxes()

        ax1 = sns.kdeplot(
            data=data,
            x=x,
            y=y,
            color=self._canvas.colors.dark_blue,
            ax=ax1,
            label="Probability Density Function",
            legend=True,
        )
        ax2 = ax1.twinx()
        ax2 = sns.kdeplot(
            data=data,
            x=x,
            y=y,
            cumulative=True,
            ax=ax2,
            color=self._canvas.colors.orange,
            label="Cumulative Distribution Function",
            legend=True,
        )
        title = "Probability Density Function and Cumulative Distribution Function"

        h1, l1 = ax1.get_legend_handles_labels()
        h2, l2 = ax2.get_legend_handles_labels()

        ax1.legend(handles=h1 + h2, labels=l1 + l2, loc="upper left")
        fig.suptitle(title, fontsize=self._canvas.fontsize_title)
        fig.tight_layout()

    def pairplot(
        self,
        data: Union[pd.DataFrame, np.ndarray] = None,
        vars: list = None,
        hue: str = None,
        title: str = None,
        *args,
        **kwargs,
    ) -> None:
        """Plot pairwise relationships in a dataset.

        By default, this function will create a grid of Axes such that each numeric variable in data
        will by shared across the y-axes across a single row and the x-axes across a single column.
        The diagonal plots are treated differently: a univariate distribution plot is drawn to show
        the marginal distribution of the data in each column.

        It is also possible to show a subset of variables or plot different variables on the rows
        and columns.

        Args:
            data (Union[pd.DataFrame, np.ndarray]): Input data structure.
                Either a long-form collection of vectors that can be assigned to named variables or
                a wide-form dataset that will be internally reshaped
            vars (list): Variables within data to use, otherwise use every column with a numeric datatype. Optional, if not provided all numeric columns will be included.
            hue (str): Grouping variable that will produce lines with different colors. Can be
            either categorical or numeric, although color mapping will behave differently in latter case.
            title (str): Title for the plot. Optional


        """
        palette = self._canvas.palette if hue is not None else None
        data = data if data is not None else self._data

        g = sns.pairplot(
            data=data,
            vars=vars,
            hue=hue,
            palette=palette,
            *args,
            **kwargs,
        )
        if title is not None:
            g.fig.suptitle(title)
        g.tight_layout()

    def jointplot(
        self,
        data: Union[pd.DataFrame, np.ndarray] = None,
        x: str = None,
        y: str = None,
        hue: str = None,
        title: str = None,
        *args,
        **kwargs,
    ) -> None:
        """Draw a plot of two variables with bivariate and univariate graphs.

        Args:
            data (Union[pd.DataFrame, np.ndarray]): Input data structure. Either a long-form
                collection of vectors that can be assigned to named variables or a wide-form dataset
                that will be internally reshaped
            x,y (str): Keys in data.
            hue (str): Grouping variable that will produce lines with different colors. Can be either categorical or numeric, although color mapping will behave differently in latter case.
            title (str): Title for the plot. Optional


        """

        palette = self._canvas.palette if hue is not None else None
        data = data if data is not None else self._data

        g = sns.jointplot(
            data=data,
            x=x,
            y=y,
            hue=hue,
            palette=palette,
            *args,
            **kwargs,
        )
        if title is not None:
            g.fig.suptitle(title)
        g.fig.tight_layout()

    def ttestplot(
        self,
        statistic: float,
        dof: int,
        result: str = None,
        alpha: float = 0.05,
        title: str = None,
        ax: plt.Axes = None,
        *args,
        **kwargs,
    ) -> None:
        """Draw the results of a t-test with the statistic and reject regions.

        Args:
            statistic (float): The student's t test statistic
            dof (int): Degrees of freedom
            alpha (float): The statistical significance. Default is 0.05.
            title (str): Title for the plot. Optional
            ax: (plt.Axes): A matplotlib Axes object. Optional. If not provide, one will be obtained from the canvas.


        """
        if ax is None:
            fig, ax = self._canvas.get_figaxes()

        # Render the probability distribution
        x = np.linspace(stats.t.ppf(0.001, dof), stats.t.ppf(0.999, dof), 500)
        y = stats.t.pdf(x, dof)
        ax = sns.lineplot(x=x, y=y, markers=False, dashes=False, sort=True, ax=ax)

        # Compute reject region
        lower = x[0]
        upper = x[-1]
        lower_alpha = alpha / 2
        upper_alpha = 1 - (alpha / 2)
        lower_critical = stats.t.ppf(lower_alpha, dof)
        upper_critical = stats.t.ppf(upper_alpha, dof)

        # Fill lower tail
        xlower = np.arange(lower, lower_critical, 0.001)
        ax.fill_between(
            x=xlower,
            y1=0,
            y2=stats.t.pdf(xlower, dof),
            color=self._canvas.colors.orange,
        )

        # Fill Upper Tail
        xupper = np.arange(upper_critical, upper, 0.001)
        ax.fill_between(
            x=xupper,
            y1=0,
            y2=stats.t.pdf(xupper, dof),
            color=self._canvas.colors.orange,
        )

        # Plot the statistic
        line = ax.lines[0]
        xdata = line.get_xydata()[:, 0]
        ydata = line.get_xydata()[:, 1]
        statistic = round(statistic, 4)

        try:
            idx = np.where(xdata > statistic)[0][0]
            x = xdata[idx]
            y = ydata[idx]
            _ = sns.regplot(
                x=np.array([x]),
                y=np.array([y]),
                scatter=True,
                fit_reg=False,
                marker="o",
                scatter_kws={"s": 100},
                ax=ax,
                color=self._canvas.colors.dark_blue,
            )
            ytext = 10
            if np.isclose(statistic, 0, atol=1e-1):
                ytext *= -2

            ax.annotate(
                f"t = {str(statistic)}",
                (x, y),
                textcoords="offset points",
                xytext=(0, ytext),
                ha="center",
            )
        except IndexError:
            pass

        ax.annotate(
            "Critical Value",
            (lower_critical, 0),
            textcoords="offset points",
            xytext=(20, 15),
            ha="left",
            arrowprops={"width": 2, "headwidth": 4, "shrink": 0.05},
        )

        ax.annotate(
            "Critical Value",
            (upper_critical, 0),
            xycoords="data",
            textcoords="offset points",
            xytext=(-20, 15),
            ha="right",
            arrowprops={"width": 2, "headwidth": 4, "shrink": 0.05},
        )

        ax.set_title(
            f"{result}",
            fontsize=self._canvas.fontsize_title,
        )

        plt.tight_layout()

    def x2testplot(
        self,
        statistic: float,
        dof: int,
        result: str = None,
        alpha: float = 0.05,
        title: str = None,
        ax: plt.Axes = None,
        *args,
        **kwargs,
    ) -> None:
        if ax is None:
            fig, ax = self._canvas.get_figaxes()

        # Render the probability distribution
        x = np.linspace(stats.chi2.ppf(0.01, dof), stats.chi2.ppf(0.99, dof), 100)
        y = stats.chi2.pdf(x, dof)
        ax = sns.lineplot(x=x, y=y, markers=False, dashes=False, sort=True, ax=ax)

        # Compute reject region
        upper = x[-1]
        upper_alpha = 1 - alpha
        critical = stats.chi2.ppf(upper_alpha, dof)

        # Fill Upper Tail
        x = np.arange(critical, upper, 0.001)
        ax.fill_between(
            x=x,
            y1=0,
            y2=stats.chi2.pdf(x, dof),
            color=self._canvas.colors.orange,
        )

        # Plot the statistic
        line = ax.lines[0]
        xdata = line.get_xydata()[:, 0]
        ydata = line.get_xydata()[:, 1]
        statistic = round(statistic, 4)
        try:
            idx = np.where(xdata > statistic)[0][0]
            x = xdata[idx]
            y = ydata[idx]
            _ = sns.regplot(
                x=np.array([x]),
                y=np.array([y]),
                scatter=True,
                fit_reg=False,
                marker="o",
                scatter_kws={"s": 100},
                ax=ax,
                color=self._canvas.colors.dark_blue,
            )
            ax.annotate(
                rf"$X^2$ = {str(statistic)}",
                (x, y),
                textcoords="offset points",
                xytext=(0, 20),
                ha="center",
            )
        except IndexError:
            pass

        ax.annotate(
            "Critical Value",
            (critical, 0),
            xycoords="data",
            textcoords="offset points",
            xytext=(-20, 15),
            ha="right",
            arrowprops={"width": 2, "headwidth": 4, "shrink": 0.05},
        )

        ax.set_title(
            f"{result}",
            fontsize=self._canvas.fontsize_title,
        )

        ax.set_xlabel(r"$X^2$")
        ax.set_ylabel("Probability Density")
        plt.tight_layout()

    def kstestplot(
        self,
        statistic: float,
        n: int,
        result: str = None,
        alpha: float = 0.05,
        title: str = None,
        ax: plt.Axes = None,
        *args,
        **kwargs,
    ) -> None:
        """Draw the results of a t-test with the statistic and reject regions.

        Args:
            statistic (float): The student's t test statistic
            dof (int): Degrees of freedom
            alpha (float): The statistical significance. Default is 0.05.
            title (str): Title for the plot. Optional
            ax: (plt.Axes): A matplotlib Axes object. Optional. If not provide, one will be obtained from the canvas.


        """
        if ax is None:
            fig, ax = self._canvas.get_figaxes()

        # Render the probability distribution
        x = np.linspace(stats.kstwo.ppf(0.001, n), stats.kstwo.ppf(0.999, n), 500)
        y = stats.kstwo.pdf(x, n)
        ax = sns.lineplot(x=x, y=y, markers=False, dashes=False, sort=True, ax=ax)

        # Compute reject region
        lower = x[0]
        upper = x[-1]
        lower_alpha = alpha / 2
        upper_alpha = 1 - (alpha / 2)
        lower_critical = stats.kstwo.ppf(lower_alpha, n)
        upper_critical = stats.kstwo.ppf(upper_alpha, n)

        # Fill lower tail
        xlower = np.arange(lower, lower_critical, 0.001)
        ax.fill_between(
            x=xlower,
            y1=0,
            y2=stats.kstwo.pdf(xlower, n),
            color=self._canvas.colors.orange,
        )

        # Fill Upper Tail
        xupper = np.arange(upper_critical, upper, 0.001)
        ax.fill_between(
            x=xupper,
            y1=0,
            y2=stats.kstwo.pdf(xupper, n),
            color=self._canvas.colors.orange,
        )

        # Plot the statistic
        line = ax.lines[0]
        xdata = line.get_xydata()[:, 0]
        ydata = line.get_xydata()[:, 1]
        statistic = round(statistic, 4)

        try:
            idx = np.where(xdata > statistic)[0][0]
            x = xdata[idx]
            y = ydata[idx]
            _ = sns.regplot(
                x=np.array([x]),
                y=np.array([y]),
                scatter=True,
                fit_reg=False,
                marker="o",
                scatter_kws={"s": 100},
                ax=ax,
                color=self._canvas.colors.dark_blue,
            )
            ytext = 10
            if np.isclose(statistic, 0, atol=1e-1):
                ytext *= -2

            ax.annotate(
                f"t = {str(statistic)}",
                (x, y),
                textcoords="offset points",
                xytext=(0, ytext),
                ha="center",
            )
        except IndexError:
            pass

        ax.annotate(
            "Critical Value",
            (lower_critical, 0),
            textcoords="offset points",
            xytext=(20, 15),
            ha="left",
            arrowprops={"width": 2, "headwidth": 4, "shrink": 0.05},
        )

        ax.annotate(
            "Critical Value",
            (upper_critical, 0),
            xycoords="data",
            textcoords="offset points",
            xytext=(-20, 15),
            ha="right",
            arrowprops={"width": 2, "headwidth": 4, "shrink": 0.05},
        )

        ax.set_title(
            f"{result}",
            fontsize=self._canvas.fontsize_title,
        )

        plt.tight_layout()

    def cramersv(
        self,
        data: pd.DataFrame,
        value: float,
        thresholds: np.array,
        interpretation: str,
        title: str = None,
        *args,
        **kwargs,
    ) -> None:
        default_title = f"Cramer's V Measure of Association between {data.index.name.capitalize()} & {data.columns.name.capitalize()} is {interpretation}"

        title = f"{title}\n{interpretation}" if title else default_title

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=value,
                gauge={
                    "axis": {"range": [0, 1]},
                    "bar": {"color": "#122740"},
                    "steps": [
                        {"range": [0, thresholds[1]], "color": "#84B29E"},
                        {"range": [thresholds[1], thresholds[2]], "color": "#568F8B"},
                        {"range": [thresholds[2], thresholds[3]], "color": "#326B77"},
                        {"range": [thresholds[3], thresholds[4]], "color": "#1B485E"},
                    ],
                },
                domain={"x": [0, 1], "y": [0, 1]},
                title={"text": title},
            )
        )
        fig.show()

    def kendallstau(
        self,
        data: pd.DataFrame,
        a: str,
        b: str,
        value: float,
        thresholds: np.array,
        interpretation: str,
        title: str = None,
        *args,
        **kwargs,
    ) -> None:
        default_title = f"Kendall's Tau-C Measure of Correlation between {a.capitalize()} & {b.capitalize()} is {interpretation}"

        title = f"{title}\n{interpretation}" if title else default_title

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=value,
                gauge={
                    "bar": {"thickness": 0},
                    "axis": {
                        "range": [-1, 1],
                        "tickmode": "array",
                        "tickvals": [-1, -0.5, -0.3, 0, 0.3, 0.5, 1],
                    },
                    "steps": [
                        {
                            "range": [thresholds[0], thresholds[1]],
                            "color": "#003c65",
                        },
                        {
                            "range": [thresholds[1], thresholds[2]],
                            "color": "#457c93",
                        },
                        {
                            "range": [thresholds[2], thresholds[3]],
                            "color": "#88c1bf",
                        },
                        {
                            "range": [thresholds[3], thresholds[4]],
                            "color": "#88c1bf",
                        },
                        {
                            "range": [thresholds[4], thresholds[5]],
                            "color": "#457c93",
                        },
                        {
                            "range": [thresholds[5], thresholds[6]],
                            "color": "#003c65",
                        },
                    ],
                },
                domain={"x": [0, 1], "y": [0, 1]},
                title={"text": title},
            )
        )
        fig.show()

    def _wrap_ticklabels(
        self, axis: str, axes: List[plt.Axes], fontsize: int = 8
    ) -> List[plt.Axes]:
        """Wraps long tick labels"""
        if axis.lower() == "x":
            for i, ax in enumerate(axes):
                xlabels = [label.get_text() for label in ax.get_xticklabels()]
                xlabels = [label.replace(" ", "\n") for label in xlabels]
                ax.set_xticklabels(xlabels, fontdict={"fontsize": fontsize})
                ax.tick_params(axis="x", labelsize=fontsize)

        if axis.lower() == "y":
            for i, ax in enumerate(axes):
                ylabels = [label.get_text() for label in ax.get_yticklabels()]
                ylabels = [label.replace(" ", "\n") for label in ylabels]
                ax.set_yticklabels(ylabels, fontdict={"fontsize": fontsize})
                ax.tick_params(axis="y", labelsize=fontsize)

        return axes

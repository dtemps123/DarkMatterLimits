import numpy as n
import matplotlib.pyplot as pyp
import pandas as pd

## Need these for plot formatting
from matplotlib.gridspec import GridSpec

## Need these for fitting/interpolating
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d

## Class types
import ResultClass as RC

## ==================================================== ##
## Define the plotting style options

## Turn the grid on for all plots
# pyp.rcParams['axes.grid'] = True

## Set the global font size for the plots
pyp.rcParams.update({'font.size': 18})

## Use the LaTeX engine to draw text
pyp.rc('text', usetex=True)

## Select the typeface
pyp.rc('font', family='serif')

## Get a list of the default colors in order
default_colors = pyp.rcParams['axes.prop_cycle'].by_key()['color']
## ==================================================== ##

test = RC.ResultCurve("X1T_MIGDAL_2020.dat")

## ==================================================== ##
fig, ax0 = pyp.subplots(1,1, figsize = (9,7))

## Add the curves
test.plot_curve(fig)

## Set the plot scales
ax0.set_xscale('log')
ax0.set_yscale('log')

## Set the plot limits
ax0.set_xlim(3.00678e-1,1e3)
ax0.set_ylim(1e-50,1e-30)

## Set the axis labels
ax0.set_xlabel('WIMP mass [GeV/c$^{2}$]')
ax0.set_ylabel('WIMP-nucleon cross section [cm$^{2}$]')

## Turn on some extra tick marks
ax0.xaxis.set_tick_params(top = 'on', which='minor')
ax0.xaxis.set_tick_params(top = 'on', which='major')

ax0.yaxis.set_tick_params(top = 'on', which='major')
## ==================================================== ##

pyp.show()

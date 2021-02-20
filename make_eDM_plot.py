import numpy as n
import matplotlib.pyplot as pyp
import pandas as pd

## Need these for plot formatting
from matplotlib.gridspec import GridSpec

## Class types
import ResultClass as RC
import NeutrinoFloorClass as NFC

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

## Result curves
DAMIC_FDM1   = RC.ResultCurve("eDM_DAMIC_FDM1_2019.dat")
PANDAX_FDM1  = RC.ResultCurve("eDM_PandaX_FDM1_2021.dat")
CDMS_FDM1    = RC.ResultCurve("eDM_SuperCDMS_FDM1_2018.dat")
X1T_FDM1     = RC.ResultCurve("eDM_XENON1T_FDM1_2019.dat")

DAMIC_FDMq2  = RC.ResultCurve("eDM_DAMIC_FDMq2_2019.dat")
PANDAX_FDMq2 = RC.ResultCurve("eDM_PandaX_FDMq2_2021.dat")
CDMS_FDMq2   = RC.ResultCurve("eDM_SuperCDMS_FDMq2_2018.dat")

## Calculate the excluded parameter space
plot_x_limits       = n.array([ 2e-1   , 2e3   ])
plot_y_limits_FDM1  = n.array([ 1e-42  , 1e-25 ])
plot_y_limits_FDMq2 = n.array([ 1e-35  , 1e-27 ])

x_val_arr     = n.logspace( start = n.log10(plot_x_limits[0]),
							stop  = n.log10(plot_x_limits[1]),
							num   = 1000)
interp_array_FDM1   = n.zeros(shape=(4,1000))
interp_array_FDMq2  = n.zeros(shape=(3,1000))

interp_array_FDM1[0,:]  = DAMIC_FDM1.interpolator(n.power(x_val_arr,1))
interp_array_FDM1[1,:]  = PANDAX_FDM1.interpolator(n.power(x_val_arr,1))
interp_array_FDM1[2,:]  = CDMS_FDM1.interpolator(n.power(x_val_arr,1))
interp_array_FDM1[3,:]  = X1T_FDM1.interpolator(n.power(x_val_arr,1))

exp_upper_lim_FDM1      = n.min(interp_array_FDM1, axis=0)

interp_array_FDMq2[0,:] = DAMIC_FDMq2.interpolator(n.power(x_val_arr,1))
interp_array_FDMq2[1,:] = PANDAX_FDMq2.interpolator(n.power(x_val_arr,1))
interp_array_FDMq2[2,:] = CDMS_FDMq2.interpolator(n.power(x_val_arr,1))

exp_upper_lim_FDMq2     = n.min(interp_array_FDMq2, axis=0)

## ==================================================== ##
fig = pyp.figure(figsize = (9,4))

## Define the grid
gs = GridSpec(1, 2, width_ratios=[1, 1], height_ratios=[1])
gs.update(wspace=0.325, hspace=0.075) 

## Define the left plot - DM-proton coupling
ax0 = fig.add_subplot(gs[0])

## Add the result curves
DAMIC_FDM1.plot_curve(fig)
PANDAX_FDM1.plot_curve(fig)
CDMS_FDM1.plot_curve(fig)
X1T_FDM1.plot_curve(fig)

## Fill in the exclusion curve
ax0.fill_between(x_val_arr, exp_upper_lim_FDM1, 1e-18, 
	color  = '#aaffc3', 
	zorder = 0, 
	alpha  = 0.5, 
	lw     = 0)

## Set the plot scales
ax0.set_xscale('log')
ax0.set_yscale('log')

## Set the plot limits
ax0.set_xlim(plot_x_limits)
ax0.set_ylim(plot_y_limits_FDM1)

## Set the axis labels
ax0.set_xlabel('DM mass [MeV/c$^{2}$]')
ax0.set_ylabel(r'DM-electron cross section $\bar{\sigma}_e$ [cm$^{2}$]')

## Turn on some extra tick marks
ax0.xaxis.set_tick_params(top = 'on', which='minor')
ax0.xaxis.set_tick_params(top = 'on', which='major')

ax0.yaxis.set_tick_params(top = 'on', which='major')

## Define the right plot - DM-neutron coupling
ax1 = fig.add_subplot(gs[1])

## Add the result curves
DAMIC_FDMq2.plot_curve(fig)
PANDAX_FDMq2.plot_curve(fig)
CDMS_FDMq2.plot_curve(fig)

## Fill in the exclusion curve
ax1.fill_between(x_val_arr, exp_upper_lim_FDMq2, 1e-18, 
	color  = '#aaffc3', 
	zorder = 0, 
	alpha  = 0.5, 
	lw     = 0)

## Set the plot scales
ax1.set_xscale('log')
ax1.set_yscale('log')

## Set the plot limits
ax1.set_xlim(plot_x_limits)
ax1.set_ylim(plot_y_limits_FDMq2)

## Set the axis labels
ax1.set_xlabel('DM mass [MeV/c$^{2}$]')
ax1.set_ylabel(r'DM-electron cross section $\bar{\sigma}_e$ [cm$^{2}$]')

## Turn on some extra tick marks
ax1.xaxis.set_tick_params(top = 'on', which='minor')
ax1.xaxis.set_tick_params(top = 'on', which='major')

ax1.yaxis.set_tick_params(top = 'on', which='major')

## Adjust the figure spacing
fig.subplots_adjust(bottom=0.200, left=0.12, right=0.97)

## ==================================================== ##

pyp.show()

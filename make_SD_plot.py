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
CDMSlte_n = RC.ResultCurve("SD_CDMSLite_n_2016.dat")
CDMSlte_p = RC.ResultCurve("SD_CDMSLite_p_2016.dat")
LUX_n     = RC.ResultCurve("SD_LUX_n_2017.dat")
LUX_p     = RC.ResultCurve("SD_LUX_p_2017.dat")
PANDAX_n  = RC.ResultCurve("SD_PandaX_n_2016.dat")
PANDAX_p  = RC.ResultCurve("SD_PandaX_p_2016.dat")
PICASSO   = RC.ResultCurve("SD_PICASSO_2016.dat")
PICO_C3F8 = RC.ResultCurve("SD_PICO60_C3F8.dat")
PICO_CF3I = RC.ResultCurve("SD_PICO_CF3I.dat")
XENON1T_n = RC.ResultCurve("SD_XENON1T_n_2019.dat")
XENON1T_p = RC.ResultCurve("SD_XENON1T_p_2019.dat")
X1T_n_low = RC.ResultCurve("SD_XENON1T_n_lowmass.dat")
X1T_n_mig = RC.ResultCurve("SD_X1T_n_migdal.dat")
X1T_p_mig = RC.ResultCurve("SD_X1T_p_migdal.dat")

## Neutrino Fog curves
NuFog     = NFC.NeutrinoFog("SI_NeutrinoFloor_Ruppin_LZ_Fig3_1000ty.dat")

## Calculate the excluded parameter space
plot_x_limits = n.array([ 1e-1   , 1e3   ])
plot_y_limits = n.array([ 1e-42 , 1e-30 ])

x_val_arr     = n.logspace( start = n.log10(plot_x_limits[0]),
							stop  = n.log10(plot_x_limits[1]),
							num   = 1000)
interp_array_p  = n.zeros(shape=(4,1000))
interp_array_n  = n.zeros(shape=(4,1000))

interp_array_p[0,:] = CDMSlte_p.interpolator(n.power(x_val_arr,1))
interp_array_p[1,:] = PICO_C3F8.interpolator(n.power(x_val_arr,1))
interp_array_p[2,:] = PICASSO.interpolator(n.power(x_val_arr,1))
interp_array_p[3,:] = X1T_p_mig.interpolator(n.power(x_val_arr,1))

exp_upper_lim_p     = n.min(interp_array_p, axis=0)

interp_array_n[0,:] = CDMSlte_n.interpolator(n.power(x_val_arr,1))
interp_array_n[1,:] = XENON1T_n.interpolator(n.power(x_val_arr,1))
interp_array_n[2,:] = X1T_n_low.interpolator(n.power(x_val_arr,1))
interp_array_n[3,:] = X1T_n_mig.interpolator(n.power(x_val_arr,1))

exp_upper_lim_n     = n.min(interp_array_n, axis=0)

## ==================================================== ##
fig = pyp.figure(figsize = (9,4))

## Define the grid
gs = GridSpec(1, 2, width_ratios=[1, 1], height_ratios=[1])
gs.update(wspace=0.325, hspace=0.075) 

## Define the left plot - DM-proton coupling
ax0 = fig.add_subplot(gs[0])

## Add the result curves
CDMSlte_p.plot_curve(fig)
LUX_p.plot_curve(fig)
PANDAX_p.plot_curve(fig)
PICO_C3F8.plot_curve(fig)
PICO_CF3I.plot_curve(fig)
PICASSO.plot_curve(fig)
X1T_p_mig.plot_curve(fig)
XENON1T_p.plot_curve(fig)

## Fill in the exclusion curve
ax0.fill_between(x_val_arr, exp_upper_lim_p, 1e-28, 
	color  = '#aaffc3', 
	zorder = 0, 
	alpha  = 0.5, 
	lw     = 0)

## Set the plot scales
ax0.set_xscale('log')
ax0.set_yscale('log')

## Set the plot limits
ax0.set_xlim(plot_x_limits)
ax0.set_ylim(plot_y_limits)

## Set the axis labels
ax0.set_xlabel('DM mass [GeV/c$^{2}$]')
ax0.set_ylabel(r'SD DM-proton $\sigma_{\chi p}^\mathrm{SD}$ [cm$^{2}$]')

## Turn on some extra tick marks
ax0.xaxis.set_tick_params(top = 'on', which='minor')
ax0.xaxis.set_tick_params(top = 'on', which='major')

ax0.yaxis.set_tick_params(top = 'on', which='major')

## Define the right plot - DM-neutron coupling
ax1 = fig.add_subplot(gs[1])

## Add the result curves
CDMSlte_n.plot_curve(fig)
LUX_n.plot_curve(fig)
PANDAX_n.plot_curve(fig)
X1T_n_mig.plot_curve(fig)
X1T_n_low.plot_curve(fig)
XENON1T_n.plot_curve(fig)

## Fill in the exclusion curve
ax1.fill_between(x_val_arr, exp_upper_lim_n, 1e-28, 
	color  = '#aaffc3', 
	zorder = 0, 
	alpha  = 0.5, 
	lw     = 0)

## Set the plot scales
ax1.set_xscale('log')
ax1.set_yscale('log')

## Set the plot limits
ax1.set_xlim(plot_x_limits)
ax1.set_ylim(plot_y_limits)

## Set the axis labels
ax1.set_xlabel('DM mass [GeV/c$^{2}$]')
ax1.set_ylabel(r'SD DM-neutron $\sigma_{\chi n}^\mathrm{SD}$ [cm$^{2}$]')

## Turn on some extra tick marks
ax1.xaxis.set_tick_params(top = 'on', which='minor')
ax1.xaxis.set_tick_params(top = 'on', which='major')

ax1.yaxis.set_tick_params(top = 'on', which='major')

## Adjust the figure spacing
fig.subplots_adjust(bottom=0.200, left=0.12, right=0.97)

## ==================================================== ##

pyp.show()

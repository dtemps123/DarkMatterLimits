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
CDEX10    = RC.ResultCurve("CDEX10_2018.dat")
CDMSLite  = RC.ResultCurve("CDMSLite_2016.dat")
CRESSTII  = RC.ResultCurve("CRESSTII_2015.dat")
CRESSTIII = RC.ResultCurve("CRESSTIII_2017.dat")
CRESSTsrf = RC.ResultCurve("CRESSTsurface_2017.dat")
DarkSide  = RC.ResultCurve("DarkSide50_S2only_2018.dat")
LUX       = RC.ResultCurve("LUX_completeExposure_2016.dat")
NEWSG     = RC.ResultCurve("NEWS_G_2018.dat")
PANDAX    = RC.ResultCurve("PandaX_2017.dat")
PICO_C3F8 = RC.ResultCurve("PICO_C3F8_2017.dat")
PICO_CF3I = RC.ResultCurve("PICO_CF3I_2015.dat")
X1T_MIG   = RC.ResultCurve("X1T_MIGDAL_2020.dat")
XENON1T   = RC.ResultCurve("XENON1T_2018.dat")
XENON100  = RC.ResultCurve("XENON100S2_2016.dat")
XMASS     = RC.ResultCurve("XMASS_2018.dat")

## Projection curves
LZ        = RC.ResultCurve("LZ_projection_2018.dat")
SuperCDMS = RC.ResultCurve("SuperCDMS_SNOLAB_projection_2017.dat")
XENONnT   = RC.ResultCurve("XENONnT_projection_2020.dat")

## Neutrino Fog curves
NuFog     = NFC.NeutrinoFog("SI_NeutrinoFloor_Ruppin_LZ_Fig3_1000ty.dat")

## Calculate the excluded parameter space
plot_x_limits = n.array([ 3.00678e-1 , 1e3   ])
plot_y_limits = n.array([ 1e-50      , 1e-30 ])

x_val_arr     = n.logspace( start = n.log10(plot_x_limits[0]),
							stop  = n.log10(plot_x_limits[1]),
							num   = 1000)
interp_array  = n.zeros(shape=(5,1000))

interp_array[0,:] = X1T_MIG.interpolator(n.power(x_val_arr,1))
interp_array[1,:] = DarkSide.interpolator(n.power(x_val_arr,1))
interp_array[2,:] = PANDAX.interpolator(n.power(x_val_arr,1))
interp_array[3,:] = LUX.interpolator(n.power(x_val_arr,1))
interp_array[4,:] = XENON1T.interpolator(n.power(x_val_arr,1))

exp_upper_lim     = n.min(interp_array, axis=0)


## ==================================================== ##
fig, ax0 = pyp.subplots(1,1, figsize = (9,7))

## Add the result curves
CDEX10.plot_curve(fig)
CDMSLite.plot_curve(fig)
CRESSTII.plot_curve(fig)
CRESSTIII.plot_curve(fig)
CRESSTsrf.plot_curve(fig)
DarkSide.plot_curve(fig)
LUX.plot_curve(fig)
NEWSG.plot_curve(fig)
PANDAX.plot_curve(fig)
PICO_C3F8.plot_curve(fig)
PICO_CF3I.plot_curve(fig)
X1T_MIG.plot_curve(fig)
XENON1T.plot_curve(fig)
# XENON100.plot_curve(fig)
XMASS.plot_curve(fig)

## Add the projection curves
LZ.plot_curve(fig, style='projection')
SuperCDMS.plot_curve(fig, style='projection')
XENONnT.plot_curve(fig, style='projection')

## Add the neutrino floor
NuFog.plot_curve(fig)

## Fill in the exclusion curve
ax0.fill_between(x_val_arr, exp_upper_lim, 1e-28, 
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
ax0.set_xlabel('WIMP mass [GeV/c$^{2}$]')
ax0.set_ylabel('WIMP-nucleon cross section [cm$^{2}$]')

## Turn on some extra tick marks
ax0.xaxis.set_tick_params(top = 'on', which='minor')
ax0.xaxis.set_tick_params(top = 'on', which='major')

ax0.yaxis.set_tick_params(top = 'on', which='major')
## ==================================================== ##

pyp.show()

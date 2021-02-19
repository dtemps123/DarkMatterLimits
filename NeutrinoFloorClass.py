import numpy as n
from scipy.interpolate import interp1d

N_HEAD_LINES = 7

class NeutrinoFog:

	source = "arXiv source"
	label  = "LABEL"
	year   = "2020"
	fillcolor  = "#FFFFFF"
	linecolor  = "#FFFFFF"

	def __init__( self            , 
				  file_name	      ,
				  user_label=None ):

		self.full_file_path = "./limit_data/"+file_name
		
		## Read in the markup part of the file
		with open(self.full_file_path) as file:
		    head = [next(file).strip().replace(": ",":") for x in range(N_HEAD_LINES+1)]
		# print(head)

		## Parse the markup part of the file
		for i in n.arange(N_HEAD_LINES+1):
			parts = head[i].split(':')

			if not (len(parts)==2):
				continue

			if (parts[0].lower()=="source"):
				self.source = parts[1]

			if (parts[0].lower()=="label"):
				self.label  = parts[1]

			if (parts[0].lower()=="year"):
				self.year   = parts[1]

			if (parts[0].lower()=="fillcolor"):
				self.fillcolor  = parts[1]

			if (parts[0].lower()=="linecolor"):
				self.linecolor  = parts[1]

			if (parts[0].lower()=="label_xpos"):
				self.label_xpos  = float(parts[1])

			if (parts[0].lower()=="label_ypos"):
				self.label_ypos  = float(parts[1])
				
		## Read in the data part of the file
		data = n.loadtxt(self.full_file_path ,
			skiprows  = N_HEAD_LINES     ,
			delimiter = ','              )

		self.mass = data[:,0]
		self.xsec = data[:,1]	

		self.interpolator = interp1d(self.mass, self.xsec,
			bounds_error=False,
			fill_value=(self.xsec[0],self.xsec[-1]))

	def plot_curve( self, fig, 
					show_label=True,
					style=None):
		ax = fig.gca()

		## Draw the curve
		ax.plot(self.mass, self.xsec,
			linestyle = '--',
			linewidth = 2.5,
			color     = self.linecolor,
			label     = self.label,
			zorder    = 2)

		ax.fill_between(self.mass, self.xsec, 1e-55,
			color  = self.fillcolor,
			zorder = 2,
			alpha  = 0.5, 
			lw     = 0)

		## Draw the text
		if (show_label):
			ax.text( self.label_xpos, self.label_ypos ,
				self.label,
				color    = self.linecolor,
				fontsize = 10.)

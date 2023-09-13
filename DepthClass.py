import numpy as n
# from scipy.interpolate import interp1d

N_HEAD_LINES = 1

class DepthPoints:

	def __init__( self, 
				  file_name='underground_muon_flux.csv'):

		self.full_file_path = "./limit_data/"+file_name
		
		## Read in the markup part of the file
		with open(self.full_file_path) as file:
		    head = [next(file).strip() for x in range(N_HEAD_LINES)]
		# print(head)
		self.colnames = head[0].split(",")

		## Read in the data part of the file
		data = n.loadtxt(self.full_file_path ,
			skiprows  = N_HEAD_LINES     ,
			delimiter = ','              ,
			usecols   = (0,1) )

		self.depths = data[:,0]
		self.muonfs = data[:,1]
		self.labels = n.loadtxt(self.full_file_path ,
			skiprows  = N_HEAD_LINES     ,
			delimiter = ','              ,
			usecols   = (2)              ,
			dtype     = type("a") )

	def plot_depths( self, fig, 
					default_labels=True,
					style=None):
		ax = fig.gca()

		## Draw the points and labels
		for i in n.arange(len(self.depths)):
			xpos = self.depths[i]
			ypos = self.muonfs[i]
			text = self.labels[i]

			ax.scatter(xpos, ypos,
			linestyle = "None",
			linewidth = 0.0,
			color     = "C"+str(int(i)),
			zorder    = 1)

			ax.text(xpos,ypos,text,
			fontsize = 18,
			color    = "C"+str(int(i)),
			rotation = 45
			)

		if default_labels:
			ax.set_xlabel(self.colnames[0])
			ax.set_ylabel(self.colnames[1])

		ax.set_yscale('log')
		ax.set_ylim([1e-10,1e-6])

		# xlims = ax.get_xlim() ; xrng = xlims[1]-xlims[0]
		# ylims = ax.get_ylim() ; yrng = ylims[1]-ylims[0]

import numpy as n
# import matplotlib.pyplot as pyp

N_HEAD_LINES = 6

class ResultCurve:

	source = "arXiv source"
	label  = "LABEL"
	year   = "2020"
	color  = "#FFFFFF"

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

			if (parts[0].lower()=="color"):
				self.color  = parts[1]

			if (parts[0].lower()=="label_xpos"):
				self.label_xpos  = float(parts[1])

			if (parts[0].lower()=="label_ypos"):
				self.label_ypos  = float(parts[1])

		## Add more text to label
		self.label = self.label + " (" + self.year + ")"

		## Overwrite the label if requested
		if not (user_label == None):
			self.label = user_label

		# print(self.source)
		# print(self.label)
		# print(self.year)
		# print(self.color)

		## Read in the data part of the file
		data = n.loadtxt(self.full_file_path ,
			skiprows  = N_HEAD_LINES     ,
			delimiter = ','              )

		self.mass = data[:,0]
		self.xsec = data[:,1]		

	def plot_curve( self, fig, 
					show_label=True,
					style=None):
		ax = fig.gca()

		## Draw the curve
		ax.plot(self.mass, self.xsec,
			linestyle = ( '--' if (style=='projection') else '-'),
			linewidth = 1.5,
			color     = self.color,
			label     = self.label,
			zorder    = 3)

		## Draw the text
		if (show_label):
			ax.text( self.label_xpos, self.label_ypos ,
				self.label,
				color    = self.color,
				fontsize = 10.)

import random		
import csv
import platform
import numpy				
from matplotlib import pyplot

# either read from file or use randomly generated data
read_from_file = True

if read_from_file:
        # define csv file name for 2D grid data
        grid_1_file = "residual.dat"
        grid_2_file = "residual_c.dat"
        # load grid data from csv file into 2D array
        f1 = open(grid_1_file,"rb")
        f2 = open(grid_2_file,"rb")

        grid_1_matrix = numpy.fromfile(f1).reshape(3,4096,4096)[0]
        grid_2_matrix = numpy.fromfile(f2).reshape(3,4096,4096)[0]

	#grid_1_matrix = numpy.loadtxt(open(grid_1_file, "rb"), delimiter=",")
	#grid_2_matrix = numpy.loadtxt(open(grid_2_file, "rb"), delimiter=",")
else:
	# generate random values
	grid_1_matrix = numpy.random.random((50, 50))
	grid_2_matrix = numpy.random.random((50, 50))

# define plot figure for presenting graphcs
figure = pyplot.figure()
figure_rows = 1
figure_cols = 3

# add a new subplot in figure for presenting grid_1 data
figure.add_subplot(figure_rows, figure_cols, 1) # (total rows, total columns, index for grid_1 data subplot)
# insert grid_1 data into subplot
pyplot.imshow(grid_1_matrix , cmap='hot', interpolation='none')
pyplot.title("Model by Python!")
pyplot.ylabel("X label")
pyplot.xlabel("Y label")
pyplot.colorbar() # enables bar to show value range

# add a new subplot in figure for presenting grid_2 data
figure.add_subplot(figure_rows, figure_cols, 2) # (total rows, total columns, index for grid_2 data subplot)
# insert grid_2 data into subplot
pyplot.imshow(grid_2_matrix , cmap='hot', interpolation='none')
pyplot.title("Model by C++!")
pyplot.ylabel("X label")
pyplot.xlabel("Y label")
pyplot.colorbar() # enables bar to show value range

# create third matrix for difference between grid_1 and grid_2
difference = numpy.subtract(grid_1_matrix, grid_2_matrix)
# add a new subplot in figure for presenting grid_3 data
figure.add_subplot(figure_rows, figure_cols, 3) # (total rows, total columns, index for difference data subplot)
pyplot.imshow(difference , cmap='hot', interpolation='none')
pyplot.title("The difference!")
pyplot.ylabel("X label")
pyplot.xlabel("Y label")
pyplot.colorbar() # enables bar to show value range

# Calculate relative root mean squared error between grid_1 and grid_2 
# (how different are the two grids, smaller is better)
relative_diff = numpy.sqrt(((grid_2_matrix-grid_1_matrix) ** 2).sum()) / numpy.sqrt((grid_2_matrix ** 2).sum())
print("Relative root mean squared error: %f (%.2f%% different)" % (relative_diff, (relative_diff * 100)))

# set figures to full screen
if platform.system() == "Linux":
	manager = pyplot.get_current_fig_manager()
	#manager.resize(*manager.window.maxsize())

# show the figure on screen
pyplot.show()

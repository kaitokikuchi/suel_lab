# Script to generate animated histograms from csv input
# To run, open Terminal and execute
# $python hist_animation.py data.csv


import pandas as pd
import argparse
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def main(file):
	# Input CSV should be formatted to have rows as timepoints
    # and columns for individual ROIs
    # 

	data= pd.read_csv(file)
	frame_length = len(data.index)

	def update_hist(i):
		#clears previous histogram to update with new one
	    plt.cla()
	    
	    #plt.title('title')
	    
	    #plot text to show image frame number i
	    plt.text(0.85, 0.85, 'frame = {}'.format(i),size=15,
	    	horizontalalignment='center',
	    	verticalalignment='center',
	    	transform = ax.transAxes)

	    #plot ith row of dataset
	    plt.hist(data.iloc[i])

	#This inititalization will plot the background
	def init():
	    line = plt.plot([])
	    return (line)

	fig = plt.figure()
	ax = fig.add_subplot(111)

	ani = animation.FuncAnimation(fig, update_hist, frame_length, 
                                  init_func=init, repeat=False)

	#define writer command. Change fps for different speeds
	Writer = animation.writers['ffmpeg']
	writer = Writer(fps=3, bitrate=1800)

	ani.save('hist_animation.mp4', writer=writer)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='path to the CSV file')
    args_namespace = parser.parse_args()
    args = vars(args_namespace)['file']
    main(args)
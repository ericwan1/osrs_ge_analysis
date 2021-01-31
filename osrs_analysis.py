import csv
import pandas as pd
import matplotlib.pyplot as plt


def calculate_percent_change(start_val, end_val):
	# Calculates positive, negative percent change
	return ((end_val - start_val) / abs(start_val)) * 100


def calculate_moving_windows_df_whole(df, window):
	# Returns a list of lists. Each list contains the item name&number, with the computed avgs
	all_window_list = []
	for val in range(len(df.index)):
		window_list = []
		window_list.append(df.iloc[val,0])
		for increment in range((len(df.columns) - 1) // window):
			start = window * increment + 1
			end = window * (increment + 1) + 1 
			grabbed_window = df.iloc[val,start:end]
			window_avg_val = grabbed_window.mean()
			window_list.append(window_avg_val)

		all_window_list.append(window_list)

	return all_window_list


def prev_x_days_specific(df, x, item_number):
	# Returns list containing the previous x number of days of prices for specific item
	return df.iloc[item_number, ((len(df.columns)) - x):(len(df.columns))]


def prev_x_days_df_whole(df, x):
	all_items_list = []
	for val in range(len(df.index)):
		x_days_list = []
		x_days_list.append(df.iloc[val,0])
		x_days_list.append(df.iloc[val, ((len(df.columns)) - x):(len(df.columns))])

	all_items_list.append(x_days_list)

	
df = pd.read_csv("osrs_df.csv")
window_avg_15 = calculate_moving_windows_df_whole(df, 15)

for list_of_avgs in window_avg_15:
	list_data = list_of_avgs[1:]
	item_name = list_of_avgs[0]

	plot_all = plt.plot(list_data, label = item_name)
	plot_all = plt.xlabel("Windows")
	plot_all = plt.ylabel("Price")
	plot_all = plt.title("Window Prices")
	plot_all = plt.legend(bbox_to_anchor = (1, 0.5), loc = 6)
	plot_all = plt.tight_layout()

plt.show()

copper_prev_5 = prev_x_days_specific(df, 5, 0)
copper_prev_5 = calculate_percent_change(copper_prev_5[0],copper_prev_5[4])


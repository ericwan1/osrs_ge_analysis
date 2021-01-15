import json
import requests
import pandas as pd


def load_names_id(input_list):
	item_name_list = []
	for item_id in input_list:
		item_url = "https://secure.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item=" + str(item_id)
		item_response = requests.get(item_url)
		item_json = item_response.json()

		# Current price
		# item_price = item_json['item']['current']['price'] 
		item_name = item_json['item']['name']

		name_id = str(item_name) + "-" + str(item_id)
		item_name_list.append(name_id)

	return item_name_list


def load_graph_data(input_list):
	price_track = []
	for item_id in input_list:
		item_url = "https://services.runescape.com/m=itemdb_oldschool/api/graph/" + str(item_id) + ".json"
		item_response = requests.get(item_url)
		item_json = item_response.json()

		item_daily = item_json['daily']
		temp_list = []

		for time in item_daily:
			# Json grabs previous 180 days from the graph api
			temp_price_val = item_daily[str(time)]
			temp_list.append(temp_price_val)

		price_track.append(temp_list)

	return price_track

# Dictionary will work in format as follows- "item_name-item_id":[list of past 180 day vals]
def build_dictionary(keys, data):
	return dict(zip(keys,data))

# I want to grab the information for ores and fish. 

# Copper, Tin, Silver, Gold, Iron, Coal, Mithril (Ore)
ore_id = [436, 438, 442, 444, 440, 453, 447] 
# Salmon, Trout, Lobster, Swordfish (Cooked)
cooked_fish_id = [329, 333, 379, 373]
# Salmon, Trout, Lobster, Swordfish (Raw)
raw_fish_id = [331, 335, 377, 371]

combined_id_list = ore_id + cooked_fish_id + raw_fish_id
combined_name_list = load_names_id(combined_id_list)
combined_price_list = load_graph_data(combined_id_list)

item_dictionary = build_dictionary(combined_name_list, combined_price_list)

df = pd.DataFrame.from_dict(item_dictionary, orient = 'index')
df.to_csv('osrs_df.csv')
import json

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(high_income_counties(counties))
    print(alphabetically_first_county(counties))
    print(county_most_under_18(counties))
    print(percent_most_under_18(counties))
    print(lowest_median_income(counties))
    print(state_with_most_counties(counties))

def high_income_counties(counties):
	county = []
	for data in counties:
		if data['Income']['Median Houseold Income'] > 90000:
			county.append(data['County'])
	return county
	"""Return a LIST of the counties with a median household income over $90,000."""
    

def lowest_median_income(counties):
	"""Return a name of a county with the lowest median household income"""
	countyLowIncome = ["county", 100000000]
	for data in counties:
		if countyLowIncome[1] > data['Income']['Median Houseold Income']:
			countyLowIncome[1] = data['Income']['Median Houseold Income']
			countyLowIncome[0] = data['County']
	return countyLowIncome[0]

def alphabetically_first_county(counties):
	"""Return the county with the name that comes first alphabetically."""
	#Hint: you can use < to compare strings in Python. ex) "cat" < "dog" gives the value True
	county = "Z"
	for data in counties:
		if data['County'] < county:
			county = data['County']
	return county
def percent_most_under_18(counties):
	"""Return the highest percent of under 18 year olds."""    
	under18 = 0.1
	for data in counties:
		if data['Age']['Percent Under 18 Years'] > under18:
			under18 = data['Age']['Percent Under 18 Years']
	return under18
def county_most_under_18(counties):
	"""Return the name a county with the highest percent of under 18 year olds."""
	under18 = [0.1, "county"]
	for data in counties:
		if data['Age']['Percent Under 18 Years'] > under18[0]:
			under18[0] = data['Age']['Percent Under 18 Years']
			under18[1] = data['County']
	return under18[1]
def state_with_most_counties(counties):
	"""Return a state that has the most counties."""
	#1. Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
	StateNumCounties = {}
	#2. Find the state in the dictionary with the most counties
	for data in counties:
		if data['State'] in StateNumCounties:
			data['State'] = data['State'] + 1
		else:
			data['State'] = 1
	#3. Return the state with the most counties
	mostCounties = [0, "hi"]
	for data in StateNumCounties:
		if StateNumCounties.get(data) > mostCounties[0]:
			mostCounties[0] = StateNumCounties.get(data)
			mostCounties[1] = data
	return mostCounties[1]
def your_interesting_demographic_function(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""

if __name__ == '__main__':
    main()

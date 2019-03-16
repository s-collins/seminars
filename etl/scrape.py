from wrappers import ClevelandMuseumOfArt


if __name__ == '__main__':
	# List of wrapper objects for data sources
	all_wrappers = [
		ClevelandMuseumOfArt.Wrapper(),
	]

	for wrapper in all_wrappers:
		source_name = wrapper.get_source_name()
		source_events = []
		if wrapper.ping():
			print("Successful Ping:", source_name)
			# TODO: scrape events
		else:
			print("Failed Ping:", source_name)

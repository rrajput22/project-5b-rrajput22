# Author: Rajvi Rajput
# GitHub username: rrajput22
# Date: 10/29/2023
# Description: Program defines a class 'NobelData' that reads Nobel Prize data from a JSON file and uses the
# 'search_nobel' method to get then sort the last names of winners in a specific year and category.

import json


class NobelData:
    def __init__(self, file_path='nobels.json'):
        """
        initializes the 'NobelData' class by reading Nobel Prize data from a JSON file
        """
        self._data = self._read_json(file_path)

    def _read_json(self, file_path):
        """
        method to read JSON data from file
        """
        with open(file_path, 'r') as json_file:
            return json.load(json_file)

    def search_nobel(self, year, category):
        """Method to search and retrieve the winners in a specific year and category."""
        if year not in self._data or category.lower() not in self._data[year]:  # checks if the provided year and
            # category are valid
            return []

        winners = self._data[year][category.lower()]  # pull out winners for the specific year and category

        winners_with_last_name = []
        for winner in winners:
            if 'last_name' in winner and winner.get('last_name'):
                winners_with_last_name.append(winner.get('last_name', ''))

        return sorted(winners_with_last_name)[:3]  # returns 3 last names after sorting

# Example usage:
# nd = NobelData()
# result = nd.search_nobel("2001", "economics")
# print(result)

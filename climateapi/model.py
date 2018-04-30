import requests
import csv


try:
    # for Python 2.x
    from StringIO import StringIO
except ImportError:
    # for Python 3.x
    from io import StringIO


def store_disasters():
    result = requests.get("https://www.fema.gov/api/open/v1/DisasterDeclarationsSummaries.csv")
    temp_data = StringIO(result.text)
    keys = []
    processed_data = []
    if result.status_code == 200:
        data = csv.reader(temp_data)
        for index, row in enumerate(data):
            if index is 0:
                keys = row
            else:
                disaster_data = {}
                for i, value in enumerate(row):
                    disaster_data[keys[i]] = value
                disaster = Disaster(
                    disaster_data['incidentType'],
                    disaster_data['fyDeclared'],
                    disaster_data['state'],
                    int(disaster_data['disasterNumber'])
                )
                processed_data.append(disaster)
    return processed_data


class Disaster:
    """Keep Track of all disasters"""

    def __init__(self, incident, year, state, disasterid):
        self.type = incident
        self.year = year
        self.state = state
        self.disasterid = disasterid


    def __repr__(self):
        return "Disaster:{} {} {} {}".format(self.type, self.year, self.state, self.disasterid)
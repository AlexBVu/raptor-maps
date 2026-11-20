    # 11/18/26
    # Alex Vu
    # parser.py

import simplejson as json 
from itertools import islice
from collections import Counter

JSON_FILE = "/Users/alexvu/Desktop/projects/raptor-maps/data/InfraredSolarModules/module_metadata.json"


# API-called function
# expects n to be a number 
def getFirstN(n : int):
    with open(JSON_FILE) as json_data:
        data = json.load(json_data)

    return dict(islice(data.items(), int(n)))

# API-called function
# expects n to be a number and category to be a valid str
def getByClass(n : int, category : str):
    with open(JSON_FILE) as json_data:
        data = json.load(json_data)

    res = []

    for key, val in data.items():
        if len(res) == n:
            return res
        if val["anomaly_class"] == category:
            res.append((key, val))

def getInfo() -> None:
    with open(JSON_FILE) as json_data:

        anomaly_classes = set()
        anomaly_counts = Counter()

        # get length
        data = json.load(json_data)
        print("\nthere are", len(data), "entries in the json file")

        # get the classes
        for key, value in data.items():
            val = value['anomaly_class']
            if val not in anomaly_classes:
                anomaly_classes.add(val)

            anomaly_counts[val] += 1
            

        print("\nthe anomaly classes are: ", anomaly_classes)

        print("\nthe classes have frequencies as follows:\n")
        for key, value in anomaly_counts.items():
            print(key, ":", value)
        
def main():
    getInfo()

if __name__ == "__main__":
    main()
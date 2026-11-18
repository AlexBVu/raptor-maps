    # 11/18/26
    # Alex Vu
    # parser.py

import simplejson as json 
from collections import Counter

JSON_FILE = "/Users/alexvu/Desktop/projects/raptor-maps/data/InfraredSolarModules/module_metadata.json"

def getInfo() -> dict:
    with open(JSON_FILE) as json_data:

        # anomaly_classes = set()
        anomaly_counts = Counter()

        # get length
        data = json.load(json_data)
        # print("\nthere are", len(data), "entries in the json file")

        # get the classes
        for key, value in data.items():
            val = value['anomaly_class']
            # if val not in anomaly_classes:
            #     anomaly_classes.add(val)

            anomaly_counts[val] += 1
            

        # print("\nthe anomaly classes are: ", anomaly_classes)

        # print("\nthe classes have frequencies as follows:\n")
        # for key, value in anomaly_counts.items():
        #     print(key, ":", value)
        return anomaly_counts
        
def main():
    getInfo()

if __name__ == "__main__":
    main()
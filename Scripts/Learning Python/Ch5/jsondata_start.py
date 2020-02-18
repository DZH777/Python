# 
# Example file for parsing and processing JSON
#
import urllib.request 
import json

def printResults(data):
  # Use the json module to load the string data into a dictionary
  theJSON = json.loads(data)
  
  # now we can access the contents of the JSON like any other Python object
  if "title" in theJSON["metadata"]:
    print(theJSON["metadata"]["title"])
  
  # output the number of events, plus the magnitude and each event name  
  if "count" in theJSON["metadata"]:
    print("The quantity of events is", theJSON["metadata"]["count"])
  # for each event, print the place where it occurred
  if "features" in theJSON:
    for elem in theJSON["features"]:
      print(elem["properties"]["place"])
  print("----------------")
      # print the events that only have a magnitude greater than 4
  if "features" in theJSON:
    for elem in theJSON["features"]:
      if elem["properties"]["mag"] >= 4.0:
        print("%2.1f" % elem["properties"]["mag"], elem["properties"]["place"])
  print("----------------")
  # print only the events where at least 1 person reported feeling something
  print("Events that were felt: ")
  if "features" in theJSON:
    for elem in theJSON["features"]:
      feltReports = elem["properties"]["felt"]
      if feltReports != None:
        if feltReports > 0:
            print(elem["properties"]["felt"], "men", elem["properties"]["place"])
  print("----------------")
def main():
  # define a variable to hold the source URL
  # In this case we'll use the free data feed from the USGS
  # This feed lists all earthquakes for the last day larger than Mag 2.5
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

  # Open the URL and read the data
  webUrl = urllib.request.urlopen(urlData)
  webCode = webUrl.getcode()
  print ("result code: ",webCode)
  if (webCode):
    data = webUrl.read()
    printResults(data)
  else:
    print("Received error", webCode)

if __name__ == "__main__":
  main()

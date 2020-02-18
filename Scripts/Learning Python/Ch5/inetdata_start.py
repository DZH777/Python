# 
# Example file for retrieving data from the internet
#

import urllib.request

def main():
  webURL = urllib.request.urlopen("http://epam.com")
  print("result code:", webURL.getcode())
  data = webURL.read()
  print(data)

if __name__ == "__main__":
  main()

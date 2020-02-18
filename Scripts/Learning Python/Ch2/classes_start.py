#
# Example file for working with classes
#

class myClass1:
    def method1(self):
      print("myClass1 method1")
    def method2(self, someString):
      print("myClass1 method2 " + someString)

class myClass2(myClass1):
    def method1(self):
      myClass1.method1(self)
      print("myClass2 method1")
    def method2(self, someString):
      print("myClass2 method2 ")


def main():
  c1 = myClass1()
  c1.method1()
  c1.method2("String")

  c2 = myClass2()
  c2.method1()
  c2.method2("String")

  print(50 * ('!'))
  
if __name__ == "__main__":
  main()

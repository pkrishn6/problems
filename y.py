import time
while True:
   try:
      import x
      print(x.x())
   except Exception as e:
      print("x not found")
      time.sleep(2)

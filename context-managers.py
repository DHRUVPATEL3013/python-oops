class MyContext:

  def __enter__(self):
    print("starting")

  def __exit__(self, exc_type, exc, tb):
    print("exit")


with MyContext():
  print("hello this is content")


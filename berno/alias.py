from subprocess import call
import sys


def logger(msg, filename='output.txt'):
  print msg
  sys.stdout.flush()
  with open(filename, "a") as fd:
    fd.write(msg)

def alias():
  call(["alias", "test='test test'"])

if __name__ == "__main__":
  alias()

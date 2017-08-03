def varargs(arg1, *args):
  print "Got "+arg1+" and "+ "".join(args)
  print args
varargs("one") # output: "Got one and "
varargs("one", "two") # output: "Got one and two"
varargs("one", "two", "three","four") # output: "Got one and two, three"
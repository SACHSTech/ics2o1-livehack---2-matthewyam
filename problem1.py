#These are the 2 variables where the user inputs the information
ant = (int(input("How many antennas? ")))
eye = (int(input("How many eyes? ")))

#The if statemenmt here determins what kind of alien it is.
if ant>=3 and eye<=4:
  print("Life form detected: AudreyMartian")

if ant<=6 and eye>=2:
  print("Life form detected: MaxMartian")

if ant<=2 and eye<=3:
  print("Life form detected: BrooklynMartian")

if ant==0 and eye==2:
  print("Life form detected: MattDamonMartian")

else:
  print("No life form detected")
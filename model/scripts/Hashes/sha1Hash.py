import hashlib

outputhash  = open("outputhashes.txt", "w")

outputhash.write(hashlib.sha1(b"PowerUser").hexdigest())
outputhash.write("\n")
outputhash.write(hashlib.sha1(b"SiemensUser").hexdigest())
outputhash.write("\n")
outputhash.write(hashlib.sha1(b"RockwellUser").hexdigest())
outputhash.write("\n")
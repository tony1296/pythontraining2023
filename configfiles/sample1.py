from configparser import ConfigParser

# create object of Configuration class
config=ConfigParser()
# for dynamic access

config.read("../configfiles/sample1.cfg")
print(config.get("Section1","username"))
print(config.get("Section1","password"))
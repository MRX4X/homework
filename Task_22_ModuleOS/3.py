import os
name=0
for i in os.listdir("/Users/denis/Downloads/target"):
    if int(i)%2==0:
        os.rename("/Users/denis/Downloads/target/"+i, "/Users/denis/Downloads/target/"+"denis"+str(name))

import sys
user_number=int(sys.argv[1])
for i in range(1,21):
    print("%d*%2d=%3d"%(user_number,i,user_number*i))
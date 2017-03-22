import time
t0 = time.time()
for i in xrange(10000000):
    i+=5
    print time.time()-t0

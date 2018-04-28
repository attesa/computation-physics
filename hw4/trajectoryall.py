import matplotlib.pyplot as plt

def read_plot(filename):
    file = open( filename, 'r')
    lines = file.readlines()
    x = []
    y = []
    for line in lines :
        words = line.split()
        ix, iy = [float(s) for s in words]
        x.append(float( ix ))
        y.append(float( iy ))
    return x,y

for i in range(18):
    x, y = read_plot("trajfile_Y_py_rmax5r10"+str(i)+".data")
#   print "trajfile_py_"+str(i)+".data"
    plt.plot(x,y)
plt.show()

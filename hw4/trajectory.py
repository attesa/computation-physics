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
x1 = []
y1 = []
x1, y1 = read_plot("differential_cross_sectiony.data")
#x1, y1 = read_plot("differential_cross_sectionrmaxr100100.data")
#x1, y1 = read_plot("y1.data")

plt.plot(x1,y1)
plt.show()

from matplotlib import pyplot
import sqlite3 as sq
import numpy as np

connection = sq.connect('longley.db')
cursor = connection.cursor()
data = cursor.execute('SELECT * FROM longley').fetchall()
type(data),type(data[0][0])
data= np.array(data)
x, y =  data[:,5],data[:,0]
x =np.array([int(l) for l in x])
y =np.array([float(l) for l in y])
pyplot.figure(figsize=(16,8))
pyplot.scatter(x, y, color='black')
pyplot.xlabel("years")
def objective(x, a, b):
	return a * x + b

from scipy.optimize import curve_fit
popt, _ = curve_fit(objective, x, y)
a, b = popt
print('y = %.5f * x + %.5f' % (a, b))
x_line= np.arange(min(x),max(x)+1,1)
y_line = np.array(objective(x_line, a, b))
pyplot.scatter(x, y, color='black')
pyplot.xlabel("years")
pyplot.plot(x_line, y_line, '--', color='red')
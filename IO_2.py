import matplotlib.pyplot as plt 
import numpy as np 

x = np.arange(0,50,0.1) 

# plotting the lines 
a1 = 40 - 0.1111*x
a2 = 30 +0.5*x 
a3 = 0.0001*x
a5 = 60 - 1*x

# The upper edge of 
# polygon 
a4 = np.minimum(a1,  a2) 
a6 = np.minimum(a4, a5)
# Setting the y-limit 
plt.ylim(0, 60) 
plt.xlim(0,60)
# Plot the lines 
plt.plot(x, a1, 
	x, a2,
         x, a5) 

# Filling between line a3 
# and line a4 
plt.fill_between(x, a3, a4,
                 where = (x<20),
                 color='green', 
                    alpha=0.5)
plt.fill_between(x, 0, a6,
                 where = (x<50),
                 color='green', 
                    alpha=0.5)
plt.show() 

x = np.arange(0,5,0.1)
a1 = 5-2*x

a2 = -5

# Shade the area between y1 and line y=0
plt.fill_between(x, a1, a2,
                 facecolor="orange", # The fill color
                 color='blue',       # The outline color
                 alpha=0.2)          # Transparency of the fill

# Show the plot
plt.show()

x = np.arange(-5,5,0.1)

a1 = 5

plt.ylim(0, 10) 
plt.xlim(-5,5)

# Shade the area between y1 and line y=0
plt.fill_between(x, a1, a2,
                 facecolor="orange", # The fill color
                 color='blue',       # The outline color
                 alpha=0.2)          # Transparency of the fill

# Show the plot
plt.show()

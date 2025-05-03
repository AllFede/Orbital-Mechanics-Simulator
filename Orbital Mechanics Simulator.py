import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# COSTANTS OF THE PROJECT
# -------------------------------

# Costante gravitazionale (N*m^2/Kg^2)
G = 6.67430e-11

# Massa della Terra (Kg)
M = 5.972e24

# Raggio della Terra (m)
R = 6.371e6

# -------------------------------
# INITIALIZATION SATELLITE
# -------------------------------

#Now we define the position and velocity of the satellite and simulate a LEO-Low Earth Orbit. We place it at a certain altitude above the Earth's surface with a tangential speed to remain in orbit

#Initial altitude of the satellite (300 km above the Earth's surface)
h = 300e3

#Initial position along the x-axis
x0 = R + h
y0 = 0

#to mantein the satellite in a circul orbit without falling or escaping into space we apply the right orbital velocity through Newton's law
v0 = np.sqrt(G * M/x0)

#initial velocity along the y-axis
vx0 = 0
vy0 = v0

# -------------------------------
# ORBIT SIMULATION
# -------------------------------

#Using Euler's metohod we upgrade the position and velocity of the satellite in any time interval

#Simulation time (s)
dt = 1 
t_max = 6000  #(total time about 1 hour and 40 minutes)

#List initialization for the memorization of the trajectorie
x_vals = [x0] #position in any instant of time along the x-axis
y_vals = [y0] #position in any istant of time along the y-axis
vx = vx0      #initial velocity along the x-axis
vy = vy0      #intial velocity along the y-axis

#Orbit simulation
for _ in range(int(t_max / dt)):
  #Calculating the distance from the center of the Earth through the Pythagorean theorem
  r = np.sqrt(x_vals[-1]**2 + y_vals[-1]**2)

  #Gravitational acceleration
  a = -G * M / r**3 # derives from F = G*M*m/r^2 and F = m*a , substituting in the equation we obtain G*M/r^2 = a. BuT through vectorial components it is with r**3
  ax = a * x_vals[-1]
  ay = a * y_vals[-1]

  #Velocity upgrade
  vx += ax * dt
  vy += ay * dt

  #Position upgrade
  x_new = x_vals[-1] + vx * dt
  y_new = y_vals[-1] + vy * dt

  #Save the new position
  x_vals.append(x_new)
  y_vals.append(y_new)



plt.figure(figsize=(8, 8))
plt.plot(x_vals, y_vals, label="Orbita del satellite")
plt.plot(0, 0, 'yo', markersize=12, label="Terra")  # Terra al centro
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Simulazione dell'orbita attorno alla Terra")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()

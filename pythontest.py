from aguaclara.play import *

r = 0.2 * u.m
d = 2*r
q = 2 * u.m**3 / u.s

temp_list = np.arange(0,201,1) #Temperature range in degrees Celsius, in increments of 1, from 0 to 200
temp_array = np.array(temp_list)
celsius_array = temp_array
kelvin_array = (celsius_array + 273) * u.degK
nu = pc.viscosity_kinematic(celsius_array*u.degC)
rey = pc.re_pipe(q,d,nu)
rey_array = u.Quantity(np.array(rey))

plt.plot(kelvin_array, rey_array, label = "Reynolds Number")
plt.xlabel('Temperature / K')
plt.ylabel('Reynolds Number')
plt.title('Reynolds Number vs Temperature in Kelvins')
plt.minorticks_on()
plt.grid(which = 'major')
plt.grid(which = 'minor')
plt.legend(loc = 'lower right', ncol = 1)
plt.tight_layout()
plt.savefig('./Images/ReyKelvinPlot.png')
plt.show()

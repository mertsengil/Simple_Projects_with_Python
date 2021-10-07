import matplotlib.pyplot as plt
import numpy as np

heat_flux = [10.858,10.617,10.183,9.7003,9.652,10.086,9.459,8.3972,7.6251,7.1902,7.046,6.9494,6.7081,6.3221,6.0325,5.7429,5.5016,5.2603,5.1638,5.0673,4.9708,4.8743,4.7777,4.7295,4.633,4.4882,4.3917,4.2951,4.2469,4.0056,3.716,3.523,3.4265,3.3782,3.4265,3.3782,3.3299,3.3299,3.4265]
skin_temperature = [31.002,31.021,31.058,31.095,31.133,31.188,31.226,31.263,31.319,31.356,31.412,31.468,31.524,31.581,31.618,31.674,31.712,31.768,31.825,31.862,31.919,31.975,32.013,32.07,32.126,32.164,32.221,32.259,32.296,32.334,32.391,32.448,32.505,32.543,32.6,32.657,32.696,32.753,32.791]
square_heat_flux = []
square_skin_temperature = []
heat_skin = []

for i in heat_flux:
    square_heat_flux.append(i**2)
for i in skin_temperature:
    square_skin_temperature.append(i**2)
for i in range(len(heat_flux)):
    heat_skin.append(heat_flux[i]*skin_temperature[i])

sum_heat_flux = sum(heat_flux)
sum_skin_temperature = sum(skin_temperature)
sum_square_heat_flux = sum(square_heat_flux)
sum_square_skin_temperature = sum(square_skin_temperature)
sum_heat_skin = sum(heat_skin)

beta = (len(heat_flux) * sum_heat_skin - sum_heat_flux * sum_skin_temperature) / (len(heat_flux) * sum_square_heat_flux - sum_heat_flux**2)
alfa = (1 / len(heat_flux)) * sum_skin_temperature - beta * (1 / len(heat_flux)) * sum_heat_flux

x = np.linspace(heat_flux[0]+1,heat_flux[-1]-1)
y = []
for i in x:
    y.append(beta * i + alfa)

plt.plot(x, y, '-')

plt.plot(heat_flux, skin_temperature, '*')
plt.xlabel('Heat Flux')
plt.ylabel('Skin Temperature')
plt.title('Heat Flux - Skin Temperature simple regression')
plt.show()

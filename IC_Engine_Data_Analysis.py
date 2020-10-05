import matplotlib.pyplot as plt
import numpy as np
import math

line_count = 1
crank = []
pressure = []
max_press = []
min_press = []
mean_temp = []
max_temp = []
min_temp = []
mass = []
density = []
temperature = []
volume=[]
integrated_hr=[]
hr_rate = []
c_p = []
c_v = []
gamma = []
kin_visc = []
dyn_visc = []
column_no=[]
properties=[]
units=[]


data_file = input('Type the file name : ')
try:

   file_data = open(data_file,'r')
   
   # File parsing starts here
   for line in file_data:
   
     if line_count is 2:
       for i in range(2,18):
         column_no.append(line.split()[i])
       #print(column_no)
       
       
     if line_count is 3:
       for k in range(0,18):
           properties.append(line.split()[k])
       #print(properties)
       
       
      if line_count is 4:
        for p in range(0,18):
           units.append(line.split()[p])
        #print(units)
        
        
      line_count = line_count + 1
      
      
      if '#' not in line:
      
          crank.append(float(line.split()[0]))
          pressure.append(float(line.split()[1]))
          max_press.append(float(line.split()[2]))
          min_press.append(float(line.split()[3]))
          mean_temp.append(float(line.split()[4]))
          max_temp.append(float(line.split()[5]))
          min_temp.append(float(line.split()[6]))
          volume.append(float(line.split()[7]))
          mass.append(float(line.split()[8]))
          density.append(float(line.split()[9]))
          integrated_hr.append(float(line.split()[10]))
          hr_rate.append(float(line.split()[11]))
          c_p.append(float(line.split()[12]))
          c_v.append(float(line.split()[13]))
          gamma.append(float(line.split()[14]))
          kin_visc.append(float(line.split()[15]))
          dyn_visc.append(float(line.split()[16]))
          
          
column_nos = np.array([[0],crank,pressure,max_press,min_press,mean_temp,max_temp,min_temp,volume,mass,density,integrated_hr,hr_rate,c_p,c_v,gamma,kin_visc,dyn_v])


      print('n Choose Simulation parameters to Generate plot : ')
      print('n 1. Crank n 2. Pressure n 3. max_press n 4. min_press n 5. mean_temp n 6. max_temp n 7. min_temp n 8. volume n 9. mass n 10. density n 11. integrated_hr n 12. hr_rate n 13. c_p n 14. c_v n 15. gamma n 16. kin_visc n 17. dyn_visc')
      x_value = int(input('n Choose parameter on X-axis : '))
      y_value = int(input('n Choose parameter on Y-axis : '))
      
      
      plt.plot(column_nos[x_value],column_nos[y_value],color="red",linewidth = 2)
      plt.xlabel(str(properties[x_value]) + ' ' + str(units[x_value]))
      plt.ylabel(str(properties[y_value]) + ' ' + str(units[y_value]))
      plt.title(str(properties[x_value]) + ' '+'vs'+ ' ' + properties[y_value])
      plt.savefig(str(properties[x_value]) + ' '+'vs'+ ' ' + properties[y_value])
      plt.show()
      
      
     
    if x_value == 2 and y_value == 8 or x_value == 8 and y_value == 2:
      rpm = 1500
      fuel_consumed_perstroke = 20 #micrograms
      N = np.trapz(column_nos[x_value],column_nos[y_value])
      p = (2*math.pi*rpm*N)/(60)
      sfc = ((fuel_consumed_perstroke*rpm)*(pow(10,-6))*(3600))/(p*1000*60)
      
      
    plt.fill_between(column_nos[x_value],column_nos[y_value],linewidth = 2 , color = 'red' , alpha = 0.35)
    plt.show()
    print('n Engine Performance Calculation')
    print('n Area under the pV plot = ', N , 'N-m')
    print('n Power output = ', p, 'MW')
    print('n sfc = ',sfc, 'g/kW-h')
    
    
except FileNotFoundError:
    print("File not recognized. Please provide a valid CONVERGE output file")
    
   
finally:
print("n code exiting")

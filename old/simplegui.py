import PySimpleGUI as sg  
import time    
import serial
import numpy as np

# Abrimos el puerto del arduino a 9600
#arduino = serial.Serial('COM3', 57600)
# Ratio de conversión mm a steps
ustep = 16.
stepturn = 20.
turns = 10.
dist = 30.
#ratio = (turns*stepturn*ustep)/dist
ratio = 106
print (ratio)      

sg.SetOptions(text_justification='right')      

layout = [[sg.Text('Ingresar Objetivo en mm (max.38)', font=('Helvetica', 13), key='head')],            

          [sg.In(default_text='0', size=(4, 1), key='in11'), sg.In(default_text='0', size=(4, 1), key='in12'), sg.In(default_text='0', size=(4, 1), key='in13'),
          sg.ProgressBar(38, orientation='h', size=(5, 20), key='progbar11'),
          sg.ProgressBar(38, orientation='h', size=(5, 20), key='progbar12'),
          sg.ProgressBar(38, orientation='h', size=(5, 20), key='progbar13')],

          [sg.In(default_text='0', size=(4, 1), key='in21'), sg.In(default_text='0', size=(4, 1), key='in22'), sg.In(default_text='0', size=(4, 1), key='in23'),
          sg.ProgressBar(38, orientation='h', size=(5, 20), key='progbar21'),
          sg.ProgressBar(38, orientation='h', size=(5, 20), key='progbar22'),
          sg.ProgressBar(38, orientation='h', size=(5, 20), key='progbar23')],

          [sg.Submit(), sg.Cancel()]]      

window = sg.Window('Demo Dispositivo', layout, font=("Helvetica", 12))      
event = 0
while event != sg.WIN_CLOSED or event == 'Exit' or event == 'Cancel':
	event, values = window.read()
	if event=='Cancel':
		window.close()

	print(event,values)
	# Main Loop
	if values != None:
		input11 = values['in11']
		input12 = values['in12']
		input13 = values['in13']
		input21 = values['in21']
		input22 = values['in22']
		input23 = values['in23']

	 # Validación de tipo de inputs
		chk11 = input11.replace('.','',1).isnumeric()
		chk12 = input12.replace('.','',1).isnumeric()
		chk13 = input13.replace('.','',1).isnumeric()
		chk21 = input21.replace('.','',1).isnumeric()
		chk22 = input22.replace('.','',1).isnumeric()
		chk23 = input23.replace('.','',1).isnumeric()

		print('num:',chk11, chk12, chk13, chk21, chk22, chk23)
		
		if chk11 & chk12 & chk13 & chk21 & chk22 & chk23:

			chkrange11 = (int(float(input11))) <= 38
			chkrange12 = (int(float(input12))) <= 38
			chkrange13 = (int(float(input13))) <= 38
			chkrange21 = (int(float(input21))) <= 38
			chkrange22 = (int(float(input22))) <= 38
			chkrange23 = (int(float(input23))) <= 38
	
	# Validación de rango

			print('range:', chkrange11, chkrange12, chkrange13, chkrange21, chkrange22, chkrange23)

	# Conversión a steps

			stepsfloat = np.array([float(input11), float(input12), float(input13), float(input21), float(input22), float(input23)])*ratio
			steps = stepsfloat.astype(int)

			print(steps)

			if  chkrange11:
				window['progbar11'].update_bar(values['in11'])
				window['head'].update('Ingresar Objetivo en mm (max.38)')
			else:
				window['head'].update('Máximo rango excedido')

			if  chkrange12:
				window['progbar12'].update_bar(values['in12'])
				window['head'].update('Ingresar Objetivo en mm (max.38)')
			else:
				window['head'].update('Máximo rango excedido')

			if  chkrange13:
				window['progbar13'].update_bar(values['in13'])
				window['head'].update('Ingresar Objetivo en mm (max.38)')
			else:
				window['head'].update('Máximo rango excedido')

			if  chkrange21:
				window['progbar21'].update_bar(values['in21'])
				window['head'].update('Ingresar Objetivo en mm (max.38)')
			else:
				window['head'].update('Máximo rango excedido')

			if  chkrange22:
				window['progbar22'].update_bar(values['in22'])
				window['head'].update('Ingresar Objetivo en mm (max.38)')
			else:
				window['head'].update('Máximo rango excedido')

			if  chkrange23:
				window['progbar23'].update_bar(values['in23'])
				window['head'].update('Ingresar Objetivo en mm (max.38)')
			else:
				window['head'].update('Máximo rango excedido')

			if chkrange11 & chkrange12 & chkrange13 & chkrange21 & chkrange22 & chkrange23:
				## Enviar comando por serial
				stringparaenviar = '11,' + str(steps[3]) + ',' + str(steps[4]) + ',' + str(steps[5]) + ',' + str(steps[0]) + ',' + str(steps[1]) + ',' + str(steps[2])
				stringparaenviar = stringparaenviar.encode()
				#arduino.write(stringparaenviar)
				print (stringparaenviar)
		else:
			window['head'].update('Datos Inválidos')
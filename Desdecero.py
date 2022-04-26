###### Imports #######
import sys
import PySimpleGUI as sg  
import time    
import serial
import numpy as np
from mk2robot import MK2Robot
import json
#######################

######## Setup ###############
limits_xyz = [20, 30, 20] # Límite en modo XYZ
limits_angle = [45, 45, 45] # Límite en modo angular
flag_tipo_input = 0 # 0 -> XYZ , 1 -> angular
xcurrent = 0
ycurrent = 0
zcurrent = 0
q0current = 0
q1current = 0
q2current = 0
robot = MK2Robot(link_lengths=[55, 39, 135, 147, 66.3])
delta_xyz = 1 # mm
delta_angular = 1 # grado
#startup_flag = True # Indica primera ejecución
###########################################

############### FUNCIONES #################
def generar_string_comando (modo,x0,x1,x2):
    comm = '{"mode" : %s, "x0" : %s , "x1" : %s , "x2" : %s }' % (modo, x0, x1, x2)
    return comm

def update_current (modo,x0,x1,x2):
# Actualiza el texto de las coordenadas actuales
    global xcurrent
    global ycurrent
    global zcurrent
    global q0current
    global q1current
    global q2current

    if modo == 0:
        xcurrent = float(x0)
        ycurrent = float(x1)
        zcurrent = float(x2)
        try:
            q0current, q1current, q2current = robot.inverse_kinematics(xcurrent,ycurrent,zcurrent)
            print (q0current, q1current, q2current)
            #if startup_flag == False:
            window['xval'].update(str(xcurrent))
            window['yval'].update(str(ycurrent))
            window['zval'].update(str(zcurrent))
            window['q0val'].update(str(q0current))
            window['q1val'].update(str(q1current))
            window['q2val'].update(str(q2current))
        except:
            print ("Fuera de rango")

    elif modo == 1:
        q0current = float(x0)
        q1current = float(x1)
        q2current = float(x2)
        try:
            xcurrent, ycurrent, zcurrent = robot.forward_kinematics(q0current, q1current, q2current)
            print (xcurrent, ycurrent, zcurrent)
            #if startup_flag == False:
            window['xval'].update(str(xcurrent))
            window['yval'].update(str(ycurrent))
            window['zval'].update(str(zcurrent))
            window['q0val'].update(str(q0current))
            window['q1val'].update(str(q1current))
            window['q2val'].update(str(q2current))
        except:
            print ("Fuera de rango")


def move_delta (modo, dir):
    if modo == 0:
        new_x0 = xcurrent
        new_x1 = ycurrent
        new_x2 = zcurrent

        if dir == "+x0":
            new_x0 = new_x0 + delta_xyz

        elif dir == "-x0":
            new_x0 = new_x0 - delta_xyz

        elif dir == "+x1":
            new_x1 = new_x1 + delta_xyz

        elif dir == "-x1":
            new_x1 = new_x1 - delta_xyz

        elif dir == "+x2":
            new_x2 = new_x2 + delta_xyz

        elif dir == "-x2":
            new_x2 = new_x2 - delta_xyz

        else:
            pass

        submit_target (modo, new_x0, new_x1, new_x2)

    elif modo == 1:

        new_x0 = q0current
        new_x1 = q1current
        new_x2 = q2current

        if dir == "+x0":
            new_x0 = new_x0 + delta_angular

        elif dir == "-x0":
            new_x0 = new_x0 - delta_angular

        elif dir == "+x1":
            new_x1 = new_x1 + delta_angular

        elif dir == "-x1":
            new_x1 = new_x1 - delta_angular

        elif dir == "+x2":
            new_x2 = new_x2 + delta_angular

        elif dir == "-x2":
            new_x2 = new_x2 - delta_angular

        else:
            pass

        submit_target (modo, new_x0, new_x1, new_x2)

    else:
        pass     
        # Sumar un delta al valor actual en XYZ en la dirección especificada: +x0,-x0,+x1,-x1,+x2,-x2
        # Enviar comando en modo XYZ
        # Calcular q0, q1, q2
        # Actualizar Valor actual mostrado


def submit_target (modo, x0, x1, x2):
    # Leer campos
    # Armar string de comando
    string_comando = generar_string_comando(modo, x0, x1, x2)
    print (string_comando)
    # Enviar por SSH (?)
    send_command (string_comando)
    # Actualizar valor actual
    update_current (modo,x0,x1,x2)
    print (xcurrent,ycurrent,zcurrent,q0current,q1current,q2current,)

def connect_SSH (path, user, pw):
    # Establecer conexión y loguearse por SSH
    pass

def send_command (comando):
    # Envía el comando de posición vía SSH
    pass

def go_home ():
    global flag_tipo_input
    flag_tipo_input = 1
    submit_target(flag_tipo_input, 45, 90, 90)
############################################

# Enviando a Home #

#if startup_flag:
#    print ('Initializing, going to home position')
#    go_home()
#    startup_flag = False

# Recipe for getting keys, one at a time as they are released
# If want to use the space bar, then be sure and disable the "default focus"

layout = [[sg.Text("Test GUI")],

          [sg.Text("Modo"), sg.OptionMenu(values=("XYZ","Angular"), key='selector',)],

          [sg.Text("Posición Actual")],
          
          [sg.Text("X: "), sg.Text(str(xcurrent), key='xval'), sg.Text("mm"), sg.Text("q0: "), sg.Text(str(q0current), key='q0val'), sg.Text("°") ],

          [sg.Text("Y: "), sg.Text(str(ycurrent), key='yval'), sg.Text("mm"), sg.Text("q1: "), sg.Text(str(q1current), key='q1val'), sg.Text("°") ],

          [sg.Text("Z: "), sg.Text(str(zcurrent), key='zval'), sg.Text("mm"),  sg.Text("q2: "), sg.Text(str(q2current), key='q2val'), sg.Text("°") ],
          
          [sg.Text("Target")],

          [sg.Text("", key='in_x0_title'), sg.In(default_text='0', key='in_x0'), sg.Text("", key='mm_deg0') ],

          [sg.Text("", key='in_x1_title'), sg.In(default_text='0', key='in_x1'), sg.Text("", key='mm_deg1') ],

          [sg.Text("", key='in_x2_title'), sg.In(default_text='0', key='in_x2'), sg.Text("", key='mm_deg2') ],

          [sg.Button("Submit", key='Submit')],      

          [sg.Text("", size=(18, 1), key='text')],

          [sg.Button("Connect", key='Connect'), sg.Button("Home", key='Home'), sg.Button("Exit", key='Exit')]]

window = sg.Window("MyLittleFactory", layout,
                   return_keyboard_events=True, use_default_focus=False)

    
# ---===--- Loop taking in user input --- #
while True:

    event, values = window.read()
    print(event)
    print(values)

    ######### Establecer tipo de input ##########
    # Si selector está en modo XYZ
    if values['selector']=="XYZ":
        #Cambiar las cabeceras y poner flag en modo xyz
        window['in_x0_title'].update("X")
        window['in_x1_title'].update("Y")
        window['in_x2_title'].update("Z")
        window['mm_deg0'].update("[mm]")
        window['mm_deg1'].update("[mm]")
        window['mm_deg2'].update("[mm]")
        flag_tipo_input = 0

    # Si selector está en modo angular
    elif values['selector']=="Angular":
        #Cambiar las cabeceras y poner flag en modo xyz
        window['in_x0_title'].update("q0")
        window['in_x1_title'].update("q1")
        window['in_x2_title'].update("q2")
        window['mm_deg0'].update("[°]")
        window['mm_deg1'].update("[°]")
        window['mm_deg2'].update("[°]")
        flag_tipo_input = 1

    else:
        pass
    #################################################
    #
    #
    #
    ######## Atrapar cierre de ventana ##############    
    if event == sg.WIN_CLOSED:
       break
    if event == "Exit":
       break
    #################################################
    #
    #
    #
    ############## Detectar teclas ###################
    if event in ("Left:37", "a"):
        print("izq")
        move_delta(flag_tipo_input, "-x0")
        # Mover un delta hacia la izq

    if event in ("Up:38", "w"):
        print("adelante")
        move_delta(flag_tipo_input, "+x1")
        # Mover un delta hacia la adelante

    if event in ("Right:39", "d"):
        print("der")
        move_delta(flag_tipo_input, "+x0")
        # Mover un delta hacia la derecha

    if event in ("Down:40", "s"):
        print("atras")
        move_delta(flag_tipo_input, "-x1")
        # Mover un delta hacia atrás

    ##################################################
    # 
    # 
    # 
    ############## Submit ############################
    
    if event == "Submit":
        # Tomar valores de input
        input0 = values['in_x0']
        input1 = values['in_x1']
        input2 = values['in_x2']
        print(input0, input1, input2)
        submit_target(flag_tipo_input, input0, input1, input2)
    
    # ################################################
    # 
    # 
    # 
    # 
    ############# Set Home ###########################    
    if event =="Home":
        go_home()

    ##################################################
    #
    #
    #
    #
    ############ Connect SSH #########################
    if event =="Connect":
        ip=".."
        user=".."
        passw=".."
        connect_SSH(ip, user, passw)


    ###################################################

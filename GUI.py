#!/usr/bin/python
# -*- coding: utf-8 -*-

# Modulos para la interfaz gráfica
from tkinter import *
from tkinter import ttk

# Modulo de sistema
# Lo usaremos para desactivar el keystroke si hacemos hold en alguna tecla
import os
os.system('xset r off')

# Funciones globales
import configs

# Funciones del RC
import rc

# Este archivo contiene constantes que ajudan a cambiar de golpe los estilos
# de colores, letras... 
import style



def App():

    global  root
    # Instancioms la clase tkinter
    root = Tk()

    # Construimos la ventana usando una clase con toda la información
    deadlight = GUI(root)
    
    # Iniciamos bucle
    root.mainloop()
    
    
class GUI:
    
    def __init__( self, deadlight=None ):
        
        # Configuramos dimension de la ventana, posición, background color y titulo
        deadlight.geometry( "500x185+265+105" )
        deadlight.configure( background = style.BG_COLOR )
        deadlight.title( "RC Control" )
        
        # Usaremos el widget style de tkinter para darle color a botones
        self.style = ttk.Style(root)
        
        # Ponemos el id y class de a quien le afectará
        # Y configuramos los colores iniciales
        self.style.configure( 'exitButton.TButton' ,
                              background = style.COLOR_DANGER ,
                              foreground = style.COLOR_WHITE ,
                              font = style.FONT_STYLE_TITLE ,
                              width = 10
                            )
        # En caso de hacer hover/active/focus... el boton cambiara el estilo
        self.style.map( 'exitButton.TButton' ,
                   
                    background = [ ('active', style.COLOR_DANGER_ACTIVE) ],
                   
                    foreground = [],
                   
                    highlightcolor = [],
                    
                    relie = [ ('pressed', 'ridge') ]
                    
                    )

        # Configuramos los labels
        # Donde en función de lo que este haciendo el RC se pondra ver o no .
        # Es como una panel de control en el que ves lo que se activa y lo que se inactiva del RC
        self.lbl_inter_left = Label( root , text =" < " , bg = style.COLOR_INACTIVE , fg = style.COLOR_BLACK , font = style.FONT_STYLE_TXT , width = style.LBL_SQUARE_WIDTH_HEIGHT )
        self.lbl_inter_left.grid(pady = 10 , padx = 5, row = 2 , column = 2 )
        
        self.lbl_up = Label( root , text ="ACELERAR" , bg = style.COLOR_INACTIVE , fg = style.COLOR_BLACK , font = style.FONT_STYLE_TXT , width = style.LBL_FIXED_WIDTH )
        self.lbl_up.grid(pady = 10 , padx = 5, row = 2 , column = 3 )
        
        self.lbl_inter_right = Label( root , text =" > " , bg = style.COLOR_INACTIVE , fg = style.COLOR_BLACK , font = style.FONT_STYLE_TXT , width = style.LBL_SQUARE_WIDTH_HEIGHT )
        self.lbl_inter_right.grid(pady = 10 , padx = 5, row = 2 , column = 4 )

        self.lbl_back = Label( root , text = "MARCHA ATRÁS" , bg = style.COLOR_INACTIVE , fg = style.COLOR_BLACK , font = style.FONT_STYLE_TXT , width = style.LBL_FIXED_WIDTH )
        self.lbl_back.grid(pady = 10 , padx = 5, row = 4 , column = 3)
        
        self.lbl_brake = Label( root , text = "BRAKE" , bg = style.COLOR_SUCCESS , fg = style.COLOR_BLACK , font = style.FONT_STYLE_TXT , width = style.LBL_FIXED_WIDTH )
        self.lbl_brake.grid(pady = 10 , padx = 5, row = 3 , column = 3)
         
        self.lbl_right = Label( root , text = "GIRO DERECHA" , bg = style.COLOR_INACTIVE , fg = style.COLOR_BLACK , font = style.FONT_STYLE_TXT , width = style.LBL_FIXED_WIDTH )
        self.lbl_right.grid(pady = 10 , padx = 5, row = 3 , column = 4)
        
        self.lbl_left = Label( root , text = "GIRO IZQUIERDA" , bg = style.COLOR_INACTIVE , fg = style.COLOR_BLACK , font = style.FONT_STYLE_TXT , width = style.LBL_FIXED_WIDTH )
        self.lbl_left.grid(pady = 10 , padx = 5, row = 3 , column = 2)
        
        self.lbl_lights = Label( root , text = "LIGHTS" , bg = style.COLOR_DISABLED , fg = style.COLOR_BLACK , font = style.FONT_STYLE_TXT , width = style.LBL_FIXED_WIDTH )
        self.lbl_lights.grid(pady = 10 , padx = 5, row = 4 , column = 2)
        
        self.lbl_brake_lights = Label( root , text = "BRAKE LIGHTS" , bg = style.COLOR_DISABLED , fg = style.COLOR_BLACK , font = style.FONT_STYLE_TXT , width = style.LBL_FIXED_WIDTH )
        self.lbl_brake_lights.grid(pady = 10 , padx = 5, row = 4 , column = 4)

        # Botón de Salir
        self.btn_exit = ttk.Button( root ,
                                  text = 'Exit' ,
                                  command = quit ,
                                  style = 'exitButton.TButton' )
        
        # Estilo botón salir
        self.btn_exit.grid(pady = 10 , padx = 5, row = 5 , column = 3)
    
        # Detecta que tecla se pulsa y se suelta
        # En función de lo que haga activar o desactivara motores
        root.bind( "<KeyPress>" , self.move_rc_on )
        root.bind( "<KeyRelease>" , self.move_rc_off )
                 
        
    def move_rc_on( self, event ):
        # Recogemos la telca pulsada
        key = event.keysym
        
        configs.debug( "\nKey pressed : " +
                       str( key ) )
        
        # Esta variable sirve para el control de errores
        # de cuando se activa/desactiva o no un motor
        release = False
        
        # Activamos funciones
        if key == "Up":
            rc.speedUPDOWN_front( self, release )
            
        elif key == 'Down':
            rc.speedUPDOWN_back( self, release )
            
        elif key == 'Right':
            rc.turnUPDOWN_right( self, release )
            
        elif key == 'Left':
            rc.turnUPDOWN_left( self, release )
            
        elif key == 'space':
            rc.handBrake( self );
            
        elif key == 'q':
            rc.leftIntermittent( self )
        
        elif key == 'e':
            rc.rightIntermittent( self )
    
    def move_rc_off(self, event):
        # Recogemos la telca pulsada
        key = event.keysym
        
        configs.debug( "\nKey released : " +
                       str( key ) )
        
        # Esta variable sirve para el control de errores
        # de cuando se activa/desactiva o no un motor
        release = True
        
        # Desactivamos funciones
        if key == "Up":
            rc.speedUPDOWN_front( self, release )
            
        elif key == 'Down':
            rc.speedUPDOWN_back( self, release )
            
        elif key == 'Right':
            rc.turnUPDOWN_right( self, release )
            
        elif key == 'Left':
            rc.turnUPDOWN_left( self, release )
            


if __name__ == '__main__':
    App()


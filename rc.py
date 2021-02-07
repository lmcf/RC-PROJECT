# Funciones globales
from configs import debug

# Este archivo contiene constantes que ajudan a cambiar de golpe los estilos
# de colores, letras... 
import style

# Tiempo
import time

from rc_control import Rccontrol

# Variables para saber que motod hay que activar/desactivar
speed_front = False
speed_back = False
turn_right = False
turn_left = False
hand_brake = True
left_amber = False
right_amber = False

control = Rccontrol()

# Acelerar & marcha atrás
def speedUPDOWN_front( self, release = False ):
    """ Función encargada de acelerar y dar marcha atrás.

        | Hand Brake | Speed up | Speed down |
        |------------|----------|------------|
        |    True    |  False   |   False    |
        |    False   |  False   |   False    |
        |    False   |  True    |   False    |
        |    False   |  False   |   True     |
        
        Parameters
        ----------
        :param release : Boolean
            Variable que nos ajuda al control de cuando ha de acelerar o no.
            Esta sirve para cuando presionas el acelerador y antes de soltar , das marcha atrás,
            y despues sueltas el acelerador, si no fuera por esta variable aceleraria.
            Cuando no deberia hacer nada
    
        Returns
        -------
        :return: Boolean
            Devuelve True si la acción tuvo éxito
                
    """
    global speed_front
    global speed_back
    
    if speed_front is False and release is False and hand_brake is False:
        speed_back = False
        speed_front = True
        
        self.lbl_back.config( bg = style.COLOR_INACTIVE )
        self.lbl_up.config( bg = style.COLOR_SUCCESS )
        
        debug( "Acelerando...\nSpeed front : " +
                      str( speed_front ) +
                      "\nSpeed back : " +
                      str( speed_back ) )
        
    elif speed_front is True and release is True:
        speed_front = False
        
        self.lbl_up.config( bg = style.COLOR_INACTIVE )
        
        debug( "Desacelerando...\nSpeed front : " +
                      str( speed_front ) +
                      "\nSpeed back : " +
                      str( speed_back ) )
        
    if hand_brake is True:
        debug("Freno de mano : " + str(hand_brake))
        
        
def speedUPDOWN_back( self, release ):
    """ inits Spamfilter with training data
        
    :param training_dir: path of training directory with subdirectories
    '/ham' and '/spam'
    """
    global speed_back
    global speed_front
    
    if speed_back is False and release is False and hand_brake is False:
        speed_front = False
        speed_back = True
        
        self.lbl_up.config( bg = style.COLOR_INACTIVE )
        self.lbl_back.config( bg = style.COLOR_SUCCESS )
        
        debug("Acelerando marcha atrás...\nSpeed front : " +
                      str(speed_front) +
                      "\nSpeed back : " +
                      str(speed_back))
        
    elif speed_back is True and release is True:
        speed_back = False
        
        self.lbl_back.config( bg = style.COLOR_INACTIVE )
        
        debug("Desacelerando marcha atrás...\nSpeed front : " +
                      str(speed_front) +
                      "\nSpeed back : " +
                      str(speed_back))
    
    if hand_brake is True:
        debug("Freno de mano : " + str(hand_brake))
        
    
    
    
# Girar derecha
def turnUPDOWN_right( self, release = False ):
    global turn_right
    global turn_left
    
    if turn_right is False and release is False:
        turn_left = False
        turn_right = True
        
        self.lbl_left.config( bg = style.COLOR_INACTIVE )
        self.lbl_right.config( bg = style.COLOR_SUCCESS )
        
        debug( "Girando derecha...\nTurn_right : " +
                      str( turn_right ) +
                      "\nTurn_left : " +
                      str( turn_left ) )
        
        control.servoControl(10)
        
    elif turn_right is True and release is True:
        turn_left = False
        turn_right = False
        
        self.lbl_right.config( bg = style.COLOR_INACTIVE )
        
        debug( "Recto...\nTurn_right : " +
                      str( turn_right ) +
                      "\nTurn_left : " +
                      str( turn_left ) )
        
        control.servoControl()

# Girar izquierda
def turnUPDOWN_left( self, release = False ):
    global turn_left
    global turn_right
    global hand_brake
    
    if turn_left is False and release is False:
        turn_right = False
        turn_left = True
        
        self.lbl_right.config( bg = style.COLOR_INACTIVE )
        self.lbl_left.config( bg = style.COLOR_SUCCESS )
                
        debug("Girando izquierda...\nTurn_right : " +
                      str( turn_right ) +
                      "\nTurn_left : " +
                      str( turn_left ) )
        
        control.servoControl(5)
        
    elif turn_left is True and release is True:
        turn_right = False
        turn_left = False
        
        self.lbl_left.config( bg = style.COLOR_INACTIVE )
        
        debug("Recto...\nTurn_right : " +
                      str( turn_right ) +
                      "\nTurn_left : " +
                      str( turn_left ) )
        
        control.servoControl()


# Freno de mano
def handBrake( self ):
    global hand_brake
    
    if hand_brake is False:
        hand_brake = True
        self.lbl_brake.config( bg = style.COLOR_SUCCESS )
        
    elif hand_brake is True:
        hand_brake = False;
        self.lbl_brake.config( bg = style.COLOR_INACTIVE )
    
    debug("Freno de mano : " + str(hand_brake))
    
# Intermitente izquierdo
def leftIntermittent( self , onoff = True):
    global left_amber
        
    if left_amber is False and onoff is True:
        rightIntermittent(self , False)
        left_amber = True
        #control.leftIntermittent()
        self.lbl_inter_left.config( bg = style.COLOR_INTERMITENTE )
        
    elif left_amber is True:
        left_amber = False
        #control.leftIntermittent(False)
        self.lbl_inter_left.config( bg = style.COLOR_INACTIVE )
        
    else:
        left_amber = False
        self.lbl_inter_left.config( bg = style.COLOR_INACTIVE )
    
    debug("Intermitente izquierdo : " + str(left_amber))
  
  # Intermitente derecho
def rightIntermittent( self , onoff = True):
    global right_amber
    
    if right_amber is False and onoff is True:
        leftIntermittent(self , False)
        right_amber = True
        self.lbl_inter_right.config( bg = style.COLOR_INTERMITENTE )
        
    elif right_amber is True:
        right_amber = False
        self.lbl_inter_right.config( bg = style.COLOR_INACTIVE )
        
    else:
        right_amber = False
        self.lbl_inter_right.config( bg = style.COLOR_INACTIVE )
    
    debug("Intermitente derecho : " + str(right_amber))
    
    
    
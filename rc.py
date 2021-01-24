# Funciones globales
import configs

# Este archivo contiene constantes que ajudan a cambiar de golpe los estilos
# de colores, letras... 
import style

# Variables para saber que motod hay que activar/desactivar
speed_front = False
speed_back = False
turn_right = False
turn_left = False

# Acelerar & marcha atrás
def speedUPDOWN_front( self, release = False ):
    global speed_front
    global speed_back
    
    if speed_front is False and release is False:
        speed_back = False
        speed_front = True
        
        self.lbl_back.config( bg = style.COLOR_INACTIVE )
        self.lbl_up.config( bg = style.COLOR_SUCCESS )
        
        configs.debug( "Acelerando...\nSpeed front : " +
                      str( speed_front ) +
                      "\nSpeed back : " +
                      str( speed_back ) )
        
    elif speed_front is True and release is True:
        speed_front = False
        
        self.lbl_up.config( bg = style.COLOR_INACTIVE )
        
        configs.debug( "Desacelerando...\nSpeed front : " +
                      str( speed_front ) +
                      "\nSpeed back : " +
                      str( speed_back ) )
        
        
def speedUPDOWN_back( self, release ):
    global speed_back
    global speed_front
    
    if speed_back is False and release is False:
        speed_front = False
        speed_back = True
        
        self.lbl_up.config( bg = style.COLOR_INACTIVE )
        self.lbl_back.config( bg = style.COLOR_SUCCESS )
        
        configs.debug("Acelerando marcha atrás...\nSpeed front : " +
                      str(speed_front) +
                      "\nSpeed back : " +
                      str(speed_back))
        
    elif speed_back is True and release is True:
        speed_back = False
        
        self.lbl_back.config( bg = style.COLOR_INACTIVE )
        
        configs.debug("Desacelerando marcha atrás...\nSpeed front : " +
                      str(speed_front) +
                      "\nSpeed back : " +
                      str(speed_back))
    
    
    
# Girar derecha
def turnUPDOWN_right( self, release = False ):
    global turn_right
    global turn_left
    
    if turn_right is False and release is False:
        turn_left = False
        turn_right = True
        
        self.lbl_left.config( bg = style.COLOR_INACTIVE )
        self.lbl_right.config( bg = style.COLOR_SUCCESS )
        
        configs.debug( "Girando derecha...\nTurn_right : " +
                      str( turn_right ) +
                      "\nTurn_left : " +
                      str( turn_left ) )
        
    elif turn_right is True and release is True:
        turn_left = False
        turn_right = False
        
        self.lbl_right.config( bg = style.COLOR_INACTIVE )
        
        configs.debug( "Recto...\nTurn_right : " +
                      str( turn_right ) +
                      "\nTurn_left : " +
                      str( turn_left ) )

# Girar izquierda
def turnUPDOWN_left( self, release = False ):
    global turn_left
    global turn_right
    
    if turn_left is False and release is False:
        turn_right = False
        turn_left = True
        
        self.lbl_right.config( bg = style.COLOR_INACTIVE )
        self.lbl_left.config( bg = style.COLOR_SUCCESS )
                
        configs.debug("Girando izquierda...\nTurn_right : " +
                      str( turn_right ) +
                      "\nTurn_left : " +
                      str( turn_left ) )
        
    elif turn_left is True and release is True:
        turn_right = False
        turn_left = False
        
        self.lbl_left.config( bg = style.COLOR_INACTIVE )
        
        configs.debug("Recto...\nTurn_right : " +
                      str( turn_right ) +
                      "\nTurn_left : " +
                      str( turn_left ) )

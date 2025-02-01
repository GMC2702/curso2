# condicionales AND OR OR
# AND REVISA QUE AMBAS CONDICIONES SEAN VERDADERAS
# OR REVISA AL MENOS UNA DE LAS CONDICIONES SE CUMPLA 1
acceso_usuario = True
acceso_admin = False
if acceso_usuario or acceso_admin:
    print('ACCESO TOTAL')
elif acceso_usuario:
    print('El usuario está autenticado')
else:
    print('El usuario no está autenticado')
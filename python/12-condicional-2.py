#Condicional EL IF IFEL ELSE
# tipo = 'estudiante'

# if tipo =='estudiante':
#     print('Tienes un descuento del 50%')
# elif tipo=='profesor':
#     print('Tienes un descuento del 80%')
# elif tipo=='invitado':
#     print('Tienes un descuento del 10%')
# else:
#     print('No hay descuento')


# tipo_usuario = 'usuario'

# if tipo_usuario =='super admin':
#     print('Puedes borrar la página con un click')

# elif tipo_usuario =='admin':
#     print('Puedes borrar usuarios')

# elif tipo_usuario =='usuario':
#     print('Puedes ingresar a la página')

# elif tipo_usuario=='hacker':
#     print('Puedes irte baneado')

# else:
#     print('Ingrese sus datos')

usuario = 'geraldo2'
tipoUsuario = 'admin'
tiposUsuarios = ['admin', 'superadmin', 'usuario']

if tipoUsuario in tiposUsuarios and usuario == 'geraldo2':
    print(f'entras {tipoUsuario} {usuario}')
else:
    print('el usuario no puede entrar al sistema')
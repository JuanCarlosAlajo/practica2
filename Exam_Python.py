from os import system

def fn_presentacion():
    system("cls")
    print('###############################################')
    print('## MAESTRIA EN CIBERSEGURIDAD                ##')
    print('## Introducción a Python                     ##')
    print('## Autor : Juan Carlos Alajo                 ##')
    print('## Tema : Registro de equipos portátiles     ##')
    print('###############################################')

#inicializar presentación
fn_presentacion()
print('Opciones')
print('--------')
vld_tipo_reg={'1':'<INGRESO>','2':'<SALIDA>'}
vlt_marcas_eq={'1':'HP','2':'LENOVO','3':'ASUS','4':'TOSHIBA','5':'OTRO'}
for i,j in vld_tipo_reg.items():
    print(i,j)

#--tipo de registro
vln_id_tipo_reg=int(input('seleccione el tipo de registro --> '))
while vln_id_tipo_reg not in (1,2):
    print('Lo siento. El tipo de registro No es correcto!')
    vln_id_tipo_reg = int(input('seleccione un tipo de registro válido --> '))

'''
if vln_id_tipo_reg==1:
   print('Proceda a solicitar información tipo : '+vld_tipo_reg['1'])
else:
   print('Proceda a solicitar información tipo : '+vld_tipo_reg['2'])
'''
#---marcas de equipos
vln_id_marca=int(input('seleccione la marca del equipo --> '))
for x,y in vlt_marcas_eq.items():
    print(x,y)

while vln_tipo_reg not in (1,2,3,4,5):
    print('Lo siento. La marca del equipo seleccionado No es correcto!')
    vln_id_marca = int(input('seleccione una marca de equipo válido --> '))


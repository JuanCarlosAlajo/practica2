from os import system

#------- definición de funciones ------------
def fn_presentacion():
    system("cls")
    print('###############################################')
    print('## MAESTRIA EN CIBERSEGURIDAD                ##')
    print('## Introducción a Python                     ##')
    print('## Autor : Juan Carlos Alajo                 ##')
    print('## Tema : Registro de equipos portátiles     ##')
    print('###############################################')
def fn_menu(val_param='valor'):
    print('--------')
    print(val_param)
    print('--------')

def fn_registrar_inf(p_tiporeg,p_marca,p_numserie,p_codemp,p_nomemp):
    try:
        vld_reg_final['Tipo ->'] = p_tiporeg
        vld_reg_final['Marca ->'] = p_marca
        vld_reg_final['No.Serie ->'] = p_numserie
        vld_reg_final['Cod.Emp ->'] = p_codemp
        vld_reg_final['Nombre Emp ->'] = p_nomemp
        print('')
        print('<<<  INFORMACION REGISTRADA CON EXITO   >>>')
    except Exception as inst:
        print('Error: ', inst)

#------- definicion de diccionarios ------
vld_tipo_reg={'1':'INGRESO','2':'SALIDA'}
vlt_marcas_eq={'1':'HP','2':'LENOVO','3':'ASUS','4':'TOSHIBA','5':'OTRO'}
vld_reg_final = {}

try:
    vlc_soliresp='S'
    while vlc_soliresp.upper()=='S':
        fn_presentacion()
        #------- tipo de registro -------
        fn_menu('Opciones')
        for i,j in vld_tipo_reg.items():
            print(i,j)
        vln_id_tipo_reg=int(input('seleccione el tipo de registro --> '))

        while vln_id_tipo_reg not in (1,2):
            print('Lo siento. El tipo de registro No es correcto!')
            vln_id_tipo_reg = int(input('seleccione un tipo de registro válido --> '))


        #------ marcas de equipos -------
        fn_menu('Marcas')
        for x,y in vlt_marcas_eq.items():
            print(x,y)
        vln_id_marca=int(input('seleccione la marca del equipo --> '))

        while vln_id_marca not in (1,2,3,4,5):
            print('Lo siento. La marca del equipo seleccionado No es correcto!')
            vln_id_marca = int(input('seleccione una marca de equipo válido --> '))

        #------ Información Adicional -------
        fn_menu('Adicional')
        vlc_serie_equipo=input('Ingrese el No. serial del Equipo --> ')
        vlc_cod_empleado=input('Ingrese el Código del funcionario --> ')
        vlc_nom_empleado=input('Ingrese el Nombre del funcionario --> ')

        #---- registrar información -------
        fn_registrar_inf(vld_tipo_reg.get(str(vln_id_tipo_reg)),vlt_marcas_eq.get(str(vln_id_marca)),vlc_serie_equipo,vlc_cod_empleado,vlc_nom_empleado)

        vlc_req_print=input('Digite ENTER para imprimir el resumen del registro ...')

        #----- impresión del registro -----
        fn_menu('Resumen')
        for m,n in vld_reg_final.items():
            print(m,n)

        #---- encerar diccionario ---------
        vld_reg_final.clear()

        print('')
        vlc_soliresp=input('Desea registrar a otro funcionario (S/N)...?')

except Exception as inst:
    print('Error: ', inst)

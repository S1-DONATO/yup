OpiMenuPri=5
cargos=("CEO","DESARROLLADOR","ANALISTA DE DATOS")
def seleccionar_cargo():
    while True:
        for i in range(len(cargos)):
            print(f"{i+1}- {cargos[i]}")
            
        opiCargo=int(input("Seleccione el cargo correspondiente: "))
        if(opiCargo<1 or opiCargo>len(cargos)):
            print("Debe seleccionar alguno de los cargos disponibles.")
        else:
            cargo=cargos[opiCargo-1]
            return cargo
        
def crear_trabajador():
    nombre=input("Ingrese el nombre del trabajador: ")
    cargo=seleccionar_cargo()
    while True:
        try:
            sueldoBruto=int(input("Ingrese el sueldo bruto: "))
        except ValueError:
            print("Debe ingresar solamente numeros.")
        else:
            break
        
    #descuentos
    descuentoSalud=sueldoBruto*0.07
    descuentoAFP=sueldoBruto*0.12
    descuentoTotal=descuentoAFP+descuentoSalud
    #calculo sueldo
    sueldoLiquido=sueldoBruto-descuentoTotal
    trabajador=[nombre,cargo,sueldoBruto,descuentoSalud,descuentoAFP,sueldoLiquido]
    return trabajador

def agregar_trabajador(trabajador,trabajadores=None):
    if trabajadores==None:
        trabajadores=[trabajador]
    else:
        trabajadores.append(trabajador)
        
    return trabajadores
    
def listar_trabajadores(trabajadores):
    for trabajador in trabajadores:
        print(trabajador)
        

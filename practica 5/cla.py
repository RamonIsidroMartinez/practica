class alumno:
    
    def nombrecompleto(self,nombre,apellido):
        return nombre+""+apellido
    
alu = alumno()
nombre = input("nombre...")
apellido = input("apellido...")
print(alu.nombrecompleto(nombre,apellido)) 
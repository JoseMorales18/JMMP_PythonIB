class Persona:
    nombre = ''
    escuela= ''
     
    def print_nombre(self):
        print (self.nombre)
         
    def print_escuela(self):
        print (self.escuela)
     
a = Persona()
a.nombre = 'Jose'
a.escuela = 'Facultad de Ingenieria Mecanica y Electrica'
a.print_nombre()
a.print_escuela()

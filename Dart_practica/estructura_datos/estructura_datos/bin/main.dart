class Persona{
  String nombre;
  int edad;
  Persona(this.nombre);
}


void main(List<String> arguments) {
  

  //lista de objetos
  var diego = new Persona("diego");
  var david = new Persona("david");
  var mike = new Persona("mike");

  var list = new List<Persona>();
  list.add(diego);
  list.add(david);
  list.add(mike);

  for(int i = 0; i<list.length; i++){
    print(list[i].nombre);
  }

  //lista
  var lista2 = [ 1,2,4,10,7];
  lista2.add(6);

  for(int i=0; i< lista2.length;i++){
    print("indice $i  elemento ${lista2[i]}");
  }

}

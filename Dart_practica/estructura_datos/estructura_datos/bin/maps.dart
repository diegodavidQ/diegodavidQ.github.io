void main(List<String> arguments) {
  var persona = {
    "nombre":"Diego",
    "edad":28,
    "telefono":1234
  };

  print(persona["nombre"]);

  persona.forEach((k,v) => print(k+" : "+v.toString()));

  var keys = persona.keys;
  print("Keys: "+keys.toString());

}
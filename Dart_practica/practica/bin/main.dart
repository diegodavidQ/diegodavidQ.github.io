
void main(List<String> arguments) {
  

/* Condicionales */ 
//###################################//
var numero = 10;
var n = 100;

if (numero<n){
  print("numero < n");
}
else{
  print("numero > n");
}
//as, is, !is
print((numero is String));

//###################################//
/* Switches */ 
var x= 10;

switch(x){
  case 1:
  print("1");
  break;
  case 2:
  print("2");
  break;
  default:
  print("ninguno");
  break;

}

//###################################//
//llamada a función
String resultado = miFuncion("inicial");
print(resultado);
//###################################//

}//fin de main



//###################################//
/* Funciones */ 

//[parámetro opcional = valor por defecto]
String miFuncion(String args, [int valor=2]){
  return "mi Funcion $args " + valor.toString() ;
}
//###################################//
/* Funciones */ 



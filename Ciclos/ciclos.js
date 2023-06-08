var x;
var resp = 'y';
var y;

function ninio()
{
  for (var i = 0; i < x; i++)
  {
    document.write("Eres un ninio ");
  }
}
function adolescente()
{
  for (var i = 0; i < x; i++)
  {
    document.write("Eres un adolescente ");
  }
}
function adulto()
{
  for (var i = 0; i < x; i++)
  {
    document.write("Eres un adulto ");
  }
}
function viejo()
{
  for (var i = 0; i < x; i++)
  {
    document.write("Eres viejo y oxidado ");
  }
}
function testamento()
{
  for (var i = 0; i < x; i++)
  {
    document.write("Ya tienes tu testamento? ");
  }
}
function limites()
{
  for (var i = 0; i < x; i++)
  {
    document.write("Esos limites de edad no son muy humanos!");
  }
}
function conSwitch()
{
  document.write(",pero con switch");
}

do
{
  x = parseInt(prompt("Cuantos anios tiene? "));
  if (x >= 0 && x <= 11)
  {
    ninio();
  }
  else if (x <= 12 && x <= 17)
  {
    adolescente();
  }
  else if (x <= 18 && x <= 40)
  {
    adulto();
  }
  else if (x <= 41 && x <= 60)
  {
    viejo();
  }
  else if (x <= 61 && x <= 120)
  {
    testamento();
  }
  else
  {
    limites()
  }
  resp = parseInt(prompt("¿Que quieres hacer? (1 continuar, 2 finalizar)"));
}
while(resp == 'y' || resp == 'Y')

y = parseInt(prompt("Cuantos anios tiene, pero con switch? "));
while (resp == 'y' || resp == 'Y')
{
  switch (y)
  {
    case y >= 0 && y <= 11: ninio(); conSwitch();
    break;
    case y <= 12 && y <= 17: adolescente(); conSwitch();
    break;
    case y <= 18 && y <= 40: adulto(); conSwitch();
    break;
    case y <= 41 && y <= 60: viejo(); conSwitch();
    break;
    case y <= 61 && y <= 120: testamento(); conSwitch();
    break;
    default: limites(); conSwitch();
    break;
  }
}

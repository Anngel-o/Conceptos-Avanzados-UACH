var x;
var resp = 1;
var ec;
var y;

function calcY()
{
  y = Math.random() * 5;
}

function main()
{
  do
  {
    x = parseInt(prompt("Agrega valor a x: "));
    resp = parseInt(prompt("¿Que quieres hacer? (1 continuar, 2 finalizar)"));

    calcY();
    ec = parseFloat(( ( Math.pow(x,2) + 20) / (y + 10) )).toFixed(2);

    document.write(ec);
  }
  while(resp == 1)
}


main();

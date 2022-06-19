# MangaPrintablePDF
Este repositorio es un intento para hacer una utilidad que ayude con la generación de un archivo PDF para la impresión de Manga.

## El Problema
Al momento de descargar manga desde Internet (Por favor, obtenerlo de manera legal) surgen problemas al momento de querer realizar su impresión en el sentido original de lectura Japones (De derecha a Izquierda). Por lo menos cuando se desea hacer con impresoras caseras, a doble cara, y doblándolo por medio, en resumidas cuentas queriendo dejarlo como los tomos originales de manga.

Sucede que los capítulos, los tomos, ya sea en CBR o en PDF que usualmente se obtienen en Internet vienen en el orden de lectura (1-2-3-4), además hay páginas de por medio que son dobles, por lo que los lectores de PDF (O por lo menos yo no pude hacerlo 😅) no pueden imprimir de manera correcta un manga, no como los tomos originales. 

Por lo que la finalidad de esta herramienta es generar un PDF que sea factible para imprimir, siguiendo un patrón de las hojas 1-4-3-2 para que sea factible imprimirlo a doble cara, poder doblar las hojas y ensamblar el manga completo, además respetando las páginas dobles.
## Requerimientos
 - Python3
 - Pillow (PIL Fork)
 - Reportlab
## Uso
Por el momento su utilización es compleja, prácticamente hay que editar el código fuente para introducirle los parámetros de funcionamiento. Por lo que por el momento no voy a hacer una explicación detallada de su utilización, en esta etapa tampoco está apto para su uso por el público general, aunque si ya permite generar PDF pero requiere de pre-procesamiento manual, además de introducir los parametros y variables dentro del código.

Según vaya teniendo la oportunidad trabajaré para facilitar su utilización, y en un futuro de ser posible me gustaría crear una interfaz gráfica para su utilización.
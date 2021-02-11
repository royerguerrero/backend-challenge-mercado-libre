# Problem Overview
Han Solo ha sido recientemente nombrado General de la Alianza
Rebelde y busca dar un gran golpe contra el Imperio Galáctico para
reavivar la llama de la resistencia.
El servicio de inteligencia rebelde ha detectado un llamado de auxilio de
una nave portacarga imperial a la deriva en un campo de asteroides. El
manifiesto de la nave es ultra clasificado, pero se rumorea que
transporta raciones y armamento para una legión entera.

## Challenge
Como jefe de comunicaciones rebelde, tu misión es crear un programa en Python que retorne
la fuente y contenido del mensaje de auxilio. Para esto, cuentas con tres satélites que te
permitirán triangular la posición, ¡pero cuidado! el mensaje puede no llegar completo a cada
satélite debido al campo de asteroides frente a la nave.

**Posición de los satélites actualmente en servicio**
- Kenobi: [-500, -200]
- Skywalker: [100, -100]
- Sato: [500, 100]

# Use Cases
- Crear una función para rearmar el mensaje luego del ruido emitido por los asteroides
- Crear una función que permite triangular la posición usando el algoritmo de
trilateración
- Crear un servicio que permita recibir la distancia de cada satélite a su emisor
y el mensaje recibido por dicho satélite para que este retorne el mensaje limpiando el ruido y la posición del emisor de la señal
- Crear un segundo servicio que permita recibir la información de la distancia y mensaje cada satélite por separado y cuando este tenga los datos suficientes para poder retornar el mensaje y la posición lo haga
- Despliegue de la API en cualquier cloud (AWS, Azure, GCP, ...)

### Out to scope
- Crear un sistema de autenticación para proteger los endpoints topsecret
- Crear validadores para errores (En lugar de ello se responderá 404)

# Proposal
## Architecture
El sistema propuesto contempla la construcción de una API usando [FastAPI](https://fastapi.tiangolo.com/) un framework de python de alto performance, dicha API será desplegada usando Docker en una instancia EC2 sobre AWS Cloud.

Las funciones descritas en los primeros casos de uso se realizarán de la siguiente manera

1. Para eliminar el ruido del mensaje se usará una tabla de hash para insertar cada parte del mensaje que no sea vacía, luego dicha tabla se ordenará y por último se unirá en un string.
2. La función de triangulación se usará [Trilateración 2D](https://es.wikipedia.org/wiki/Trilateraci%C3%B3n) para lograr hallar la distancia basandose en la solucion matematica planteada en el articulo titulado ([Cell Phone Trilateration Algorithm](https://www.101computing.net/cell-phone-trilateration-algorithm/)) que se encuentra en [101Computing.net](https://www.101computing.net/)

## Architecture Diagram
![Architecture Diagram Image](architecture_diagram.jpg)


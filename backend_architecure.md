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
- Crear una funcion para rearmar el mensaje luego del ruido emitido por los asteroides
- Crear una funcion que permita triangular la posicion usando el algoritmo de
trilateracion
- Crear un servicio que permita recibir la distancia de cada satelite a su emisor
y el mensaje recibido por dicho satelite para que este retorne el mensaje limpiando el ruido y la posicion del emisor de la señal
- Crear un segundo servicio que permita recivir la informacion de la distacia y mensaje cada satelite por separado y cuando este tenga los datos suficientes para poder retornar el mensaje y la posicion lo haga
- Despliege de la API en cualquier cluod (AWS, Azure, GCP, ...)

### Out to scope
- Crear un sistema de autentificacion para protejer los endpoints topsecret
- Crear validadores para errores (En lugar de ello se respondera 404)

# Proposal
## Architecture
El sistema propuesto sera la construccion de una API usando [FastAPI](https://fastapi.tiangolo.com/) un framework de python de alto performance, dicha api sera desplegada usando Docker en una instancia EC2 sobre AWS Cloud.

## Architecture Diagram

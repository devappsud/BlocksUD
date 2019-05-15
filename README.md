# blocksUD

Simulador del comportamiento de una cadena de bloques

Una transacción puede representar la transferencia de valor, la validación de un documento o el registro de propiedad de un activo.
Un usuario debe iniciar la transacción (origen) desde una aplicación de usuario, denominada “Billetera” en la cual se provee el api para el envío de un activo de información o de valor, y el procedimiento continúa de la siguiente manera: El sistema crea la transacción previo validación de la viabilidad de la misma.

La nueva transacción se adiciona al posible nuevo bloque, el cual está integrado por todas las transacciones no confirmadas. El bloque candidato a ser integrado en la blockchain es enviado a todos los nodos mineros para su corroboración. Cada nodo minero dispone de una copia actualizada de la cadena de bloques, evalúa el nuevo bloque y resuelve la prueba de trabajo. Ésta versión implementa una prueba de trabajo soportada en cálculo de números primos, en la cual el valor de minado debe generar un número primo a partir de la suma de los números contenidos en la cadena y del valor para el nuevo bloque. El nodo minero que resuelva el problema en el menor tiempo posible, recibirá la recompensa expresada en una cantidad determinada de una hipotética criptomoneda y adicionará el bloque a la cadena. Cada vez que un bloque se agrega a la cadena, se envía una notificación a todos los mineros para que se actualicen. El usuario destino no interviene en este proceso, al finalizar el trabajo y el bloque es agregado en la cadena, todas las transacciones involucradas notifican a la aplicación final de los usuarios la correcta culminación. Es muy importante aclarar que este diseño para efectos de agilizar los cálculos y evitar retardos por acceso a disco, la cadena de bloques se crea y mantiene en memoria principal (R.A.M). No se ha realizado persistencia en disco duro.

La implementación del prototipo se realizó en lenguaje de programación Python versión 3.3 con el IDE Spyder 3.7 y la simulación se realiza con datos pseudo aleatorios de transacciones que emulan el funcionamiento de una blockchain, cada usuario debe pertenecer a un pool de minería con una capacidad de cómputo específica, y se realiza una distribución proporcional de usuarios entre los pools de minería definidos.

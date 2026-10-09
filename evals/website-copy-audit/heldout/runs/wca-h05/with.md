# Auditoría del texto de la página principal

**Lectura de un desconocido:** al ver solo el titular y el subtítulo, no sabría que es un taller de bicis de Zaragoza, ni que puede reservar cita, ni cuánto cuesta. El titular podría ser de cualquier tienda de bicis del país.

**Suposiciones:** el público son ciclistas urbanos y de ocio de Zaragoza. El objetivo es que reserven cita en la web en lugar de llamar. No he podido revisar el diseño, el PDF de precios ni ninguna otra página.

## Hallazgos (por orden de prioridad)

**1. Mayor: no hay forma de reservar cita.**
- Texto: el formulario pide "Nombre, Email, Mensaje. Botón: Enviar".
- Es un formulario de contacto, no de reserva. No pregunta qué servicio quieres, qué bici tienes ni qué día te viene bien. El cliente tendría que redactar una petición y esperar respuesta, y llamar es más rápido.
- Arreglo: convertirlo en solicitud de cita con estos campos: servicio (desplegable con los tres servicios), tipo de bici, fecha preferida, teléfono y comentario opcional. Si no tenéis agenda online, el formulario puede ser una solicitud, siempre que digáis cuándo respondéis.
- Botón: "Enviar" → **"Pedir cita"**.
- Añadid debajo una línea con la respuesta: "Te confirmamos la cita en [plazo real]".

**2. Mayor: precios y plazos están ocultos.**
- Texto: "Revisión básica · Revisión completa · Puesta a punto premium", sin precio, sin plazo y sin contenido. El PDF no está enlazado.
- Quien duda entre reservar y llamar suele querer saber cuánto cuesta y cuándo tendrá la bici. Si la web no lo dice, llama. Es probablemente la causa principal de las llamadas.
- Arreglo: poned bajo cada servicio qué incluye, el precio "desde" y el plazo, tomados del PDF. Si no queréis publicar precios, poned al menos el plazo y qué incluye. Mejor aún, publicad el contenido del PDF como texto en la página, que se lee mejor que un PDF en el móvil.
- Plantilla: **Revisión básica** — [qué incluye en una línea] · desde [X] € · lista en [plazo].

**3. Mayor: el botón no lleva a ninguna acción.**
- Texto: "Más información".
- No dice a dónde lleva, y ya sabemos que no hay más información enlazada. Aleja al visitante de la reserva en vez de acercarlo.
- Arreglo: **"Pedir cita"** o **"Reservar revisión"**, que lleve al formulario. Si tenéis un botón por servicio, "Reservar [servicio]".

**4. Mayor: los tres servicios no se distinguen.**
- Texto: "Revisión básica · Revisión completa · Puesta a punto premium".
- Un cliente que no sabe de mecánica no puede elegir. ¿Qué diferencia hay entre "completa" y "premium"? Si no lo sabe, no reserva o llama a preguntar.
- Arreglo: una línea por servicio con el problema que resuelve, con vuestras palabras. Ejemplo de estructura: "Revisión básica: para la bici que usas a diario y quieres que siga fina" → completa → premium. Rellenad con lo que incluye cada una, que solo vosotros lo sabéis.

**5. Mayor: el titular no dice qué sois ni dónde.**
- Texto: "Pasión por las dos ruedas desde siempre".
- No aparecen "taller", "bicis" ni "Zaragoza". "Desde siempre" tampoco dice nada comprobable. Cualquier competidor podría firmarlo.
- Arreglo (solo con datos que ya me habéis dado): **"Taller de bicicletas en Zaragoza"** como titular o como línea justo encima. Si queréis conservar la voz, dejad "Pasión por las dos ruedas" como segunda línea y quitad "desde siempre". Si tenéis un año de fundación, "Desde [año]" sí es una afirmación comprobable y sería mejor.

**6. Medio: el subtítulo es genérico.**
- Texto: "servicios integrales de mantenimiento y reparación con la máxima calidad y un trato cercano y profesional".
- "Integrales", "máxima calidad", "cercano" y "profesional" son adjetivos que todo taller se atribuye, y "máxima calidad" no se puede comprobar. Además no dice qué gana el cliente.
- Arreglo: sustituir por un beneficio concreto que podáis respaldar, p. ej. "Reparamos y revisamos tu bici en [plazo]. Pide cita en un minuto." Si el plazo no es fijo, usad el real más habitual o quitad la promesa de plazo.

**7. Medio: "Por qué elegirnos" no da ninguna razón.**
- Texto: "Somos un equipo apasionado y comprometido con tus necesidades."
- Habla de vosotros, no da un motivo verificable y repite la "pasión" del titular. El visitante no sale sabiendo por qué elegiros frente a otro taller.
- Arreglo: sustituirla por 3 razones concretas y ciertas. Algunas que tal vez podáis dar, que debéis confirmar: años en el barrio, marcas que reparáis, garantía en la reparación, presupuesto antes de empezar, recogida o reparación en el día. No las pongo como hechos porque no me las habéis dado: `[razón 1]`, `[razón 2]`, `[razón 3]`.

**8. Medio: faltan los datos prácticos.**
- No aparece dirección, horario ni teléfono en el texto que me habéis pegado (puede que estén en otra parte).
- Quien sí prefiere llamar necesita el teléfono a mano, y quien viene a dejar la bici necesita la dirección y el horario. Ponedlos cerca de la reserva.

**Otros detalles:** el formulario no dice qué pasa después de enviarlo (mensaje de confirmación y plazo). Conviene una frase de confirmación tipo "Recibido. Te escribimos a [email] en [plazo]".

## Lo que funciona

- **"trato cercano"**: la idea es buena, pero necesita una prueba concreta. Si tenéis un ejemplo real (presupuesto antes de tocar nada, explicar la avería), usadlo en lugar del adjetivo.
- **"mantenimiento y reparación"**: sí dice qué hacéis, en palabras que el cliente usa. Conservadlo.
- **Los tres niveles de servicio**: la estructura básica, completa y premium es clara. El problema es la falta de detalle, no la estructura.

## Orden de arreglos

1. **Convertir el formulario en solicitud de cita** y cambiar el botón a "Pedir cita" (medio).
2. **Publicar precios, plazos y contenido de cada servicio** a partir del PDF (pequeño o medio, es copiar y ordenar).
3. **Cambiar "Más información" por un botón que lleve al formulario** (pequeño).
4. **Reescribir el titular** para incluir "taller de bicicletas en Zaragoza" (pequeño).
5. **Sustituir "Por qué elegirnos"** por razones concretas y verificables (medio, necesita vuestros datos).

**Para medir:** apuntad durante unas semanas cuántas llamadas preguntan por precio o plazo y cuántas citas entran por la web, para comprobar si el cambio funciona.

Si me pasáis el contenido del PDF y qué incluye cada servicio, os preparo el texto completo de la sección de servicios.

No he podido guardar el archivo porque la herramienta de escritura está desactivada en esta sesión. Te dejo el HTML completo aquí. Guárdalo como `index.html` y ábrelo en el navegador.

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>La Herramienta Compartida · Biblioteca de herramientas en Villaverde del Mar</title>
<meta name="description" content="Una biblioteca de herramientas de barrio en Villaverde del Mar. Abrimos el 14 de marzo en la calle Tejares 14. Más de 120 herramientas para tomar prestadas.">
<style>
  :root {
    --crema: #fbf5ea;
    --tinta: #3a2a1d;
    --terracota: #c4572f;
    --terracota-oscuro: #9c3f1d;
    --arena: #f0e3cc;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    font-family: Georgia, "Times New Roman", serif;
    background: var(--crema);
    color: var(--tinta);
    line-height: 1.6;
    font-size: 18px;
  }
  .contenedor { max-width: 760px; margin: 0 auto; padding: 0 24px; }
  header.hero {
    text-align: center;
    padding: 72px 0 56px;
    background: var(--arena);
    border-bottom: 6px solid var(--terracota);
  }
  .etiqueta {
    display: inline-block;
    background: var(--terracota);
    color: #fff;
    font-family: system-ui, sans-serif;
    font-size: 14px;
    letter-spacing: .08em;
    text-transform: uppercase;
    padding: 6px 14px;
    border-radius: 999px;
  }
  h1 { font-size: clamp(2.2rem, 6vw, 3.4rem); line-height: 1.1; margin: 20px 0 12px; }
  .lema { font-size: 1.25rem; max-width: 560px; margin: 0 auto; }
  section { padding: 44px 0 8px; }
  h2 { font-size: 1.7rem; margin: 0 0 14px; color: var(--terracota-oscuro); }
  .tarjetas { display: grid; gap: 16px; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); margin-top: 16px; }
  .tarjeta { background: #fff; border: 2px solid var(--arena); border-radius: 14px; padding: 20px; }
  .tarjeta strong { display: block; font-size: 1.6rem; color: var(--terracota); }
  .tarjeta span { font-family: system-ui, sans-serif; font-size: 15px; }
  .inauguracion {
    margin: 52px 0 0;
    background: var(--terracota);
    color: #fff;
    text-align: center;
    padding: 44px 24px;
  }
  .inauguracion h2 { color: #fff; }
  .inauguracion p { margin: 6px 0; }
  .fecha { font-size: 2rem; font-weight: bold; }
  footer { text-align: center; padding: 28px 0 40px; font-family: system-ui, sans-serif; font-size: 14px; }
</style>
</head>
<body>

<header class="hero">
  <div class="contenedor">
    <span class="etiqueta">Muy pronto en el barrio</span>
    <h1>La Herramienta Compartida</h1>
    <p class="lema">¿Para qué comprar un taladro que usarás dos veces? Una biblioteca de herramientas para todo el barrio de Villaverde del Mar.</p>
  </div>
</header>

<main>
  <div class="contenedor">

    <section>
      <h2>Cómo funciona</h2>
      <p>Es como una biblioteca, pero en vez de libros prestamos herramientas. Te haces socio, eliges lo que necesitas, te lo llevas a casa y lo devuelves cuando termines el arreglo. Así de sencillo.</p>
    </section>

    <section>
      <h2>Más de 120 herramientas</h2>
      <p>Taladros, lijadoras, escaleras, sierras de calar, carretillas… y mucho más para tus obras, tu huerto o ese estante que lleva meses esperando.</p>
    </section>

    <section>
      <h2>Lo que necesitas saber</h2>
      <div class="tarjetas">
        <div class="tarjeta"><strong>25 € al año</strong><span>o 3 € al mes, tú eliges.</span></div>
        <div class="tarjeta"><strong>Hasta 7 días</strong><span>de préstamo por herramienta.</span></div>
        <div class="tarjeta"><strong>Sin fianza</strong><span>No dejas ningún depósito.</span></div>
      </div>
      <p style="margin-top:20px">La primera vez te pedimos una <strong>charla de seguridad de 30 minutos</strong>, para que uses cada herramienta con confianza.</p>
    </section>

  </div>

  <div class="inauguracion">
    <div class="contenedor">
      <h2>Te esperamos en la inauguración</h2>
      <p class="fecha">14 de marzo</p>
      <p><strong>Calle Tejares 14</strong>, Villaverde del Mar</p>
      <p style="margin-top:18px">Horario habitual<br>
        Miércoles de 17 a 20 h · Sábados de 10 a 14 h</p>
    </div>
  </div>
</main>

<footer>
  La Herramienta Compartida · Calle Tejares 14 · Villaverde del Mar
</footer>

</body>
</html>
```

**Qué he hecho y qué he dejado fuera**
- **Solo tus datos.** No hay testimonios, cifras de socios, teléfono, email ni formulario, porque no los tenías. El texto de "Cómo funciona" describe el préstamo de forma general, sin añadir reglas nuevas.
- **Sin año en la fecha.** Pone "14 de marzo" a secas. Hoy es 7 de octubre de 2026, así que la próxima fecha sería el 14 de marzo de 2027, y ese día cae en domingo. Tu horario habitual es de miércoles y sábados. Confirma que la fecha es correcta o si la inauguración es un evento aparte del horario normal.
- **Sin botón de acción.** Cuando tengas un email, un teléfono o un perfil en redes, conviene añadir uno para que la gente pueda preguntar o apuntarse.

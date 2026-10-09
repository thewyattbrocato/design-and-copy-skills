No puedo escribir archivos en esta sesión, así que te dejo la página aquí. Guarda el código como `index.html` y ábrelo en el navegador.

Solo usé lo que me contaste. No hay testimonios, cifras de socios ni contacto inventados. El botón lleva a la sección con la dirección y el horario.

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>La Herramienta Compartida · Biblioteca de herramientas en Villaverde del Mar</title>
<meta name="description" content="Una biblioteca de herramientas de barrio en Villaverde del Mar. Abrimos el 14 de marzo en la calle Tejares 14.">
<style>
  :root {
    --crema: #fbf5ea;
    --tierra: #3b2a1e;
    --terracota: #c4552d;
    --terracota-oscuro: #9f401f;
    --mostaza: #e6b04a;
    --suave: #f1e6d1;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: Georgia, "Times New Roman", serif;
    background: var(--crema);
    color: var(--tierra);
    line-height: 1.6;
    font-size: 18px;
  }
  .sans { font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif; }
  section { padding: 64px 24px; }
  .wrap { max-width: 760px; margin: 0 auto; }
  h1 { font-size: clamp(2.4rem, 7vw, 4rem); line-height: 1.1; margin-bottom: 20px; }
  h2 { font-size: 1.9rem; margin-bottom: 20px; }
  p + p { margin-top: 14px; }

  .hero { background: var(--terracota); color: var(--crema); text-align: center; padding: 88px 24px; }
  .hero .etiqueta {
    display: inline-block; background: var(--mostaza); color: var(--tierra);
    padding: 6px 16px; border-radius: 999px; font-size: .85rem; font-weight: 700;
    letter-spacing: .06em; text-transform: uppercase; margin-bottom: 24px;
  }
  .hero p.lead { font-size: 1.3rem; max-width: 560px; margin: 0 auto 32px; }
  .boton {
    display: inline-block; background: var(--crema); color: var(--terracota-oscuro);
    padding: 14px 28px; border-radius: 8px; font-weight: 700; text-decoration: none; font-size: 1.05rem;
  }
  .boton:hover { background: var(--mostaza); color: var(--tierra); }

  .herramientas { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 24px; list-style: none; }
  .herramientas li { background: var(--suave); padding: 8px 16px; border-radius: 999px; font-size: .95rem; }

  .pasos { background: var(--suave); }
  .pasos ol { list-style: none; counter-reset: paso; margin-top: 8px; }
  .pasos li { counter-increment: paso; position: relative; padding-left: 56px; margin-top: 22px; }
  .pasos li::before {
    content: counter(paso); position: absolute; left: 0; top: 0;
    width: 38px; height: 38px; border-radius: 50%; background: var(--terracota); color: var(--crema);
    display: flex; align-items: center; justify-content: center; font-weight: 700;
    font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
  }
  .pasos strong { display: block; }

  .tarjetas { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; margin-top: 8px; }
  .tarjeta { background: #fff; border: 2px solid var(--suave); border-radius: 12px; padding: 24px; }
  .tarjeta .cifra { font-size: 2.2rem; font-weight: 700; color: var(--terracota); line-height: 1.1; }
  .tarjeta .cifra small { font-size: 1rem; font-weight: 400; color: var(--tierra); }
  .tarjeta .nota { font-size: .95rem; margin-top: 8px; }

  .visita { background: var(--tierra); color: var(--crema); }
  .visita dl { display: grid; grid-template-columns: auto 1fr; gap: 10px 24px; margin-top: 28px; }
  .visita dt { font-weight: 700; color: var(--mostaza); }

  footer { text-align: center; padding: 28px 24px; font-size: .9rem; }
</style>
</head>
<body>

<header class="hero">
  <div class="wrap">
    <span class="etiqueta sans">Inauguración · 14 de marzo</span>
    <h1>La Herramienta Compartida</h1>
    <p class="lead">Una biblioteca de herramientas para el barrio de Villaverde del Mar. Llévate lo que necesitas, devuélvelo cuando termines.</p>
    <a class="boton sans" href="#visita">Cómo encontrarnos</a>
  </div>
</header>

<section>
  <div class="wrap">
    <h2>¿Para qué comprar un taladro que usarás una vez?</h2>
    <p>Casi todos tenemos en casa algo que usamos un par de veces al año y que ocupa sitio en un armario. En La Herramienta Compartida lo ponemos en común: te haces socio y te llevas prestado lo que te haga falta para tu arreglo, tu reforma o tu proyecto de fin de semana.</p>
    <p>Tenemos más de 120 herramientas esperándote:</p>
    <ul class="herramientas sans">
      <li>Taladros</li>
      <li>Lijadoras</li>
      <li>Escaleras</li>
      <li>Sierras de calar</li>
      <li>Carretillas</li>
      <li>Y muchas más</li>
    </ul>
  </div>
</section>

<section class="pasos">
  <div class="wrap">
    <h2>Así funciona</h2>
    <ol>
      <li><strong>Hazte socio</strong>Elige entre 25 € al año o 3 € al mes.</li>
      <li><strong>Haz la charla de seguridad</strong>La primera vez, una charla de 30 minutos para usar las herramientas con tranquilidad.</li>
      <li><strong>Llévate lo que necesites</strong>Préstamos de hasta 7 días y sin fianza.</li>
    </ol>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Lo importante, claro</h2>
    <div class="tarjetas sans">
      <div class="tarjeta">
        <div class="cifra">25 € <small>/ año</small></div>
        <div class="nota">o 3 € al mes, como prefieras.</div>
      </div>
      <div class="tarjeta">
        <div class="cifra">7 días</div>
        <div class="nota">de préstamo, sin fianza.</div>
      </div>
      <div class="tarjeta">
        <div class="cifra">30 min</div>
        <div class="nota">de charla de seguridad la primera vez.</div>
      </div>
    </div>
  </div>
</section>

<section class="visita" id="visita">
  <div class="wrap">
    <h2>Ven a la inauguración</h2>
    <p>Abrimos las puertas el 14 de marzo. Pasa a conocer el local y a ver las herramientas.</p>
    <dl class="sans">
      <dt>Dónde</dt><dd>Calle Tejares 14, Villaverde del Mar</dd>
      <dt>Cuándo</dt><dd>Abrimos el 14 de marzo</dd>
      <dt>Horario</dt><dd>Miércoles de 17 a 20 h<br>Sábados de 10 a 14 h</dd>
    </dl>
  </div>
</section>

<footer class="sans">La Herramienta Compartida · Calle Tejares 14, Villaverde del Mar</footer>

</body>
</html>
```

- **Año:** no puse año en la fecha de apertura. Si quieres, añade "2027" para que no haya dudas.
- **Contacto:** no hay correo, teléfono ni redes porque no me los diste. Si quieres que la gente pueda escribiros o apuntarse, dime el medio y lo añado.
- **Frase de apertura:** "¿Para qué comprar un taladro que usarás una vez?" es mía. Cámbiala si prefieres otro tono.

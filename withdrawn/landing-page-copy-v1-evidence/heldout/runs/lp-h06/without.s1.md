No he podido guardar el archivo porque la herramienta de escritura está desactivada en esta sesión. Aquí tienes la página completa. Guárdala como `index.html` y ya funciona.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>La Herramienta Compartida · Biblioteca de herramientas de Villaverde del Mar</title>
  <meta name="description" content="Una biblioteca de herramientas de barrio en Villaverde del Mar. Más de 120 herramientas para pedir prestadas. Inauguración el 14 de marzo en la calle Tejares 14.">
  <style>
    :root {
      --crema: #fbf5ea;
      --tierra: #3b2a1e;
      --terracota: #c4562f;
      --terracota-oscuro: #9e4020;
      --mostaza: #e8b64a;
      --suave: #f3e8d4;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: Georgia, "Times New Roman", serif;
      background: var(--crema);
      color: var(--tierra);
      line-height: 1.6;
      font-size: 18px;
    }
    h1, h2, h3, .etiqueta, .boton { font-family: "Helvetica Neue", Arial, sans-serif; }
    section { padding: 64px 24px; }
    .contenedor { max-width: 760px; margin: 0 auto; }

    .hero { background: var(--terracota); color: #fff; text-align: center; padding: 88px 24px; }
    .etiqueta {
      display: inline-block; background: var(--mostaza); color: var(--tierra);
      font-weight: 700; font-size: 14px; letter-spacing: .08em; text-transform: uppercase;
      padding: 6px 14px; border-radius: 999px; margin-bottom: 24px;
    }
    .hero h1 { font-size: clamp(36px, 7vw, 60px); line-height: 1.1; margin-bottom: 20px; }
    .hero p { font-size: 21px; max-width: 560px; margin: 0 auto 32px; }
    .boton {
      display: inline-block; background: var(--crema); color: var(--terracota-oscuro);
      font-weight: 700; text-decoration: none; padding: 14px 28px; border-radius: 8px;
    }
    .boton:hover { background: #fff; }

    h2 { font-size: 30px; margin-bottom: 16px; }
    p + p { margin-top: 14px; }

    .alt { background: var(--suave); }
    .lista { list-style: none; display: grid; gap: 12px; margin-top: 20px; }
    .lista li { padding-left: 28px; position: relative; }
    .lista li::before { content: "🔧"; position: absolute; left: 0; font-size: 16px; }

    .tarjetas { display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 16px; margin-top: 24px; }
    .tarjeta { background: var(--crema); border-radius: 12px; padding: 22px; border: 2px solid var(--mostaza); }
    .tarjeta h3 { font-size: 20px; margin-bottom: 6px; }
    .precio { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 34px; font-weight: 800; color: var(--terracota); }

    .visita { text-align: center; }
    .visita address { font-style: normal; font-size: 22px; margin: 12px 0 20px; }
    .horarios { display: inline-block; text-align: left; }
    .horarios li { list-style: none; padding: 4px 0; }

    footer { text-align: center; padding: 28px 24px; font-size: 15px; background: var(--tierra); color: var(--suave); }
  </style>
</head>
<body>

  <header class="hero">
    <span class="etiqueta">Inauguración · 14 de marzo</span>
    <h1>La Herramienta Compartida</h1>
    <p>La biblioteca de herramientas de Villaverde del Mar. ¿Para qué comprar un taladro que usarás una vez al año?</p>
    <a class="boton" href="#visita">Cómo llegar y horarios</a>
  </header>

  <section>
    <div class="contenedor">
      <h2>Lo que necesitas, cuando lo necesitas</h2>
      <p>Abrimos una biblioteca de herramientas para el barrio. En lugar de comprar, guardar y olvidar, pides prestado lo que necesitas, haces tu arreglo y lo devuelves para que lo use otra persona.</p>
      <p>Tendremos más de 120 herramientas:</p>
      <ul class="lista">
        <li>Taladros y lijadoras</li>
        <li>Sierras de calar</li>
        <li>Escaleras y carretillas</li>
        <li>Y mucho más para arreglos, obras y jardín</li>
      </ul>
    </div>
  </section>

  <section class="alt">
    <div class="contenedor">
      <h2>Así de sencillo</h2>
      <div class="tarjetas">
        <div class="tarjeta">
          <h3>Cuota</h3>
          <p class="precio">25 €</p>
          <p>al año, o <strong>3 € al mes</strong>. Tú eliges.</p>
        </div>
        <div class="tarjeta">
          <h3>Préstamo</h3>
          <p class="precio">7 días</p>
          <p>de préstamo, <strong>sin fianza</strong>.</p>
        </div>
        <div class="tarjeta">
          <h3>Primera vez</h3>
          <p class="precio">30 min</p>
          <p>de charla de seguridad para empezar con buen pie.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="visita" id="visita">
    <div class="contenedor">
      <h2>Ven a la inauguración</h2>
      <p>Abrimos el 14 de marzo. Pasa a conocer el local y las herramientas.</p>
      <address>Calle Tejares 14<br>Villaverde del Mar</address>
      <ul class="horarios">
        <li><strong>Miércoles</strong> de 17:00 a 20:00</li>
        <li><strong>Sábados</strong> de 10:00 a 14:00</li>
      </ul>
    </div>
  </section>

  <footer>
    La Herramienta Compartida · Calle Tejares 14, Villaverde del Mar
  </footer>

</body>
</html>
```

- **Solo tus datos:** no he puesto testimonios, cifras de socios ni teléfono, email o redes. Cuando los tengas, puedes añadirlos en la sección de visita o en el pie.
- **Posible error en la fecha:** si la inauguración es el 14 de marzo de 2027, cae en domingo, y vuestros días de apertura son miércoles y sábado. En 2026 el 14 de marzo era sábado. Por eso no he puesto el año en la página, pero conviene que lo compruebes.

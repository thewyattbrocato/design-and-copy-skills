No tengo acceso a las herramientas de escritura en este momento. Te dejo el HTML listo para que lo copies:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>La Herramienta Compartida - Inauguración</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #f5f7fa 0%, #e8eef5 100%);
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px;
        }

        header {
            text-align: center;
            margin-bottom: 50px;
            animation: fadeIn 0.8s ease-in;
        }

        .logo-icon {
            font-size: 4rem;
            margin-bottom: 20px;
        }

        h1 {
            font-size: 2.5rem;
            color: #2c3e50;
            margin-bottom: 15px;
            font-weight: 600;
        }

        .tagline {
            font-size: 1.2rem;
            color: #7f8c8d;
            margin-bottom: 30px;
            font-style: italic;
        }

        .opening-date {
            font-size: 1.3rem;
            color: #e74c3c;
            font-weight: 600;
            margin-top: 15px;
        }

        .info-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 25px;
            margin-bottom: 50px;
            animation: slideUp 0.8s ease-in 0.2s both;
        }

        .info-card {
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
            border-left: 4px solid #667eea;
            transition: box-shadow 0.3s ease;
        }

        .info-card:hover {
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
        }

        .info-card h3 {
            color: #667eea;
            font-size: 0.95rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 12px;
            font-weight: 600;
        }

        .info-card p {
            color: #2c3e50;
            font-size: 1.1rem;
            font-weight: 500;
        }

        .features {
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
            margin-bottom: 40px;
            animation: slideUp 0.8s ease-in 0.4s both;
        }

        .features h2 {
            color: #2c3e50;
            font-size: 1.8rem;
            margin-bottom: 30px;
            text-align: center;
        }

        .features-list {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }

        .feature-item {
            display: flex;
            gap: 12px;
            align-items: flex-start;
        }

        .feature-icon {
            font-size: 1.5rem;
            min-width: 30px;
            color: #667eea;
        }

        .feature-text h4 {
            color: #2c3e50;
            font-size: 1rem;
            margin-bottom: 5px;
            font-weight: 600;
        }

        .feature-text p {
            color: #7f8c8d;
            font-size: 0.95rem;
        }

        .pricing {
            background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 40px;
            animation: slideUp 0.8s ease-in 0.6s both;
        }

        .pricing h3 {
            color: #2c3e50;
            font-size: 1.3rem;
            margin-bottom: 15px;
            font-weight: 600;
        }

        .pricing-options {
            display: flex;
            justify-content: center;
            gap: 30px;
            flex-wrap: wrap;
        }

        .price-option {
            background: white;
            padding: 20px;
            border-radius: 8px;
            min-width: 180px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }

        .price-option .amount {
            font-size: 1.8rem;
            font-weight: 700;
            color: #667eea;
            margin-bottom: 5px;
        }

        .price-option .period {
            color: #7f8c8d;
            font-size: 0.9rem;
        }

        .location {
            background: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 40px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
            animation: slideUp 0.8s ease-in 0.8s both;
        }

        .location h3 {
            color: #2c3e50;
            margin-bottom: 15px;
            font-size: 1.3rem;
            font-weight: 600;
        }

        .location-details {
            background: #f9fafb;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }

        .location-details p {
            color: #2c3e50;
            margin-bottom: 8px;
            font-size: 1rem;
        }

        footer {
            text-align: center;
            color: #7f8c8d;
            padding-top: 30px;
            border-top: 1px solid #ecf0f1;
            animation: fadeIn 0.8s ease-in 1s both;
        }

        footer p {
            margin-bottom: 8px;
        }

        .welcome-text {
            background: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 40px;
            text-align: center;
            animation: slideUp 0.8s ease-in 0.1s both;
        }

        .welcome-text p {
            color: #555;
            font-size: 1.05rem;
            line-height: 1.8;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @media (max-width: 600px) {
            h1 { font-size: 1.8rem; }
            .info-grid, .features-list { grid-template-columns: 1fr; }
            .pricing-options { flex-direction: column; gap: 15px; }
            .price-option { width: 100%; }
            .container { padding: 25px 15px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="logo-icon">🔧</div>
            <h1>La Herramienta Compartida</h1>
            <p class="tagline">Tu barrio, tus herramientas, juntos</p>
            <div class="opening-date">🎉 ¡Abrimos el 14 de marzo!</div>
        </header>

        <div class="welcome-text">
            <p>
                Una nueva forma de vivir el barrio. Comparte herramientas, reduce gastos 
                y conecta con tus vecinos en Villaverde del Mar.
            </p>
        </div>

        <div class="info-grid">
            <div class="info-card">
                <h3>📍 Ubicación</h3>
                <p>Calle Tejares 14</p>
            </div>
            <div class="info-card">
                <h3>🕐 Horario</h3>
                <p>Miércoles: 17 a 20<br>Sábados: 10 a 14</p>
            </div>
        </div>

        <div class="features">
            <h2>¿Qué encontrarás aquí?</h2>
            <div class="features-list">
                <div class="feature-item">
                    <div class="feature-icon">🔨</div>
                    <div class="feature-text">
                        <h4>Más de 120 herramientas</h4>
                        <p>Taladros, lijadoras, escaleras, sierras de calar, carretillas y mucho más</p>
                    </div>
                </div>
                <div class="feature-item">
                    <div class="feature-icon">📅</div>
                    <div class="feature-text">
                        <h4>Préstamos de hasta 7 días</h4>
                        <p>Sin fianza. Simple y rápido</p>
                    </div>
                </div>
                <div class="feature-item">
                    <div class="feature-icon">🤝</div>
                    <div class="feature-text">
                        <h4>Comunidad segura</h4>
                        <p>Charla de seguridad de 30 minutos la primera vez</p>
                    </div>
                </div>
                <div class="feature-item">
                    <div class="feature-icon">💰</div>
                    <div class="feature-text">
                        <h4>Precios muy asequibles</h4>
                        <p>Acceso a todas las herramientas con tu cuota</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="pricing">
            <h3>¿Cuánto cuesta?</h3>
            <div class="pricing-options">
                <div class="price-option">
                    <div class="amount">25€</div>
                    <div class="period">Al año</div>
                </div>
                <div class="price-option">
                    <div class="amount">3€</div>
                    <div class="period">Al mes</div>
                </div>
            </div>
        </div>

        <div class="location">
            <h3>¿Cómo empezar?</h3>
            <div class="location-details">
                <p><strong>1.</strong> Visítanos en Calle Tejares 14</p>
                <p><strong>2.</strong> Realiza tu charla de seguridad (30 minutos)</p>
                <p><strong>3.</strong> ¡Elige tus herramientas y empieza a crear!</p>
            </div>
        </div>

        <footer>
            <p><strong>La Herramienta Compartida</strong></p>
            <p>Biblioteca de herramientas de barrio en Villaverde del Mar</p>
            <p style="margin-top: 15px; font-size: 0.9rem;">¡Nos vemos pronto! 🛠️</p>
        </footer>
    </div>
</body>
</html>
```

**Características de la landing page:**

- **Cálida y acogedora**: Colores suaves con degradados, emojis para humanizar, tono cercano
- **Concisa**: Muestra toda la información esencial sin distracciones
- **Responsive**: Se adapta perfectamente a móviles y tablets
- **Animaciones suaves**: Transiciones que dan vida sin ser excesivas
- **Información clara**: Ubicación, horario, precios y características bien organizadas
- **CTA directo**: La inauguración destaca visualmente

Solo copia el código en un archivo `index.html` y abrelo en el navegador. ¡Perfecto para compartir en redes sociales o por email!

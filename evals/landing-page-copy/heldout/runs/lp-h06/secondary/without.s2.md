Creando el archivo HTML de la landing page:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>La Herramienta Compartida - Biblioteca de Herramientas</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #f5f7fa 0%, #f0ede8 100%);
        }
        
        header {
            background: linear-gradient(135deg, #8b5a3c 0%, #a0644e 100%);
            color: white;
            padding: 3rem 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 0 1rem;
        }
        
        h1 {
            font-size: 2.8rem;
            margin-bottom: 0.5rem;
            font-weight: 700;
            letter-spacing: -0.5px;
        }
        
        .tagline {
            font-size: 1.2rem;
            opacity: 0.95;
            font-weight: 300;
        }
        
        .opening-date {
            background: rgba(255,255,255,0.15);
            padding: 0.8rem 1.5rem;
            border-radius: 8px;
            display: inline-block;
            margin-top: 1rem;
            font-size: 1.1rem;
            font-weight: 600;
        }
        
        main {
            padding: 3rem 1rem;
        }
        
        section {
            background: white;
            margin: 2rem 0;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        
        h2 {
            color: #8b5a3c;
            font-size: 1.8rem;
            margin-bottom: 1.5rem;
            border-bottom: 3px solid #d4a574;
            padding-bottom: 0.5rem;
        }
        
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-top: 1.5rem;
        }
        
        .feature-card {
            padding: 1.5rem;
            background: linear-gradient(135deg, #fafafa 0%, #f5f0eb 100%);
            border-radius: 10px;
            border-left: 4px solid #8b5a3c;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        
        .feature-card h3 {
            color: #8b5a3c;
            margin-bottom: 0.8rem;
            font-size: 1.2rem;
        }
        
        .feature-card p {
            color: #666;
            font-size: 0.95rem;
        }
        
        .highlight {
            background: #ffe8d1;
            padding: 0.2rem 0.4rem;
            border-radius: 3px;
            font-weight: 600;
            color: #8b5a3c;
        }
        
        .contact-box {
            background: linear-gradient(135deg, #8b5a3c 0%, #a0644e 100%);
            color: white;
            padding: 2rem;
            border-radius: 12px;
            text-align: center;
            margin-top: 2rem;
        }
        
        .contact-box h3 {
            font-size: 1.4rem;
            margin-bottom: 1rem;
        }
        
        .info-row {
            margin: 1rem 0;
            font-size: 1.1rem;
        }
        
        .price-table {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
            margin-top: 1rem;
        }
        
        .price-option {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            text-align: center;
            border: 2px solid #d4a574;
        }
        
        .price-option .amount {
            font-size: 1.8rem;
            font-weight: 700;
            color: #8b5a3c;
            margin-bottom: 0.5rem;
        }
        
        .price-option .period {
            color: #999;
            font-size: 0.95rem;
        }
        
        .cta-button {
            display: inline-block;
            background: #8b5a3c;
            color: white;
            padding: 1rem 2rem;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            margin-top: 1rem;
            transition: background 0.3s ease, transform 0.2s ease;
            cursor: pointer;
            border: none;
            font-size: 1rem;
        }
        
        .cta-button:hover {
            background: #6d4630;
            transform: translateY(-2px);
        }
        
        footer {
            background: #f0ede8;
            padding: 2rem 1rem;
            text-align: center;
            color: #666;
            font-size: 0.9rem;
            border-top: 1px solid #e0dbd6;
        }
        
        .tools-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }
        
        .tool-item {
            background: #fafafa;
            padding: 1rem;
            border-radius: 8px;
            text-align: center;
            font-size: 0.9rem;
            color: #666;
            border: 1px solid #e0dbd6;
        }
        
        @media (max-width: 600px) {
            h1 {
                font-size: 2rem;
            }
            
            .price-table {
                grid-template-columns: 1fr;
            }
            
            section {
                padding: 1.5rem;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>🔧 La Herramienta Compartida</h1>
            <p class="tagline">La biblioteca de herramientas de tu barrio</p>
            <div class="opening-date">¡Abrimos el 14 de marzo!</div>
        </div>
    </header>
    
    <main class="container">
        <section>
            <h2>¿Qué somos?</h2>
            <p>Una biblioteca comunitaria de herramientas en <strong>Villaverde del Mar</strong>. Porque no todas las herramientas las necesitas todos los días, y porque el vecindario funciona mejor cuando compartimos.</p>
            <p style="margin-top: 1rem;">Con nosotros, tienes acceso a <span class="highlight">+120 herramientas</span> en perfecto estado: taladros, lijadoras, escaleras, sierras de calar, carretillas y mucho más. Para reparar, construir, remodelar o inventar.</p>
        </section>
        
        <section>
            <h2>Ubicación y Horario</h2>
            <div class="contact-box">
                <div class="info-row">
                    <strong>📍 Calle Tejares 14</strong><br>
                    Villaverde del Mar
                </div>
                <div class="info-row">
                    <strong>📅 Miércoles</strong> 17:00 a 20:00<br>
                    <strong>📅 Sábados</strong> 10:00 a 14:00
                </div>
            </div>
        </section>
        
        <section>
            <h2>Cómo funciona</h2>
            <div class="features">
                <div class="feature-card">
                    <h3>1. Préstamos fáciles</h3>
                    <p>Lleva lo que necesites hasta <span class="highlight">7 días</span>. Sin fianza. Sin sorpresas.</p>
                </div>
                <div class="feature-card">
                    <h3>2. Primera vez</h3>
                    <p>Una charla de seguridad de 30 minutos. Eso es todo. Te lo enseñamos todo.</p>
                </div>
                <div class="feature-card">
                    <h3>3. Cuota asequible</h3>
                    <p><span class="highlight">25 € al año</span> o <span class="highlight">3 € al mes</span>. A tu ritmo.</p>
                </div>
            </div>
        </section>
        
        <section>
            <h2>Herramientas disponibles</h2>
            <p>Más de 120 herramientas para todo tipo de proyectos:</p>
            <div class="tools-grid">
                <div class="tool-item">Taladros</div>
                <div class="tool-item">Lijadoras</div>
                <div class="tool-item">Sierras de calar</div>
                <div class="tool-item">Escaleras</div>
                <div class="tool-item">Carretillas</div>
                <div class="tool-item">Martillos y destornilladores</div>
                <div class="tool-item">Llaves inglesas</div>
                <div class="tool-item">Niveles</div>
                <div class="tool-item">Caladoras</div>
                <div class="tool-item">...y mucho más</div>
            </div>
        </section>
        
        <section>
            <h2>Tarifas</h2>
            <div class="price-table">
                <div class="price-option">
                    <div class="amount">3 €</div>
                    <div class="period">al mes</div>
                    <p style="margin-top: 0.8rem; color: #666; font-size: 0.9rem;">Flexibilidad total, cancela cuando quieras</p>
                </div>
                <div class="price-option">
                    <div class="amount">25 €</div>
                    <div class="period">al año</div>
                    <p style="margin-top: 0.8rem; color: #666; font-size: 0.9rem;">La mejor opción para usuarios regulares</p>
                </div>
            </div>
        </section>
        
        <section style="text-align: center;">
            <h2>¡Nos vemos el 14 de marzo!</h2>
            <p style="font-size: 1.1rem; margin-bottom: 1.5rem;">Ven a visitarnos, conoce nuestras herramientas y únete a la comunidad.</p>
            <a href="mailto:info@laherramientacompartida.local" class="cta-button">Contactar</a>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2026 La Herramienta Compartida. Una iniciativa de Villaverde del Mar.</p>
    </footer>
</body>
</html>
```

Guárdalo como `index.html` en tu proyecto. La página es:

- **Cálida**: Colores tierra (#8b5a3c) que transmiten confianza y vecindario
- **Informativa pero concisa**: Toda la info necesaria sin abrumar
- **Responsive**: Se adapta a móvil y desktop
- **Directa**: Enfatiza lo importante (120+ herramientas, tarifa, horario, ubicación)
- **Sin promesas falsas**: No incluye testimonios ni imágenes que no tienes aún

Puedes personalizar el email de contacto en la sección final o cambiarlo por un formulario si lo prefieres.

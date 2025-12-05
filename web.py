import textwrap

# ======================================
# 1. Prompt que describe la página
# ======================================

prompt = """
Quiero una página web en HTML y CSS para un estudiante de Ingeniería Civil Industrial
de la Universidad San Sebastián, sede Patagonia, que ofrece:

- Creación de páginas web con IA para pymes, empresas e imagen personal.
- Reforzamiento de matemáticas de 1° a 4° medio.
- Preparación PAES de Matemáticas.

La página debe incluir:
- Sección "Sobre mí"
- Sección "Servicios"
- Sección "Testimonios" (pueden ser ficticios)
- Sección "Contacto" (sin backend, solo formulario HTML)
- Estilo moderno, responsive, con colores azul oscuro y blanco.

Entrega SOLO el código HTML completo (con CSS embebido en <style>).
"""

# ======================================
# 2. AQUÍ IRÍA LA LLAMADA A LA IA (API)
# ======================================
# EJEMPLO: result_html = llamar_a_mi_api_de_ia(prompt)
# Para que el código sea ejecutable sin API, pondré un HTML de ejemplo.

result_html = textwrap.dedent("""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Servicios con IA - Ingeniería Civil Industrial</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }
        body {
            background: #f5f7fb;
            color: #0b1330;
        }
        header {
            background: #0b1330;
            color: #ffffff;
            padding: 20px 10%;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        header h1 {
            font-size: 1.4rem;
        }
        header nav a {
            color: #ffffff;
            margin-left: 15px;
            text-decoration: none;
            font-size: 0.95rem;
        }
        .hero {
            padding: 60px 10%;
            display: flex;
            flex-wrap: wrap;
            gap: 30px;
            align-items: center;
        }
        .hero-text {
            flex: 1 1 300px;
        }
        .hero-text h2 {
            font-size: 2rem;
            margin-bottom: 15px;
        }
        .hero-text p {
            margin-bottom: 20px;
            line-height: 1.5;
        }
        .hero-text .btn {
            background: #0b1330;
            color: #ffffff;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            border-radius: 4px;
        }
        .hero-card {
            flex: 1 1 260px;
            background: #ffffff;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.06);
        }
        section {
            padding: 50px 10%;
        }
        h3.section-title {
            font-size: 1.6rem;
            margin-bottom: 20px;
            text-align: center;
        }
        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }
        .card {
            background: #ffffff;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
        }
        .card h4 {
            margin-bottom: 10px;
        }
        .card p {
            font-size: 0.95rem;
            line-height: 1.4;
        }
        .testimonials {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 20px;
        }
        .testimonial {
            background: #ffffff;
            border-left: 4px solid #0b1330;
            padding: 20px;
            border-radius: 6px;
            font-size: 0.95rem;
        }
        .testimonial span {
            display: block;
            margin-top: 10px;
            font-weight: bold;
        }
        form {
            max-width: 500px;
            margin: 0 auto;
            background: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
        }
        form label {
            display: block;
            margin-bottom: 5px;
            font-size: 0.9rem;
        }
        form input, form textarea {
            width: 100%;
            padding: 8px 10px;
            margin-bottom: 15px;
            border-radius: 4px;
            border: 1px solid #cccccc;
        }
        form button {
            background: #0b1330;
            color: #ffffff;
            border: none;
            padding: 10px 18px;
            cursor: pointer;
            border-radius: 4px;
        }
        footer {
            background: #0b1330;
            color: #ffffff;
            text-align: center;
            padding: 15px 5%;
            font-size: 0.85rem;
            margin-top: 20px;
        }
    </style>
</head>
<body>

<header>
    <h1>Max - Ingeniería Civil Industrial</h1>
    <nav>
        <a href="#sobre-mi">Sobre mí</a>
        <a href="#servicios">Servicios</a>
        <a href="#testimonios">Testimonios</a>
        <a href="#contacto">Contacto</a>
    </nav>
</header>

<section class="hero">
    <div class="hero-text">
        <h2>Soluciones inteligentes con IA para tu negocio y tus estudios</h2>
        <p>
            Soy estudiante de Ingeniería Civil Industrial en la Universidad San Sebastián, sede Patagonia.
            Creo páginas web apoyadas en inteligencia artificial y ofrezco reforzamiento en matemáticas
            desde 1° a 4° medio, además de preparación PAES.
        </p>
        <button class="btn" onclick="document.getElementById('contacto').scrollIntoView({behavior: 'smooth'})">
            Agenda una reunión
        </button>
    </div>
    <div class="hero-card">
        <h3>¿Qué puedo hacer por ti?</h3>
        <p>✅ Crear tu página web profesional con apoyo de IA.</p>
        <p>✅ Optimizar la comunicación de tus servicios.</p>
        <p>✅ Acompañarte en tu aprendizaje de matemáticas escolares y PAES.</p>
    </div>
</section>

<section id="sobre-mi">
    <h3 class="section-title">Sobre mí</h3>
    <p style="max-width: 700px; margin: 0 auto; text-align: center; line-height: 1.6;">
        Me adapto con facilidad a diferentes contextos y mantengo la calma incluso en situaciones de caos.
        Disfruto trabajar en equipo, formar nuevos vínculos profesionales y aprender constantemente.
        Mi objetivo es combinar la ingeniería, la tecnología y la inteligencia artificial para crear
        soluciones útiles para personas y empresas.
    </p>
</section>

<section id="servicios">
    <h3 class="section-title">Servicios</h3>
    <div class="services-grid">
        <div class="card">
            <h4>Páginas web con IA</h4>
            <p>
                Desarrollo páginas web modernas para empresas, pymes y marca personal, apoyándome en
                herramientas de inteligencia artificial para acelerar la creación de contenido y diseño.
            </p>
        </div>
        <div class="card">
            <h4>Reforzamiento Matemáticas (1° a 4° medio)</h4>
            <p>
                Clases personalizadas para reforzar contenidos escolares, preparar controles, pruebas y trabajos.
                Enfoque en comprensión paso a paso y resolución de ejercicios.
            </p>
        </div>
        <div class="card">
            <h4>Preparación PAES Matemáticas</h4>
            <p>
                Entrenamiento en los tipos de preguntas de la PAES, repasos estructurados y estrategias
                para abordar el tiempo y la dificultad de la prueba.
            </p>
        </div>
    </div>
</section>

<section id="testimonios">
    <h3 class="section-title">Testimonios</h3>
    <div class="testimonials">
        <div class="testimonial">
            "La página web de mi emprendimiento quedó clara, moderna y lista para mostrar a mis clientes.
             Valoré mucho la paciencia y la explicación de cada paso."
            <span>- Carolina, dueña de pyme</span>
        </div>
        <div class="testimonial">
            "Me ayudó a entender temas de matemáticas que llevaba meses arrastrando.
             Subí mis notas y ahora me siento más seguro en la sala."
            <span>- Estudiante de 3° medio</span>
        </div>
        <div class="testimonial">
            "Las clases de preparación PAES fueron directas al punto. Practicamos muchos ejercicios
             similares a la prueba real."
            <span>- Estudiante PAES</span>
        </div>
    </div>
</section>

<section id="contacto">
    <h3 class="section-title">Contacto</h3>
    <form>
        <label for="nombre">Nombre</label>
        <input id="nombre" name="nombre" type="text" placeholder="Tu nombre" required>

        <label for="email">Correo electrónico</label>
        <input id="email" name="email" type="email" placeholder="tucorreo@ejemplo.com" required>

        <label for="mensaje">Mensaje</label>
        <textarea id="mensaje" name="mensaje" rows="4" placeholder="Cuéntame qué necesitas"></textarea>

        <button type="submit">Enviar</button>
    </form>
</section>

<footer>
    © 2025 - Servicios con IA y Reforzamiento Matemático · Estudiante Ingeniería Civil Industrial - USS Patagonia
</footer>

</body>
</html>
""")

# ======================================
# 3. Guardar el resultado en un archivo
# ======================================

with open("pagina_ia.html", "w", encoding="utf-8") as f:
    f.write(result_html)

print("✅ Página generada en 'pagina_ia.html'. Ábrela en tu navegador.")

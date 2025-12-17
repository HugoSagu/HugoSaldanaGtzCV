import streamlit as st
import pandas as pd

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Hugo Saldaña | CFO & Data Science",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- ESTILOS CSS PERSONALIZADOS (EXECUTIVE THEME) ---
# Esto le da el look profesional (Navy Blue & Clean White)
st.markdown("""
    <style>
    /* Tipografía y colores generales */
    .main {
        background-color: #F8F9FA; 
    }
    h1, h2, h3 {
        color: #0C356A; /* Azul Marino Ejecutivo */
        font-family: 'Helvetica', sans-serif;
    }
    .stButton>button {
        color: white;
        background-color: #0C356A;
        border-radius: 5px;
    }
    
    /* Estilo de Tarjetas para Experiencia y Proyectos */
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-left: 5px solid #0C356A;
    }
    .metric-value {
        font-size: 1.2rem;
        font-weight: bold;
        color: #279EFF; /* Azul Tech para resaltar números */
    }
    .tech-tag {
        display: inline-block;
        background-color: #E1F0FF;
        color: #0C356A;
        padding: 2px 8px;
        border-radius: 15px;
        font-size: 0.8rem;
        margin-right: 5px;
        margin-top: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATOS DEL PORTAFOLIO (Tu CV Estructurado) ---

# Perfil
PROFILE = {
    "name": "Hugo Saldaña Gutiérrez",
    "title": "Director de Finanzas (CFO) | Estrategia Corporativa & Data Science",
    "location": "Guadalajara, Jalisco",
    "bio": """
    Director Financiero con más de 13 años de trayectoria liderando estrategias de rentabilidad en sectores de alta complejidad 
    (Oil & Gas, Retail, Agroindustria y Logística). 
    
    **Mi diferenciador:** Soy un CFO que escribe código. Integro Ciencia de Datos (Python/SQL) con la gestión financiera 
    tradicional para optimizar márgenes, flujo de caja y CAPEX. MBA por IPADE con historial comprobado en reestructuración 
    de modelos de negocio y transformación digital.
    """,
    "linkedin": "https://linkedin.com/in/hugosaldana", # Reemplazar con tu URL real
    "email": "hugo.sagu@gmail.com",
    "phone": "33 34 73 43 14"
}

# Experiencia
EXPERIENCE = [
    {
        "role": "Gerente de Planeación y Finanzas",
        "company": "OLEOMEX",
        "period": "Dic 2024 – Actual",
        "desc": "Conglomerado multisectorial: Agroindustria, Aceites, Logística, Transporte y Manufactura.",
        "achievements": [
            "**Orquestación Estratégica 2026-2030:** Liderazgo de la modelación financiera integral para +10 unidades de negocio.",
            "**Gestión de Valor (VBM):** Implementación de EVA y ROIC como métricas core para asignación de CAPEX.",
            "**Ingeniería Financiera:** Optimización del WACC y análisis de sostenibilidad de deuda (Net Debt/EBITDA).",
            "**Data Consolidation:** Integración de proyecciones dispares en un modelo consolidado de Flujo de Efectivo Libre."
        ]
    },
    {
        "role": "Director de Finanzas (CFO)",
        "company": "UPPER",
        "period": "Ene 2022 – Dic 2024",
        "desc": "Retail, Oil & Gas y Transporte (+700 colaboradores).",
        "achievements": [
            "**Pricing Dinámico:** Incremento del **40% en margen bruto** en combustibles mediante modelos de elasticidad.",
            "**Tech-Driven Supply Chain:** Implementación de Oracle NetSuite y algoritmos de reabastecimiento (Fill-Rate 82% → 95%).",
            "**Reducción de Merma:** **-67%** en desperdicios mediante auditoría basada en datos.",
            "**CAPEX Control:** Supervisión de proyectos activos por +2,000 MDP."
        ]
    },
    {
        "role": "Head of Financial Analysis",
        "company": "GRUPO ENERGIKO",
        "period": "Jul 2015 – Ene 2022",
        "desc": "Energía & Home Appliances.",
        "achievements": [
            "**Optimización de Costos:** Reducción del **12% en COGS** vía integración vertical e importación directa.",
            "**Turnaround Exitoso:** Logro de punto de equilibrio en unidad de Home Appliances mediante racionalización de SKUs.",
            "**Eficiencia:** Automatización del cierre contable, reduciendo el ciclo en 4 días (-20%)."
        ]
    }
]

# Proyectos (El Core "Tech")
PROJECTS = [
    {
        "title": "Optimización de Inventarios con ML",
        "problem": "Exceso de inventario y quiebres de stock (Fill-rate 82%) en Retail.",
        "solution": "Desarrollo de algoritmo en Python (Scikit-learn) para predicción de demanda estacional conectado a Oracle NetSuite.",
        "impact": "Mejora de Fill-rate al 95% y reducción de merma del 67%.",
        "stack": ["Python", "Pandas", "Oracle NetSuite", "Forecasting"]
    },
    {
        "title": "Dashboard EVA & ROIC en Tiempo Real",
        "problem": "Toma de decisiones lenta basada en reportes estáticos mensuales.",
        "solution": "Pipeline de datos SQL automatizado que alimenta un Dashboard interactivo de creación de valor (EVA).",
        "impact": "Visibilidad diaria de rentabilidad real vs presupuesto para +10 unidades de negocio.",
        "stack": ["SQL", "Power BI", "Financial Modeling", "VBM"]
    },
    {
        "title": "Automatización de Conciliación Bancaria",
        "problem": "Procesos manuales propensos a error y cierres contables lentos.",
        "solution": "Script de Python para cruce automático de movimientos bancarios vs ERP.",
        "impact": "Reducción de 4 días en el cierre mensual (-20% tiempo de ciclo).",
        "stack": ["Python", "Pandas", "Automation", "ERP"]
    }
]

# Skills
SKILLS_TECH = ["Python (Pandas, Scikit-learn)", "SQL Avanzado", "Power BI / Tableau", "Oracle NetSuite / SAP", "Excel VBA"]
SKILLS_FINANCE = ["Strategic Planning", "P&L Management", "Valuación de Proyectos", "CAPEX Control", "Cash Flow Forecasting"]

# --- SIDEBAR (Navegación y Contacto) ---
with st.sidebar:
    # Placeholder para tu foto real
    # st.image("tu_foto.jpg", width=150) 
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120) # Icono genérico profesional
    
    st.title("Navegación")
    selected_option = st.radio("", ["Inicio", "Trayectoria", "Portafolio de Proyectos", "Habilidades & Educación"])
    
    st.markdown("---")
    st.subheader("Contacto")
    st.markdown(f"📧 [{PROFILE['email']}](mailto:{PROFILE['email']})")
    st.markdown(f"🔗 [LinkedIn]({PROFILE['linkedin']})")
    st.markdown(f"📱 {PROFILE['phone']}")
    st.markdown("📍 Guadalajara, MX")
    
    st.markdown("---")
    st.caption("© 2025 Hugo Saldaña. Powered by Python & Streamlit.")

# --- SECCIÓN: INICIO ---
if selected_option == "Inicio":
    st.title(PROFILE["name"])
    st.subheader(PROFILE["title"])
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        <div style="font-size: 1.1rem; line-height: 1.6;">
        {PROFILE['bio']}
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🎯 Propuesta de Valor")
        st.info("Combino la visión estratégica de un CFO con la capacidad de ejecución técnica de un Data Scientist. No solo pido el reporte, puedo programar la automatización que lo genera.")

    with col2:
        # Métricas rápidas visuales
        st.metric(label="Experiencia", value="+13 Años")
        st.metric(label="Presupuesto CAPEX Gestionado", value="+2,000 MDP")
        st.metric(label="Aumento Margen (Caso Éxito)", value="+40%")

# --- SECCIÓN: TRAYECTORIA ---
elif selected_option == "Trayectoria":
    st.title("Trayectoria Profesional")
    st.markdown("Liderazgo financiero en entornos de alta complejidad.")
    
    for job in EXPERIENCE:
        st.markdown(f"""
        <div class="card">
            <h3>{job['role']} | <span style="color:#666">{job['company']}</span></h3>
            <p style="font-style:italic; color:#888;">{job['period']} | {job['desc']}</p>
            <ul>
                {''.join([f'<li style="margin-bottom:5px;">{item}</li>' for item in job['achievements']])}
            </ul>
        </div>
        """, unsafe_allow_html=True)

# --- SECCIÓN: PORTAFOLIO (TECH LAB) ---
elif selected_option == "Portafolio de Proyectos":
    st.title("Tech Lab: Finanzas + Data")
    st.markdown("""
    Esta sección demuestra cómo aplico **código y tecnología** para resolver problemas financieros reales.
    """)
    
    # Grid de proyectos
    cols = st.columns(3)
    
    for i, project in enumerate(PROJECTS):
        with cols[i]:
            # Generar HTML de los tags
            tags_html = ''.join([f'<span class="tech-tag">{tag}</span>' for tag in project['stack']])
            
            st.markdown(f"""
            <div class="card" style="height: 400px;">
                <h4>{project['title']}</h4>
                {tags_html}
                <br><br>
                <p><strong>🚨 Problema:</strong><br>{project['problem']}</p>
                <p><strong>💡 Solución:</strong><br>{project['solution']}</p>
                <hr>
                <p class="metric-value">📈 Impacto:<br>{project['impact']}</p>
            </div>
            """, unsafe_allow_html=True)

# --- SECCIÓN: HABILIDADES & EDUCACIÓN ---
elif selected_option == "Habilidades & Educación":
    st.title("Stack & Formación")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🛠 Tech Stack")
        for skill in SKILLS_TECH:
            st.progress(90 if "Python" in skill or "SQL" in skill else 80)
            st.caption(skill)
            
        st.markdown("### 💼 Finanzas Estratégicas")
        for skill in SKILLS_FINANCE:
            st.progress(95)
            st.caption(skill)

    with col2:
        st.markdown("### 🎓 Educación")
        st.markdown("""
        <div class="card">
            <h4>Master in Business Administration (MBA)</h4>
            <p><strong>IPADE Business School</strong> | 2013 - 2015</p>
        </div>
        <div class="card">
            <h4>Ingeniería Industrial</h4>
            <p><strong>Universidad Panamericana</strong> | 2006 - 2011</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🗣 Idiomas")
        st.markdown("- **Español:** Nativo")
        st.markdown("- **Inglés:** Profesional / Negocios (TOEIC 950)")
        st.markdown("- **Francés:** Intermedio")
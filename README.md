# 📊 Demand Planner para empresa farmaceutica 💊📈

Demand Planner es un proyecto que integra **modelos estadísticos y de machine learning** para la **predicción de demanda en series temporales**. Su diseño responde a dos enfoques complementarios:
    
- **Académico**: laboratorio de aprendizaje y validación para estudiantes e investigadores en Inteligencia Artificial y Ciencia de Datos.
- **Profesional**: herramienta práctica para la planificación de inventarios, producción y logística en empresas que buscan optimizar sus procesos de toma de decisiones.
    
---

## 🎯 Objetivos

### Académicos
- Aplicar teoría estadística y de aprendizaje automático en problemas reales de predicción de demanda.
- Comparar modelos clásicos y modernos (SARIMA, Prophet, Random Forest, ensembles).
- Validar métricas de desempeño (RMSE, MAE, MAPE) en contextos de enseñanza e investigación.
- Fomentar reproducibilidad científica mediante notebooks y pipelines documentados.

### Profesionales
- Proveer pronósticos confiables para apoyar decisiones estratégicas en supply chain.
- Generar visualizaciones ejecutivas claras y exportables para audiencias directivas.
- Automatizar flujos de trabajo para reducir tiempos de análisis y aumentar la eficiencia.
- Integrar modelos en pipelines reproducibles y adaptables a distintos sectores (retail, salud, energía).

---

## 📚 Fundamentación teórica y práctica

- **SARIMA**: modelo estadístico para series estacionarias y periódicas.
- **Prophet**: modelo aditivo desarrollado por Facebook, ideal para estacionalidad múltiple y eventos externos.
- **Random Forest**: captura relaciones no lineales y variables explicativas adicionales.
- **Ensemble**: combina modelos para robustez y reducción de sesgo/varianza.  

Las métricas de validación (RMSE, MAE, MAPE) permiten evaluar precisión y estabilidad en contextos tanto académicos como empresariales.

---

## 📂 Estructura del repositorio
```
├── app/ # Código fuente
├── assets/ # Gráficas y reportes ejecutivos generados
├── data/ # Conjuntos de datos
│   ├── inputs/ # Datos de entrada originales
│   └── outputs/ # Resultados y pronósticos generados
├── notebooks/ # Jupyter/Colab notebooks de exploración y desarrollo
├── .gitignore
├── LICENSE
├── README.md # Documentación principal del proyecto
└── requirements.txt # Dependencias del proyecto
```
### ⚙️ Archivos Clave y Descripción

* **`SOLUTION_CHALLENGE_ENSAMBLE.py`**: Script principal de análisis, modelado estadístico y generación de pronósticos. Es el punto de partida para generar los resultados.
* **`db_manager.py`**: Módulo encargado de la creación y gestión de la base de datos SQLite para persistencia de datos y resultados.
* **`app_dashboard.py`**: Código de la aplicación interactiva (Dashboard) en **Streamlit** para la visualización de datos y pronósticos.
* **`requirements.txt`**: Lista de librerías necesarias para instalar y ejecutar el proyecto (usando `pip install -r requirements.txt`).

---

## ⚙️ Instalación

```bash
git clone https://github.com/RobbeAlex/demand-planner.git
cd demand-planner

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```
En Google Colab:
```bash
!pip install prophet statsmodels scikit-learn matplotlib pandas
```

---

## 🧪 Ejemplo de uso

```bash
from src.models import demand_forecast
from src.visualization import plot_forecast
from src.utils import evaluate_model

# Cargar datos
df = load_data("data/sales.csv")

# Entrenar modelo Prophet
forecast = demand_forecast.prophet(df, periods=30)

# Visualizar resultados
plot_forecast(forecast)

# Evaluar desempeño
metrics = evaluate_model(forecast, df)
print(metrics)
```

---

## 📈 Resultados esperados
- Académico: análisis de tendencia y estacionalidad, comparación de modelos, reportes reproducibles.
- Profesional: pronósticos confiables, visualizaciones ejecutivas, métricas claras para la toma de decisiones.

---

## 🧑‍🏫 Aplicaciones
- Académicas: cursos de estadística aplicada, seminarios de machine learning, proyectos de investigación, tesis.
- Profesionales: planeación de inventarios, optimización de supply chain, análisis de ventas, proyecciones financieras.
---

## 📊 Modelos soportados

| Modelo        | Contexto académico/profesional recomendado       |
|---------------|--------------------------------------------------|
| Prophet       | Estacionalidad múltiple, eventos externos        |
| SARIMA        | Series estacionarias y periódicas                |
| Random Forest | Variables adicionales, relaciones no lineales    |
| Ensemble      | Robustez y reducción de sesgo/varianza           |

---

## 📜 Referencias bibliográficas
- Hyndman, R. J., & Athanasopoulos, G. (2018). Forecasting: Principles and Practice. OTexts.
- Taylor, S. J., & Letham, B. (2018). Forecasting at scale. The American Statistician, 72(1), 37–45.
- Breiman, L. (2001). Random Forests. Machine Learning, 45(1), 5–32.
- Box, G. E. P., Jenkins, G. M., & Reinsel, G. C. (2015). Time Series Analysis: Forecasting and Control. Wiley.

---

## 🏭 Casos de uso en la industria
- Retail: predicción de ventas para optimizar inventarios y reducir quiebres de stock.
- Salud: estimación de demanda de medicamentos y equipos médicos para mejorar la logística hospitalaria.
- Energía: pronóstico de consumo eléctrico para balancear oferta y demanda en redes inteligentes.
- Manufactura: planificación de producción en función de la demanda proyectada, reduciendo costos de almacenamiento.
- Transporte y logística: predicción de flujos de carga para optimizar rutas y capacidad de distribución.

---

## 🤝 Contribuciones
Se invita a estudiantes, docentes, investigadores y profesionales a: 
- Proponer nuevos modelos o métricas.
- Documentar casos de uso en diferentes industrias.
- Extender notebooks con experimentos reproducibles.
- Adaptar pipelines a entornos empresariales.

---

## 📜 Licencia
Este proyecto está bajo la licencia MIT.
Consulta el archivo LICENSE para más detalles.

---

## 👨‍💻 Autor
Roberto Alejandro Chagra Martínez
Licenciado en Nutrición y estudiante de Inteligencia Artificial y Ciencia de Datos en la Universidad de Guadalajara.
Experiencia en consultoría independiente y gestión operativa, con enfoque en:
- Optimización de modelos estadísticos.
- Automatización de pipelines.
- Visualización ejecutiva para tomadores de decisión.

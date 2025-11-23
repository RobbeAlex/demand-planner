# Pronóstico de Demanda para empresa farmaceutica 💊📈

**Equipo:** Quantum Analytics
**Challenge:** CUGDL 2025B

## Descripción del Proyecto

Este repositorio contiene la solución al reto de pronóstico de demanda de una empresa farmacéutica. Desarrollamos un sistema integral que no solo predice la demanda futura con alta precisión estadística, sino que también operacionaliza los resultados para la toma de decisiones gerenciales.

## Características Principales 🚀

* **Modelo Predictivo "Ensemble":** Combinación robusta de SARIMA, Prophet y Random Forest Regressor para minimizar el error de pronóstico.
* **Gestión de Incertidumbre:** Cálculo de intervalos de confianza del 95% para la gestión de riesgos de inventario.
* **Segmentación Inteligente:** Clustering (K-Means) de productos para identificar patrones de comportamiento.
* **Automatización Sostenible:** Base de datos SQLite integrada para la ingesta automática de nuevos datos mensuales y reentrenamiento del modelo.
* **Dashboard Ejecutivo Interactivo:** Interfaz gráfica (Streamlit) para la visualización de la visión global de la empresa y el detalle por cliente/producto.

## Estructura del Repositorio 📂

* `SOLUTION_CHALLENGE_ENSAMBLE.py`: Script principal de análisis, modelado estadístico y generación de pronósticos.
* `db_manager.py`: Módulo encargado de la creación y gestión de la base de datos SQLite.
* `app_dashboard.py`: Código de la aplicación interactiva (Dashboard) en Streamlit.
* `requirements.txt`: Lista de librerías necesarias para ejecutar el proyecto.

## Cómo Ejecutar el Proyecto 🛠️

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
    ```
2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Inicializar la Base de Datos (Primera vez):**
    Ejecutar el script principal para procesar los datos históricos y poblar la BD.
    ```bash
    python SOLUTION_CHALLENGE_ENSAMBLE.py
    ```
4.  **Lanzar el Dashboard:**
    ```bash
    streamlit run app_dashboard.py
    ```

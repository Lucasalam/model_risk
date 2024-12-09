# Model Risk

## Descripción del Proyecto
Este proyecto tiene como objetivo construir un sistema de modelado de riesgo para evaluar y predecir la probabilidad de default en una cartera de facturas. El proceso abarca desde el análisis exploratorio de datos hasta el cálculo de provisiones utilizando técnicas de Machine Learning y estadística clásica. 

A través de notebooks organizadas y bien estructuradas, se abordan diferentes etapas del ciclo de vida de un modelo, incluyendo preparación de datos, ingeniería de características, modelado base, modelado avanzado y análisis de resultados.

---

## Estructura del Proyecto

El proyecto está dividido en varias notebooks, cada una enfocada en una etapa clave del desarrollo del modelo:

### 1. **01_Exploratory_Data_Analysis.ipynb**
   - **Objetivo:** Realizar un análisis exploratorio para entender mejor los datos y descubrir patrones clave.
   - **Contenido:** Análisis de datos faltantes, valores extremos, duplicados y tendencias temporales.
   - **Hallazgos Clave:** 
     - El `bad rate` aumenta con el tiempo, sugiriendo cambios en la distribución de variables.
     - Los días promedio de pago son 40 días, pero con fluctuaciones en periodos de pandemia.

---

### 2. **02_Data_Preparation_and_Segmentation.ipynb**
   - **Objetivo:** Limpiar los datos y segmentarlos en bases de desarrollo, validación y prueba.
   - **Contenido:** Dividir la base por IDs para evitar fugas de información y preparar los datos para el modelado.
   - **Hallazgos Clave:**
     - Decisiones prácticas para mantener una base sin transformación excesiva para pruebas futuras.

---

### 3. **03_Feature_Engineering.ipynb**
   - **Objetivo:** Crear y seleccionar características relevantes para capturar comportamientos y tendencias.
   - **Contenido:** Generación de variables como `prbm_sector`, transformaciones logarítmicas, y selección de variables basadas en correlación.
   - **Hallazgos Clave:**
     - `date_paymentDays_cap` y `prbm_sector` se destacan como las variables más importantes según SHAP values.
     - Se observan relaciones no lineales en características clave como `expirationDays`.

---

### 4. **04_Baseline_Model.ipynb**
   - **Objetivo:** Desarrollar un modelo base utilizando regresión logística para establecer un punto de referencia.
   - **Contenido:** Construcción y evaluación de un modelo base con `statsmodels` y réplica con `sklearn`.
   - **Hallazgos Clave:**
     - El modelo base es estable entre entrenamiento y validación con un AUC de 0.94.
     - Limitaciones en la curva Precision-Recall, indicando espacio para mejoras con nuevas características.

---

### 5. **05_Advanced_Model.ipynb**
   - **Objetivo:** Implementar un modelo avanzado utilizando LightGBM y optimización de hiperparámetros.
   - **Contenido:** Ajuste de parámetros con Hyperopt y análisis de importancia de variables con SHAP.
   - **Hallazgos Clave:**
     - LightGBM maneja mejor las relaciones no lineales, especialmente para `expirationDays`.
     - Diferencias notables en la distribución de provisiones entre LightGBM y regresión logística.

---

### 6. **06_Pipeline.ipynb**
   - **Objetivo:** Construir un pipeline reproducible para preprocesamiento y modelado.
   - **Contenido:** Uso de `ColumnTransformer`, pipelines personalizados y serialización del modelo en `.pkl`.
   - **Hallazgos Clave:**
     - Pipelines reproducibles simplifican la integración en producción.


---

### 7. **07_PE.ipynb**
   - **Objetivo:** Calcular las provisiones esperadas (PE) utilizando metodologia sencilla.
   - **Contenido:** Comparación de técnicas de provisión, incluyendo cálculos basados en EAD, y LGD.
   - **Hallazgos Clave:**
     - La provisión total calculada es de **4,105,994,051.59**.


---

## Hallazgos Generales
- La combinación de métodos tradicionales (RL) y avanzados (ML) ofrece una visión complementaria para la gestión del riesgo.
- Las técnicas de Machine Learning, como LightGBM, destacan por capturar relaciones no lineales y mejorar la separación entre segmentos.
- Provisiones calculadas reflejan tendencias observadas en los datos, como el incremento del `bad rate` con el tiempo.
- SHAP values y análisis PDP han ayudado a identificar las variables clave y su comportamiento, como `expirationDays` y `payerSalesSegment`.

---

## Conclusiones
- **Estabilidad:** El modelo base y el modelo avanzado son estables en términos de desempeño entre entrenamiento y validación.
- **Flexibilidad:** LightGBM maneja mejor las relaciones no lineales, pero la regresión logística proporciona una base sólida y explicable.
- **Provisiones:** Las provisiones totales reflejan adecuadamente las pérdidas esperadas, aunque hay margen para mejorar 
- **Producción:** Los pipelines implementados en `sklearn` facilitan la implementación en producción y reproducibilidad.
- **Próximos pasos:** Continuar iterando sobre las características y ajustando los modelos para mejorar la separación en decisiones clave y reducir el riesgo.

---

Este proyecto proporciona un marco sólido para evaluar el riesgo de crédito y las pérdidas esperadas, destacando la importancia de integrar enfoques estadísticos y de Machine Learning.

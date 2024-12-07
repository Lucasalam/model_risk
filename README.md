# Demand Forecasting SKU

## Descripción del Proyecto

Este proyecto tiene como objetivo desarrollar un modelo de forecast de demanda semanal a nivel SKU. El enfoque principal es predecir la demanda para los próximos 3 días, donde el forecast de cada día equivale a la suma de las ventas proyectadas para los próximos 7 días. Esta solución sigue un enfoque estructurado, desde el análisis exploratorio de datos hasta la implementación de modelos de machine learning y técnicas avanzadas de forecasting con redes neuronales.

## Estructura del Proyecto

El proyecto está dividido en varias notebooks, cada una de las cuales aborda una parte específica del proceso de modelado:

1. **01_Exploratory_Data_Analysis.ipynb**
   - **Objetivo:** Realizar un análisis exploratorio para entender mejor los datos de ventas y su distribución.
   - **Contenido:** Distribuciones de ventas, análisis de series temporales, y patrones entre variables clave.
   - **Hallazgos Clave:** Identificación de patrones de demanda y diferencias significativas entre ciudades y productos.

2. **02_Data_Preparation_and_Segmentation.ipynb**
   - **Objetivo:** Limpiar y segmentar los datos para mejorar la precisión de los modelos de predicción.
   - **Contenido:** Limpieza de datos, manejo de valores nulos, segmentación por antigüedad y demanda.
   - **Hallazgos Clave:** Creación de segmentos diferenciados que permiten estrategias de modelado específicas.

3. **03_Feature_Engineering.ipynb**
   - **Objetivo:** Crear y seleccionar características relevantes que capturen la estacionalidad y las tendencias de ventas.
   - **Contenido:** Generación de características basadas en fechas, ventas pasadas y combinaciones de variables.
   - **Hallazgos Clave:** Características que mejoran significativamente la capacidad predictiva de los modelos.

4. **04_Baseline_Model.ipynb**
   - **Objetivo:** Implementar un modelo base de machine learning que sirva como referencia para evaluar futuras mejoras.
   - **Contenido:** Creación de un modelo simple de regresión y evaluación mediante `mean_absolute_error`.
   - **Hallazgos Clave:** El modelo base establece una línea de referencia para medir el éxito de enfoques más avanzados.

5. **05_Advanced_Model.ipynb**
   - **Objetivo:** Desarrollar un modelo avanzado utilizando redes neuronales recurrentes (LSTM) para mejorar el forecasting.
   - **Contenido:** Implementación de un modelo LSTM mediante la clase `ForecasterRnn`, entrenamiento, y evaluación de su rendimiento.
   - **Hallazgos Clave:** El modelo avanzado LSTM mostró una mejora significativa en la precisión, con un `mean_absolute_error` mucho menor en comparación con el modelo base.

## Hallazgos Generales

A lo largo del proyecto, se observó una mejora constante en la precisión de los modelos de forecasting a medida que se implementaron técnicas más avanzadas. El modelo final, basado en LSTM, superó significativamente al modelo base de machine learning, demostrando el valor de las redes neuronales en la predicción de demanda en este contexto.

## Instrucciones de Uso


2. **Ejecución de Notebooks:**
   - Las notebooks deben ejecutarse en el orden indicado para replicar los resultados.
   - Cada notebook está documentada con comentarios para facilitar la comprensión del proceso.

3. **Predicciones Finales:**
   - Las predicciones resultantes se encuentran en el archivo `submission.csv`, generado a partir del modelo avanzado.

## Conclusiones

Este proyecto demuestra la importancia de un enfoque metódico y basado en datos para la predicción de demanda. Los resultados obtenidos subrayan la eficacia del uso de técnicas avanzadas como las redes neuronales LSTM, que permiten una mejora significativa en la precisión del forecasting.


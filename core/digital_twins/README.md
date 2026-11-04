# 🏛️ Core / Digital Twins

## 📌 Propósito del Dominio
Esta carpeta alberga la infraestructura lógica, los esquemas de validación y las herramientas de auditoría para la creación y evaluación de **Gemelos Digitales (Digital Twins)** dentro del ecosistema `web-hiteration`. 

No es una carpeta de aplicaciones (como `applications/atenea/`); es un **dominio ontológico y transversal**. Aquí se define qué es un Gemelo Digital, qué no lo es, y bajo qué reglas epistémicas se permite que una entidad virtual interactúe con el mundo físico.

## ⚖️ 1. La Distinción Fundamental (¿Qué es y qué no es un Gemelo Digital?)

Basado en el marco de IBM y adaptado a las invariantes de `web-hiteration`, aplicamos una distinción estricta para evitar la "alucinación arquitectónica":

1.  **Modelo 3D (Representación Estática):** Es una fotografía del diseño. No tiene datos en tiempo real. *Ejemplo: Un render de AutoCAD del chasis ARES-M1.*
2.  **Simulación (Escenario Hipotético):** Ejecuta escenarios predefinidos sin conexión con el sistema físico. Sirve para probar teorías, pero no para operar el presente. *Ejemplo: Un script de Python que simula cómo caería el robot si se apaga un motor.*
3.  **Gemelo Digital (Réplica Dinámica):** Es la única entidad que califica en este dominio. Requiere **intercambio de datos bidireccional en tiempo real**. Si el activo físico cambia, el gemelo se actualiza; si el gemelo calcula una optimización, el activo físico la ejecuta. *Ejemplo: La Raspberry Pi actualizando el estado de los servos del ESP32 basándose en la telemetría del IMU.*

## 🏗️ 2. Los 7 Componentes Innegociables (Filtro IBM)

Para que cualquier propuesta de `web-hiteration` sea registrada en esta carpeta como un Gemelo Digital válido, debe documentar explícitamente los 7 componentes:
1.  **Activo Físico (Physical Asset):** El hardware real o proceso tangible.
2.  **Modelo Virtual (Virtual Model):** La representación digital con estado sincronizado.
3.  **Fuentes de Datos (Data Sources):** Sensores o APIs que capturan la realidad.
4.  **Pipeline de Datos (Data Pipeline):** El canal de transporte (ej. MQTT) que asegura que los datos fluyan sin pérdida.
5.  **Bucle de Retroalimentación (Feedback Loop):** El mecanismo por el cual el modelo virtual envía comandos de ajuste al activo físico.
6.  **Motor de Analítica (Analytics Engine):** El algoritmo (o LLM) que procesa los datos para predecir o decidir.
7.  **Visualización (Visualization Interfaces):** El dashboard (aunque sea de consola) donde un humano observa el estado del gemelo.

## 🛡️ 3. Invariantes Epistémicas (El Escudo del Corpus)

La implementación de Gemelos Digitales en este repositorio está sujeta a las siguientes reglas de seguridad lógica:

*   **`SPECIFICATION_IS_NOT_IMPLEMENTATION`**: Tener un archivo `.json` que describa cómo funcionará el gemelo no significa que ya esté funcionando. Los archivos aquí presentes deben declarar su estado (`PROPOSED`, `IN_PROGRESS`, `VALIDATED`).
*   **`SELF_EVALUATION_IS_NOT_INDEPENDENT_VALIDATION`**: El Gemelo Digital (el modelo virtual) no puede auditarse a sí mismo. La lógica del "Meta-Auditor" (la Capa 3 que evalúa las decisiones del gemelo antes de ejecutarlas) debe ser un proceso aislado. 
*   **`DOCUMENTARY_ABSENCE_IS_NOT_PROOF_OF_NONEXISTENCE`**: Si un componente del pipeline (como un sensor) no está documentado en el código actual, no se asume que no exista en el diseño teórico; simplemente se marca como `MISSING_IN_IMPLEMENTATION`.

## 📂 4. Estructura de Archivos en esta Carpeta

*   **`twin_architecture.schema.json`**: El esquema de validación (JSON Schema). Define la estructura que debe tener cualquier propuesta de Gemelo Digital (sea un robot, una red de satélites o una economía histórica) para ser considerada consistente con `web-hiteration`.
*   **`consistency_auditor.py`**: Script de Python que toma un archivo JSON de propuesta y lo evalúa contra el esquema y las invariantes. Devuelve un diagnóstico (Ej. `CONSISTENT_TWIN`, `STATIC_SIMULATION_ONLY`).
*   **`(Futuros) twin_implementations/`**: Subcarpeta prevista para almacenar las definiciones JSON específicas de cada gemelo validado (ej. `atenea_twin.json`, `cybersyn_twin_analysis.json`).

## 🧠 5. Aplicaciones Prácticas en el Repositorio

*   **Proyecto ATENEA:** El ESP32 (capa física) y la Raspberry Pi (capa cognitiva) forman un Gemelo Digital de **Sistema**.
*   **Caso Cybersyn:** Se evalúa como un Gemelo Digital de **Proceso** histórico. Al carecer de un pipeline de retorno automatizado (los teletipos enviaban datos, pero los ajustes económicos requerían intervención humana), el auditor lo clasificará como un **Incomplete Twin** (Gemelo Digital Parcial), lo que demuestra la utilidad del filtro para no caer en anacronismos.
*   **Periféricos SDR:** Una antena satelital conectada a un teléfono puede ser un Gemelo Digital de **Componente** si el software (como K2er o un script SDR) refleja el estado del espectro radioeléctrico en tiempo real.

## 🚀 Principio Rector
> *"Un Gemelo Digital no es un adorno visual; es un contrato matemático entre el mundo físico y el mundo virtual. Si el canal de retorno se rompe, el gemelo se convierte en un fantasma."*

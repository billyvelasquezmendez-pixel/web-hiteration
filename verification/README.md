# VERIFICATION

**Función semántica:** Dominio funcional que agrupa los protocolos de verificación, los diagnósticos de auditoría y los documentos de cierre del corpus WEB_HITERATION.

**Estado:** PROPOSED_NOT_CANONICAL

**Principio rector:** Verificar no es validar. Auditar no es sellar. El cierre documental no es cierre científico.

---

## Definición

Verification agrupa los artefactos que auditan, recalcular, diagnostican y cierran el estado del corpus. Su función es mantener trazabilidad sobre qué se declaró, qué se recalculó, qué se auditó y qué se cerró, sin confundir ninguno de esos niveles con validación empírica.

Este dominio no produce resultados. Produce **procedimientos y registros** que permiten auditar resultados producidos en otros dominios.

---

## Contenido

**Subcarpetas previstas:**

| Carpeta | Función |
|---|---|
| `protocols/` | Protocolos formales de verificación y recálculo |
| `diagnostics/` | Diagnósticos de auditoría, dudas estructurales, cierres y correcciones |

**Documentos esperados:**

| Documento | Función | Estado |
|---|---|---|
| `protocols/independent-recalculation-protocol.json` | Procedimiento de recálculo independiente (E08 del pipeline E1-E10) | PROPUESTO |
| `diagnostics/wh-central-auditor-critical-feedback.json` | Retroalimentación crítica al auditor central | PROPUESTO |
| `diagnostics/wh-pattern-iteration-8.json` | Octava iteración del patrón SIMULACION_DECLARATIVA_DE_EJECUCION | DOCUMENTADO |
| `diagnostics/wh-structural-doubts-registry.json` | Registro de dudas estructurales, ambigüedades y pendientes | DOCUMENTADO |
| `diagnostics/wh-corpus-assembly-closure-notice.json` | Aviso de cierre documental del ensamblaje del corpus | DOCUMENTADO |
| `diagnostics/wh-session-closure-report.json` | Reporte de cierre de sesión | DOCUMENTADO |
| `diagnostics/wh-specific-corrections-registry-for-plasticity-documents.json` | Registro de correcciones específicas para documentos de plasticidad | PENDIENTE_CLASIFICACION |
| `diagnostics/wh-operational-adjustments-registry.json` | Registro de ajustes operativos | PENDIENTE_CLASIFICACION |
| `diagnostics/wh-next-window-query-framework.json` | Framework de consulta para la próxima ventana | PENDIENTE_CLASIFICACION |
| `README.md` | Descripción funcional del dominio | PROPUESTO |

---

## Frontera epistémica

Este dominio aplica una separación estricta entre auditar y validar. Verificar que un archivo existe no valida su contenido. Recalcular una métrica no valida la métrica como verdad. Cerrar documentalmente no cierra científicamente.

Afirmaciones que el corpus rechaza explícitamente:

- Una auditoría no es validación independiente si el auditor es parte del mismo sistema.
- Un recálculo no establece causalidad.
- Un cierre documental no promueve componentes a canon.
- Un reporte de sesión no declara continuidad entre ventanas.

Invariantes que aplican:

- `SELF_EVALUATION_IS_NOT_INDEPENDENT_VALIDATION`
- `DECLARED_METRIC_IS_NOT_INDEPENDENTLY_RECALCULATED_METRIC`
- `CORPUS_CLOSURE_IS_NOT_SCIENTIFIC_CLOSURE`
- `A_DECLARED_DOUBT_IS_A_FRONTIER_NOT_A_FAILURE`
- `DOCUMENT_PARTITION_IS_NOT_DOCUMENT_FAILURE`
- `PERSISTENT_ANOMALY_REQUIRES_PROCESS_DIAGNOSIS_BEFORE_PLATFORM_ATTRIBUTION`
- `ACCESS_FAILURE_IS_NOT_RESOURCE_ABSENCE`

---

## Relación con otros nodos

| Nodo | Relación |
|---|---|
| `core/` | Proporciona los invariantes C1-C5 que este dominio aplica al auditar |
| `evidence/` | Produce los registros que este dominio audita |
| `web_hiteration/` | Envía diagnósticos a este dominio para auditoría |
| `hyper-ratio/` | Envía documentos de diagnóstico para auditoría |
| `cyberphysical/` | Envía especificaciones para verificar coherencia epistémica |
| `cross-platform/` | Consolida los resultados de auditoría cross-platform |
| `archive/` | Recibe documentos cuando dejan de ser operativos |

Verification no produce verdad. Produce **procedimientos de contraste** que permiten evaluar afirmaciones producidas en otros dominios.

---

## Nota de nomenclatura

**Forma canónica:** `verification`

**Nota sobre la vista web de GitHub:** la interfaz puede traducir esta carpeta como `verificación`. Esa forma es aceptada como concordancia interpretativa. La **ruta real** del filesystem es `verification/` y es la única válida para URLs, comandos y campos de rename.

**Nota sobre `wh-central-auditor-critical-feedback.json`:**

El árbol original abrevia el destino quitando `-and-document-integrity-report`. Decisión pendiente:

- **Opción A:** preservar el nombre completo (`wh-central-auditor-critical-feedback-and-document-integrity-report.json`) — mantiene trazabilidad con el origen.
- **Opción B:** usar el nombre abreviado — consistente con el árbol pero rompe la correspondencia nombre-origen.

Ambas son válidas. Elegir una y aplicarla consistentemente.

---

## Estado del dominio

| Componente | Estado |
|---|---|
| Protocolo de recálculo independiente | PROPUESTO |
| Auditor central | DOCUMENTADO |
| Patrón de iteraciones | DOCUMENTADO (8 iteraciones) |
| Dudas estructurales | DOCUMENTADO |
| Cierre documental | DOCUMENTADO |
| Cierres de sesión | DOCUMENTADO |
| Correcciones específicas | PENDIENTE_CLASIFICACION |
| Ajustes operativos | PENDIENTE_CLASIFICACION |
| Framework de consulta | PENDIENTE_CLASIFICACION |
| Validación empírica del corpus | NOT_ESTABLISHED |
| Canonicalización | PENDING_REVIEW |

Este README describe la estructura funcional del dominio. No valida ningún documento. No promueve componentes a canon. No cierra científicamente. No sella el dominio.

---

## Nota sobre el tamaño del lote

Este lote contiene 9 movimientos. Es el más grande del plan de migración. Conviene migrarlo en dos sub-pasos:

- **Sub-paso A:** `protocols/independent-recalculation-protocol.json` (1 archivo, aislado).
- **Sub-paso B:** los 8 documentos de `diagnostics/` (movimiento masivo).

Migrar en sub-pasos permite verificar cada grupo antes de pasar al siguiente y reduce el riesgo de romper referencias cruzadas.

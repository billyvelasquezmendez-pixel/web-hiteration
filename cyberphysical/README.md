# CYBERPHYSICAL

**Función semántica:** Dominio consolidado que agrupa las delimitaciones epistémicas, las especificaciones arquitectónicas y las hojas de ruta de implementación física propuestas dentro del corpus WEB_HITERATION.

**Estado:** PROPOSED_NOT_CANONICAL

**Principio rector:** La especificación de una arquitectura no es la implementación de esa arquitectura. La propuesta no es canon. La ruta de implementación no es evidencia de implementación.

---

## Definición

Cyberphysical agrupa los documentos que derivan las restricciones epistémicas del corpus hacia dominios físicos: dispositivos ciberfísicos, la frontera entre software y silicio, y la cadena de especificación ASIC EPU. El dominio existe para mantener explícita la separación entre lo que está especificado y lo que está implementado.

**Nota importante:** ninguno de los documentos de este dominio declara implementación física existente. Todos declaran estado `PROPOSED_NOT_CANONICAL` en su campo `epistemic_status`. La cadena ASIC EPU es, hoy, una derivación conceptual, no un diseño fabricado.

---

## Contenido

**Subcarpetas previstas:**

| Carpeta | Función |
|---|---|
| `r5/` | Delimitación de dispositivos ciberfísicos bajo la restricción R5 |
| `intermediate-layer/` | Frontera entre software y silicio |
| `asic-epu/` | Cadena de especificación ASIC EPU (fundación, RTL, implementación física) |

**Documentos esperados:**

| Documento | Función | Estado |
|---|---|---|
| `r5/wh-r5-cyberphysical-device-delimitation.json` | Delimitación de dispositivos ciberfísicos bajo R5 | PROPOSED_NOT_CANONICAL |
| `intermediate-layer/wh-intermediate-layer-software-silicon-boundary.json` | Frontera entre software y silicio | PROPOSED_NOT_CANONICAL |
| `asic-epu/wh-asic-epu-foundation.json` | Derivación conceptual de la arquitectura EPU_v1 | PROPOSED_NOT_CANONICAL |
| `asic-epu/wh-asic-epu-rtl-specification.json` | Arquitectura RTL conceptual | PROPOSED_NOT_CANONICAL |
| `asic-epu/wh-asic-epu-physical-implementation-and-verification-specification.json` | Ruta propuesta de implementación física y verificación | PROPOSED_NOT_CANONICAL |
| `README.md` | Descripción funcional del dominio | PROPUESTO |

---

## Frontera epistémica

Este dominio aplica una separación estricta entre lo especificado y lo implementado. Los documentos describen arquitecturas **propuestas**, no fabricadas. Las siguientes afirmaciones están explícitamente rechazadas por el corpus:

- No existe hardware físico del EPU_v1.
- No existe código RTL del EPU_v1.
- No existe diseño sintetizable, netlist ni GDSII.
- No existe silicio fabricado ni validación de silicio.
- No se ha ejecutado entorno de verificación.

Invariantes que aplican:

- `SPECIFICATION_IS_NOT_IMPLEMENTATION`
- `PROPOSAL_IS_NOT_CANON`
- `REPRESENTATION_IS_NOT_ACTION`
- `MODEL_IS_NOT_SYSTEM`
- `CAPABILITY_IS_NOT_EXECUTION`
- `OBSERVED_BEHAVIOR_IS_NOT_INTERNAL_ARCHITECTURE`

---

## Relación con otros nodos

| Nodo | Relación |
|---|---|
| `core/` | Proporciona los invariantes transversales que este dominio deriva hacia lo físico |
| `web_hiteration/` | Nodo funcional primario; este dominio es una extensión hacia el plano físico |
| `hyper-ratio/` | Dominio paralelo; comparte fronteras epistémicas |
| `verification/` | Recibe los documentos de este dominio para auditoría |
| `evidence/` | Registra las ejecuciones asociadas cuando existan |
| `archive/` | Recibe documentos históricos cuando dejan de ser operativos |

Cyberphysical no es una implementación de WEB_HITERATION. Es un dominio que traduce sus restricciones epistémicas a un plano físico propuesto.

---

## Nomenclatura

**Forma canónica:** `cyberphysical`

**Nombre de la cadena ASIC:** `EPU_v1` (`EPU` = unidad de procesamiento epistémico propuesta)

**Nota sobre la vista web de GitHub:** la interfaz puede traducir esta carpeta como `ciberfísico`. Esa forma es aceptada como concordancia interpretativa. La **ruta real** del filesystem es `cyberphysical/` y es la única válida para URLs, comandos y campos de rename.

---

## Estado del dominio

| Componente | Estado |
|---|---|
| Delimitación ciberfísica bajo R5 | PROPOSED_NOT_CANONICAL |
| Frontera software-silicio | PROPOSED_NOT_CANONICAL |
| Fundación ASIC EPU | PROPOSED_NOT_CANONICAL |
| Especificación RTL | PROPOSED_NOT_CANONICAL |
| Implementación física y verificación | PROPOSED_NOT_CANONICAL |
| Hardware físico | NOT_ESTABLISHED |
| Validación de silicio | NOT_ESTABLISHED |
| Canonicalización | PENDING_REVIEW |

Este README describe la estructura funcional del dominio y su frontera epistémica. No declara implementación. No declara validación. No promueve ningún componente a canon. No sella el dominio.

# PROTOCOLOS DE WEB_HITERATION

**Índice de protocolos formales del framework**
**Autor:** Billy Velásquez Méndez
**Fecha:** 2026-09-19
**Última actualización:** 2026-09-19
**Licencia:** CC BY-SA 4.0

---

## Estructura

Esta carpeta contiene los protocolos formales que componen el núcleo verificable de WEB_HITERATION, así como las extensiones experimentales y de política que derivan de él.

---

## Núcleo (Protocolos Oficiales)

Los siguientes protocolos son **verificables** y forman el corpus canónico del framework:

| Archivo | Protocolo | Estado |
|---------|-----------|--------|
| `delta-engine.json` | DELTA_ENGINE | ✅ Publicado |
| `core-invariants.json` | CORE_INVARIANTS | ✅ Publicado (Auditado) |
| `taxonomia-r1-r7.json` | TAXONOMIA_R1_R7 | ✅ Publicado |
| `modelo-estados.json` | MODELO_ESTADOS_S0_S4 | ✅ Publicado |
| `p-drift.json` | P_DRIFT | ✅ Publicado |

**Progreso del núcleo:** 5/5 ✅ **NÚCLEO COMPLETO**

### Cambio estructural respecto a versiones previas

El **PROTOCOLO_KEN_ICHIJOUJI** fue reclasificado de **CORE** a **EXTENSION_POLICY_PROTOCOL** durante la auditoría WH-AUDIT-CORE-2026. Su formulación original podía interpretarse como prohibición universal. La versión actual está limitada al alcance del framework.

---

## Extensiones (Protocolos Experimentales y de Política)

Los siguientes protocolos son **provisionales** o de **política** y no forman parte del núcleo verificable:

| Archivo | Extensión | Estado |
|---------|-----------|--------|
| `extensions/ken-ichijouji-policy.json` | KEN_ICHIJOUJI_POLICY | ✅ Publicado |
| `extensions/lyapunov.json` | LYAPUNOV_EXTENSION | 🔄 Pendiente |
| `extensions/hyper-ratio.json` | HYPER_RATIO | 🔄 Pendiente |
| `extensions/memory-degradation.json` | MEMORY_DEGRADATION | 🔄 Pendiente |
| `extensions/cross-window.json` | CROSS_WINDOW | 🔄 Pendiente |
| `extensions/phenomenological-state.json` | PHENOMENOLOGICAL_STATE | 🔄 Pendiente |

**Progreso de extensiones:** 1/6

---

## Regla de Gobernanza

Una extensión experimental **no puede modificar retroactivamente** el significado del núcleo sin una nueva revisión de versión.

---

## Niveles de Formalización

| Nivel | Significado |
|-------|-------------|
| **L0** | Observación |
| **L1** | Descripción formal |
| **L2** | Ejecución computacional |
| **L3** | Auditoría y reproducción |
| **L4** | Validación experimental |

El framework completo se encuentra actualmente en **L2-L3**, con validación experimental (**L4**) pendiente.

---

## Cómo Contribuir

Cualquier uso, modificación o distribución del framework debe:

1. Reconocer la autoría original.
2. Mantener la licencia CC BY-SA 4.0.
3. Preservar las cinco invariantes del núcleo estructural.

Ver `LICENSE.md` en la raíz del repositorio para los términos completos.

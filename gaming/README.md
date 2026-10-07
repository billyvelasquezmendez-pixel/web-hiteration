# GAMING

**Función semántica:** Dominio funcional que agrupa las especificaciones, blueprints de implementación y análisis de sistemas de comportamiento autónomo aplicados a videojuegos, bajo las restricciones epistémicas del corpus WEB_HITERATION.

**Estado:** PROPOSED_NOT_CANONICAL

**Principio rector:** La especificación de un comportamiento de NPC no es la ejecución de ese comportamiento en un juego. El blueprint de implementación no es código ejecutado. El análisis del blueprint no es validación del sistema.

---

## Definición

Gaming agrupa el diseño, la especificación y el análisis de sistemas de decisión autónoma para personajes no jugables. El dominio aplica las restricciones R1–R7 y los invariantes C1–C5 a la lógica de comportamiento de NPCs: percepción, resolución de prioridades, estimación de riesgo, validación de decisiones, retroalimentación y replanificación operativa.

**Alcance del dominio:** no diseña videojuegos completos, no define mecánicas de gameplay general, no incluye arte, narrativa ni diseño de niveles. Se limita a la capa de decisión autónoma de agentes.

---

## Contenido previsto

**Subcarpetas:**

| Carpeta | Función |
|---|---|
| `npc/` | Especificaciones de NPC autónomo: jerarquía de decisión, modelo funcional de datos, autoevaluación restringida |
| `implementation/` | Blueprints de implementación en C# y C++ (Unreal Engine 5), análisis de bugs, correcciones |
| `patterns/` | Registro de patrones recurrentes detectados en el dominio |

**Documentos previstos:**

| Documento | Función | Estado |
|---|---|---|
| `npc/wh-npc-utility-spec.json` | Especificación funcional del NPC: jerarquía L1–L5, modelo de datos, fórmula de score | PROPUESTO |
| `npc/wh-npc-decision-pipeline.json` | Pipeline de ejecución: percepción, intención, jerarquía, validación, ejecución, retroalimentación, replanificación | PROPUESTO |
| `implementation/wh-npc-ue5-blueprint.json` | Blueprint de implementación C++/C# en Unreal Engine 5 | PROPUESTO |
| `implementation/wh-npc-ue5-bug-analysis.json` | Análisis de bugs del blueprint | PROPUESTO |
| `patterns/wh-declarative-simulation-pattern-gaming.json` | Registro del patrón de declaración de ejecución sin sustrato | PROPUESTO |

---

## Frontera epistémica

Este dominio **no declara** que ningún NPC esté implementado en un motor de juego. **No declara** que el blueprint haya sido compilado, ejecutado ni probado en un entorno real. **No declara** validación empírica de ningún tipo.

**Regla crítica:** la convergencia terminológica con el dominio `cyberphysical/` (variables como `intent_confidence`, `risk_level`, `context_decay`, `falsification_bias` compartidas con la especificación RTL EPU) es **terminológica, no ontológica**. El sustrato de ejecución es diferente: software de gameplay vs. especificación de hardware digital. Cualquier análisis de este dominio debe limitarse a la lógica de software.

**Invariantes que aplican:**

- `MODEL_IS_NOT_SYSTEM`
- `SPECIFICATION_IS_NOT_IMPLEMENTATION`
- `REPRESENTATION_IS_NOT_ACTION`
- `OBSERVED_BEHAVIOR_IS_NOT_INTERNAL_ARCHITECTURE`
- `CAPABILITY_IS_NOT_EXECUTION`
- `SELF_EVALUATION_IS_NOT_INDEPENDENT_VALIDATION`
- `PROPOSAL_IS_NOT_CANON`
- `TECHNICAL_TERM_ACCEPTS_INTERPRETIVE_CONCORDANCE_ACROSS_LANGUAGES`

**Invariante específica del dominio:**

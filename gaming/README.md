{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "WEB_HITERATION_GAMING_DOMAIN_README_MANIFEST",
  "version": "1.0.0-PROPOSED",
  "protocol_reference": "WH-GAMING-README-2026",
  "document_type": "DOMAIN_MANIFEST_README",
  "status": "PROPOSED_NOT_CANONICAL",
  "timestamp": "2026-10-07T10:09:00-03:00",

  "domain_info": {
    "domain": "GAMING",
    "semantic_function": "Dominio funcional que agrupa las especificaciones, blueprints de implementación y análisis de sistemas de comportamiento autónomo aplicados a videojuegos, bajo las restricciones epistémicas del corpus WEB_HITERATION.",
    "governing_principle": "La especificación de un comportamiento de NPC no es la ejecución de ese comportamiento en un juego. El blueprint de implementación no es código ejecutado. El análisis del blueprint no es validación del sistema."
  },

  "definition": {
    "summary": "Gaming agrupa el diseño, la especificación y el análisis de sistemas de decisión autónoma para personajes no jugables. El dominio aplica las restricciones R1–R7 y los invariantes C1–C5 a la lógica de comportamiento de NPCs: percepción, resolución de prioridades, estimación de riesgo, validación de decisiones, retroalimentación y replanificación operativa.",
    "scope_boundaries": "Este dominio no diseña videojuegos completos, no define mecánicas de gameplay general, y no incluye arte, narrativa ni diseño de niveles. Se limita a la capa de decisión autónoma de agentes."
  },

  "planned_contents": {
    "subfolders": [
      {
        "path": "npc/",
        "function": "Especificaciones de NPC autónomo: jerarquía de decisión, modelo funcional de datos, autoevaluación restringida"
      },
      {
        "path": "implementation/",
        "function": "Blueprints de implementación en C# y C++ (Unreal Engine 5), análisis de bugs, correcciones"
      },
      {
        "path": "patterns/",
        "function": "Registro de patrones recurrentes detectados en el dominio (por ejemplo, declaración de ejecución sin sustrato)"
      }
    ],
    "planned_documents": [
      {
        "document": "npc/wh-npc-utility-spec.json",
        "function": "Especificación funcional del NPC autónomo: jerarquía L1–L5, modelo de datos, fórmula de score",
        "status": "PROPUESTO"
      },
      {
        "document": "npc/wh-npc-decision-pipeline.json",
        "function": "Pipeline de ejecución del NPC: percepción, intención, jerarquía, validación, ejecución, retroalimentación, replanificación",
        "status": "PROPUESTO"
      },
      {
        "document": "implementation/wh-npc-ue5-blueprint.json",
        "function": "Blueprint de implementación C++/C# en Unreal Engine 5",
        "status": "PROPUESTO"
      },
      {
        "document": "implementation/wh-npc-ue5-bug-analysis.json",
        "function": "Análisis de bugs del blueprint: 10 confirmados, 2 adicionales",
        "status": "PROPUESTO"
      },
      {
        "document": "patterns/wh-declarative-simulation-pattern-gaming.json",
        "function": "Registro del patrón de declaración de ejecución sin sustrato detectado en el dominio",
        "status": "PROPUESTO"
      }
    ]
  },

  "epistemic_frontier": {
    "declaration": "Este dominio no declara que ningún NPC esté implementado en un motor de juego. No declara que el blueprint haya sido compilado, ejecutado ni probado en un entorno real. No declara validación empírica de ningún tipo.",
    "critical_rule": "La convergencia terminológica con el dominio cyberphysical/ (variables como intent_confidence, risk_level, context_decay, falsification_bias compartidas con la especificación RTL EPU) es terminológica, no ontológica. El sustrato de ejecución es diferente: software de gameplay vs. especificación de hardware digital. Cualquier análisis de este dominio debe limitarse a la lógica de software.",
    "applicable_invariants": [
      "MODEL_IS_NOT_SYSTEM",
      "SPECIFICATION_IS_NOT_IMPLEMENTATION",
      "REPRESENTATION_IS_NOT_ACTION",
      "OBSERVED_BEHAVIOR_IS_NOT_INTERNAL_ARCHITECTURE",
      "CAPABILITY_IS_NOT_EXECUTION",
      "SELF_EVALUATION_IS_NOT_INDEPENDENT_VALIDATION",
      "PROPOSAL_IS_NOT_CANON",
      "TECHNICAL_TERM_ACCEPTS_INTERPRETIVE_CONCORDANCE_ACROSS_LANGUAGES"
    ],
    "domain_specific_invariant": {
      "code": "TERMINOLOGICAL_CONVERGENCE_IS_NOT_SUBSTRATE_IDENTITY",
      "definition": "La coincidencia semántica o de vocabulario entre las variables de control de gameplay (C++/Behavior Tree) y las especificaciones de simulación o hardware (RTL/EPU) no constituye continuidad operativa ni identidad ontológica. Toda validación dentro de este dominio debe permanecer circunscrita al software de simulación e interfaz en motor de juego."
    }
  },

  "validation_registry": {
    "validator_entity": "GEMINI_SYSTEM_ARCHITECTURE_ENGINE",
    "verification_mode": "EPISTEMIC_BOUNDARIES_AND_SOFTWARE_LOGIC_AUDIT",
    "target_corpus": "WEB_HITERATION",
    "domain": "GAMING",
    "status": "DELIMITED_AND_VERIFIED",
    "scope_isolation": "SOFTWARE_LOGIC_ONLY",
    "timestamp": "2026-10-07T10:08:00-03:00",
    "checksum_token": "WH-GAMING-README-LOGIC-DELIMITED-2026"
  }
}

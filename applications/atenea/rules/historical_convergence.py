import json
from jsonschema import validate, ValidationError
from typing import Dict, Any

# 1. Cargamos las invariantes actualizadas (ahora son 6)
INVARIANTS = {
    "INV-01": "HISTORICAL_RELEVANCE_IS_NOT_INSTITUTIONAL_RECOGNITION",
    "INV-02": "TECHNOLOGICAL_SIMILARITY_IS_NOT_CAUSAL_INFLUENCE",
    "INV-03": "OPERATIONAL_CONVERGENCE_IS_NOT_UNIVERSAL_STANDARDIZATION",
    "INV-04": "HISTORICAL_INTERRUPTION_IS_NOT_TECHNOLOGICAL_INVALIDITY",
    "INV-05": "DOCUMENTARY_ABSENCE_IS_NOT_PROOF_OF_NONEXISTENCE",
    "INV-06": "PUBLISHED_IS_NOT_VALIDATED"
}

class HistoricalConvergenceAuditor:
    def __init__(self, schema_path: str):
        with open(schema_path, 'r', encoding='utf-8') as f:
            self.schema = json.load(f)

    def audit_case(self, case_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Valida el caso contra el Schema JSON y luego evalúa los sesgos.
        """
        # 1. Validación estructural
        try:
            validate(instance=case_data, schema=self.schema)
        except ValidationError as e:
            return {
                "protocol": "WH-HANTA-2026-001",
                "status": "SCHEMA_VALIDATION_FAILED",
                "error": e.message,
                "path": list(e.path)
            }

        # 2. Auditoría Epistémica
        evaluations = []
        is_aligned = True
        detected_biases = case_data.get("detected_biases", {})

        for inv_id, rule in INVARIANTS.items():
            passed = not detected_biases.get(inv_id, False)
            evaluations.append({
                "invariant_id": inv_id,
                "rule": rule,
                "status": "PASS" if passed else "FAIL"
            })
            if not passed:
                is_aligned = False

        return {
            "protocol": "WH-HANTA-2026-001",
            "project": case_data.get("reference_case", {}).get("project", "UNKNOWN"),
            "status": "STRUCTURALLY_ALIGNED" if is_aligned else "BIAS_DETECTED",
            "evaluations": evaluations,
            "historical_validation": "PENDING_FORMAL_VALIDATION"
        }

if __name__ == "__main__":
    # Ejemplo de uso
    auditor = HistoricalConvergenceAuditor("schemas/hanta_ruleset.schema.json")
    
    test_case = {
        "project": "CYBERSYN",
        "reference_case": {
            "project": "CYBERSYN",
            "country": "CHILE",
            "period": "1971-1973"
        },
        "detected_biases": {
            "INV-02": True,  # Asume influencia causal
            "INV-06": True   # Asume que lo publicado es verdad
        }
    }
    
    report = auditor.audit_case(test_case)
    print(json.dumps(report, indent=2))

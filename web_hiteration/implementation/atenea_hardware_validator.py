import os
import sys
import psutil
import json

class AteneaHardwareValidator:
    def __init__(self, contract_path):
        self.contract_path = contract_path
        self.compliance_status = "UNVERIFIED"

    def audit_environment(self):
        """Audita el entorno físico o virtual (Google Colab/Local) contra el contrato Atenea."""
        if not os.path.exists(self.contract_path):
            self.compliance_status = "CONTRACT_MISSING"
            return self.compliance_status, 0.0

        with open(self.contract_path, "r", encoding="utf-8") as f:
            contract = json.load(f)

        # Extracción de límites del contrato
        bounds_a = contract["hardware_bounds"]["engine_a_allocation"]
        bounds_b = contract["hardware_bounds"]["engine_b_allocation"]
        
        # OBSERVACIÓN LÓGICA: Si ALLOW_RESOURCE_SHARING es False y la política es STRICT_ISOLATION,
        # los motores deben ejecutarse simultáneamente. Por lo tanto, la RAM requerida es la SUMA,
        # no el máximo. (A menos que se ejecuten secuencialmente, pero la suma es más segura).
        total_required_ram_gb = bounds_a["required_ram_gb"] + bounds_b["required_ram_gb"]

        # Muestreo del hardware del sistema en tiempo real
        system_ram_gb = psutil.virtual_memory().total / (1024 ** 3)
        available_cores = os.cpu_count() or 1
        required_cores = bounds_a["max_threads"] + bounds_b["max_threads"]

        # Cálculo del índice de concordancia
        ram_ratio = min(system_ram_gb / total_required_ram_gb, 1.0)
        core_ratio = min(available_cores / required_cores, 1.0)
        concordance_index = (ram_ratio + core_ratio) / 2.0

        threshold = contract["verification_metrics"]["minimum_acceptance_threshold"]

        if concordance_index >= threshold:
            self.compliance_status = "STRUCTURALLY_ALIGNED"
        else:
            self.compliance_status = "ASYMMETRIC_DRIFT"

        return self.compliance_status, concordance_index

# Bloque de ejecución para pruebas locales
if __name__ == "__main__":
    # Ruta de ejemplo, ajusta según tu estructura local
    contract_file = "applications/atenea/wh-atenea-hardware-symmetric-contract.json"
    
    validator = AteneaHardwareValidator(contract_file)
    status, index = validator.audit_environment()
    
    print("=== ATENEA HARDWARE AUDIT ===")
    print(f"Status: {status}")
    print(f"Concordance Index: {index:.3f}")
    
    if status == "ASYMMETRIC_DRIFT":
        print("⚠️ ALERTA: El hardware no cumple con los requisitos del contrato.")
        print("Acción: El sistema bloquea la ejecución de la Fase E2.")
    else:
        print("✅ Hardware validado. Listo para la Fase E2.")

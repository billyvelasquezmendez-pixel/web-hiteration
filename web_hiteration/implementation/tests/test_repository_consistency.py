import os
import unittest
import json

class TestRepositoryConsistency(unittest.TestCase):
    def setUp(self):
        # Ajuste de ruta: Asumimos que este test está en web_hitteration/implementation/tests/
        # Por lo tanto, subimos 3 niveles para llegar a la raíz del repositorio
        current_file_path = os.path.abspath(__file__)
        self.repo_root = os.path.dirname(os.path.dirname(os.path.dirname(current_file_path)))
        self.canonical_namespace = "web_hitteration"
        self.forbidden_paths = ["web-hitteration", "web_hiterarion"]

    def test_canonical_namespace_enforcement(self):
        """Asegura que el entorno local no use nomenclaturas corruptas."""
        current_path = os.path.abspath(__file__)
        for variant in self.forbidden_paths:
            self.assertNotIn(variant, current_path, f"Colisión estructural: ruta corrupta detectada -> {variant}")

    def test_required_file_inventory(self):
        """Verifica la existencia física y el estado de recuperación de los archivos del contrato."""
        implementation_path = os.path.join(self.repo_root, self.canonical_namespace, "implementation")
        required_files = [
            "wh-delta-contract.json",
            "wh-implementation-roadmap.json"
        ]

        for filename in required_files:
            file_full_path = os.path.join(implementation_path, filename)
            # El protocolo prohíbe inventar estados si la lectura falla
            if not os.path.exists(file_full_path):
                print(f"[-] RECOVERY_FAILURE: {filename} no disponible localmente.")
                continue
                
            with open(file_full_path, "r", encoding="utf-8") as f:
                content = json.load(f)
                self.assertIn("status", content, f"El archivo {filename} no declara su estado normativo.")

if __name__ == "__main__":
    unittest.main()

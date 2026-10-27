import json

class DeltaEngineA:
    def __init__(self):
        self.namespace = "web_hitteration.delta_a"

    def process(self, data_input):
        # Aislamiento lógico para el Motor A
        result = f"[{self.namespace.upper()}] Procesando: {data_input} -> Delta_A_OK"
        return {"engine": self.namespace, "output": result}

class DeltaEngineB:
    def __init__(self):
        self.namespace = "web_hitteration.delta_b"

    def process(self, data_input):
        # Aislamiento lógico para el Motor B
        result = f"[{self.namespace.upper()}] Procesando: {data_input} -> Delta_B_OK"
        return {"engine": self.namespace, "output": result}

def run_demo():
    print("=== WEB_HITERATION: EJECUCIÓN DE LÍNEA BASE ===")

    # Simulación de datos de entrada separados por contrato
    payload_a = "Métrica_Alfa_2026"
    payload_b = "Métrica_Beta_2026"

    engine_a = DeltaEngineA()
    engine_b = DeltaEngineB()

    res_a = engine_a.process(payload_a)
    res_b = engine_b.process(payload_b)

    print(json.dumps(res_a, indent=2))
    print(json.dumps(res_b, indent=2))
    print("==============================================")

if __name__ == "__main__":
    run_demo()

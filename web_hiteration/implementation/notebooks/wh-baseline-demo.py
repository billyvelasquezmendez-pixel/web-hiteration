# WH-BASELINE-DEMO: DELTA ENGINE IMPLEMENTATION
# Protocol: WH-IMPLEMENTATION-TRACE-2026-10-26
# Status: PROPOSED_NOT_CANONICAL

def validate_input(value, name):
    if not (0 <= value <= 1):
        raise ValueError(f"{name} must be between 0 and 1. Received: {value}")

def engine_a_delta_prime(p1, p3, p5):
    """DELTA_ENGINE_A_WEIGHTED_COMPLEMENT"""
    validate_input(p1, "P1")
    validate_input(p3, "P3")
    validate_input(p5, "P5")
    return 0.4 * (1 - p1) + 0.4 * (1 - p3) + 0.2 * (1 - p5)

def engine_b_delta_prime(p1, sigma):
    """DELTA_ENGINE_B_COHERENCE_ADJUSTED"""
    validate_input(p1, "P1")
    validate_input(sigma, "sigma")
    return sigma * (1 - p1)

if __name__ == "__main__":
    print("--- WH BASELINE DEMO ---")
    p1, p3, p5 = 0.85, 0.75, 0.65
    sigma = 0.12
    
    print(f"Inputs: P1={p1}, P3={p3}, P5={p5}, sigma={sigma}")
    print(f"Engine A (Weighted Complement): {engine_a_delta_prime(p1, p3, p5):.4f}")
    print(f"Engine B (Coherence Adjusted): {engine_b_delta_prime(p1, sigma):.4f}")
    
    print("\n[NOTA EPISTEMICA] Ambos motores están implementados. Ninguno es canónico aún.")

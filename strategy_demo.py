from abc import ABC, abstractmethod

# -------------------------------------------------------------------------
# EL ANTES (Antipatrón: Acoplado a if/elif):
# def calcular_tarifa(tipo, km):
#     if tipo == "estandar": return 5.0 + (km * 2.0)
#     elif tipo == "pico": return 10.0 + (km * 3.5)
#     elif tipo == "nocturna": return 12.0 + (km * 4.0)
#     # Problema: cada nueva tarifa obliga a modificar esta función (viola Open/Closed).
# -------------------------------------------------------------------------

# 1. ESTRATEGIA (El contrato de los algoritmos)
class EstrategiaTarifa(ABC):
    @abstractmethod
    def calcular(self, distancia_km: float) -> float: pass

# 2. ALGORITMOS CONCRETOS
class TarifaEstandar(EstrategiaTarifa):
    def calcular(self, distancia_km: float) -> float:
        return 5.0 + (distancia_km * 2.0)

class TarifaHoraPico(EstrategiaTarifa):
    def calcular(self, distancia_km: float) -> float:
        return 10.0 + (distancia_km * 3.5)

# 3. CONTEXTO
class CalculadoraViaje:
    def __init__(self, estrategia: EstrategiaTarifa):
        self.estrategia = estrategia

    def cambiar_estrategia(self, nueva_estrategia: EstrategiaTarifa):
        self.estrategia = nueva_estrategia  # Cambio de algoritmo en caliente

    def cobrar(self, distancia_km: float):
        total = self.estrategia.calcular(distancia_km)
        print(f"Viaje {distancia_km} km | Total: Q{total:.2f}")

# DEMO
if __name__ == "__main__":
    viaje = CalculadoraViaje(TarifaEstandar())
    print("--- 1. Tarifa Normal ---")
    viaje.cobrar(10)

    print("\n--- 2. Cambio a Hora Pico (en ejecución) ---")
    viaje.cambiar_estrategia(TarifaHoraPico())
    viaje.cobrar(10)
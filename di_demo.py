from abc import ABC, abstractmethod

# -------------------------------------------------------------------------
# 1. EL CONTRATO (Abstracción)
# -------------------------------------------------------------------------
class PasarelaPago(ABC):
    @abstractmethod
    def procesar(self, monto: float) -> str:
        pass

# -------------------------------------------------------------------------
# 2. IMPLEMENTACIONES REALES / MOCKS
# -------------------------------------------------------------------------
class PasarelaStripe(PasarelaPago):
    def procesar(self, monto: float) -> str:
        return f"[PROD] Cobro exitoso de Q{monto:.2f} con Stripe"

class PasarelaMockPruebas(PasarelaPago):
    def procesar(self, monto: float) -> str:
        return f"[TEST] Cobro simulado de Q{monto:.2f} (sin tocar saldo real)"

# -------------------------------------------------------------------------
# 3. LÓGICA DE NEGOCIO (Recibe la dependencia por el constructor)
# -------------------------------------------------------------------------
class CheckoutServicio:
    # EL ANTES (acoplado): self.pasarela = PasarelaStripe()  <-- Mala práctica
    # EL DESPUÉS (inyección):
    def __init__(self, pasarela: PasarelaPago):
        self.pasarela = pasarela

    def confirmar_compra(self, total: float):
        resultado = self.pasarela.procesar(total)
        print(f"Checkout completado -> {resultado}")

# -------------------------------------------------------------------------
# DEMO
# -------------------------------------------------------------------------
if __name__ == "__main__":
    print("=== 1. EN PRODUCCIÓN ===")
    checkout_prod = CheckoutServicio(PasarelaStripe())
    checkout_prod.confirmar_compra(150.00)

    print("\n=== 2. EN TESTS AUTOMATIZADOS (Cero costos de API) ===")
    checkout_test = CheckoutServicio(PasarelaMockPruebas())
    checkout_test.confirmar_compra(150.00)
    
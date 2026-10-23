from abc import ABC, abstractmethod

# -------------------------------------------------------------------------
# 1. PRODUCTO (Interfaz / Contrato común)
# -------------------------------------------------------------------------
class Notificador(ABC):
    @abstractmethod
    def enviar(self, destinatario: str, mensaje: str) -> str:
        """Contrato obligatorio para todos los notificadores."""
        pass

# -------------------------------------------------------------------------
# 2. PRODUCTOS CONCRETOS
# -------------------------------------------------------------------------
class NotificadorEmail(Notificador):
    def enviar(self, destinatario: str, mensaje: str) -> str:
        return f"[EMAIL] Enviado a {destinatario}: '{mensaje}'"

class NotificadorSMS(Notificador):
    def enviar(self, destinatario: str, mensaje: str) -> str:
        return f"[SMS] Enviado a {destinatario}: '{mensaje}'"

class NotificadorWhatsApp(Notificador):
    def enviar(self, destinatario: str, mensaje: str) -> str:
        return f"[WHATSAPP] Enviado a {destinatario}: '{mensaje}'"

# -------------------------------------------------------------------------
# 3. LA FÁBRICA (Centraliza la creación)
# -------------------------------------------------------------------------
class NotificadorFactory:
    @staticmethod
    def crear_notificador(canal: str) -> Notificador:
        canal_limpio = canal.lower().strip()
        if canal_limpio == "email":
            return NotificadorEmail()
        elif canal_limpio == "sms":
            return NotificadorSMS()
        elif canal_limpio == "whatsapp":
            return NotificadorWhatsApp()
        else:
            raise ValueError(f"Canal no soportado: {canal}")

# -------------------------------------------------------------------------
# DEMO
# -------------------------------------------------------------------------
if __name__ == "__main__":
    print("=== DEMOSTRACIÓN PATRÓN FACTORY ===")
    
    canales = ["email", "sms", "whatsapp"]
    
    for canal in canales:
        # El cliente pide una instancia sin acoplarse a la clase concreta
        servicio = NotificadorFactory.crear_notificador(canal)
        resultado = servicio.enviar("cliente_101", "Tu pedido va en camino")
        print(f"Canal '{canal}' -> {resultado}")
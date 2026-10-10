import sqlite3
from abc import ABC, abstractmethod

# 1. CONTRATO
class UsuarioRepository(ABC):
    @abstractmethod
    def guardar(self, usuario: dict): pass

    @abstractmethod
    def obtener_por_id(self, user_id: int) -> dict: pass

# 2. IMPLEMENTACIÓN A: Memoria (rápida, para tests)
class UsuarioRepositoryMemoria(UsuarioRepository):
    def __init__(self):
        self._tabla = {}

    def guardar(self, usuario: dict):
        self._tabla[usuario["id"]] = usuario
        print(f"[MEMORIA] Guardado: {usuario['nombre']}")

    def obtener_por_id(self, user_id: int):
        return self._tabla.get(user_id)

# 3. IMPLEMENTACIÓN B: SQLite real (en memoria :memory:, sin archivos basura)
class UsuarioRepositorySQLite(UsuarioRepository):
    def __init__(self):
        self._con = sqlite3.connect(":memory:")
        self._con.execute("CREATE TABLE usuarios (id INT PRIMARY KEY, nombre TEXT, rol TEXT)")

    def guardar(self, usuario: dict):
        self._con.execute("INSERT OR REPLACE INTO usuarios VALUES (?, ?, ?)",
                          (usuario["id"], usuario["nombre"], usuario["rol"]))
        print(f"[SQLITE] Guardado en BD: {usuario['nombre']}")

    def obtener_por_id(self, user_id: int):
        cursor = self._con.execute("SELECT id, nombre, rol FROM usuarios WHERE id = ?", (user_id,))
        fila = cursor.fetchone()
        return {"id": fila[0], "nombre": fila[1], "rol": fila[2]} if fila else None

# 4. SERVICIO DE NEGOCIO (Desacoplado del motor de datos)
class UsuarioServicio:
    def __init__(self, repo: UsuarioRepository):  # <-- Nota: Usa Inyección de Dependencias
        self.repo = repo

    def registrar(self, user_id: int, nombre: str, rol: str):
        if not nombre.strip():
            raise ValueError("Nombre obligatorio")
        self.repo.guardar({"id": user_id, "nombre": nombre, "rol": rol})

    def consultar(self, user_id: int):
        user = self.repo.obtener_por_id(user_id)
        return f"Encontrado: {user['nombre']} [{user['rol']}]" if user else "No existe"

# DEMO: El mismo servicio funciona con dos motores distintos
if __name__ == "__main__":
    for repo in (UsuarioRepositoryMemoria(), UsuarioRepositorySQLite()):
        print(f"--- Probando con {repo.__class__.__name__} ---")
        servicio = UsuarioServicio(repo)
        servicio.registrar(1, "Luis David Castro", "Admin")
        print(servicio.consultar(1), "\n")
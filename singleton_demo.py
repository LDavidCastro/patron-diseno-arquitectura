class SesionUsuario:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        # Si la instancia no existe en memoria, se crea por única vez
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.usuario_activo = None
            cls._instancia.token = None
        return cls._instancia

    def iniciar_sesion(self, nombre_usuario: str, token: str):
        self.usuario_activo = nombre_usuario
        self.token = token

    def cerrar_sesion(self):
        self.usuario_activo = None
        self.token = None


# -------------------------------------------------------------------------
# DEMO
# -------------------------------------------------------------------------
if __name__ == "__main__":
    print("=== 1. PANTALLA DE LOGIN: Inicia sesión el usuario ===")
    modulo_login = SesionUsuario()
    modulo_login.iniciar_sesion("ldavid_castro", "JWT_XYZ_12345")
    print(f"Login guardó -> Usuario: {modulo_login.usuario_activo} | Token: {modulo_login.token}")

    print("\n=== 2. OTRA PANTALLA (PERFIL): Accede a los mismos datos ===")
    modulo_perfil = SesionUsuario()
    print(f"Perfil leyó -> Usuario: {modulo_perfil.usuario_activo} | Token: {modulo_perfil.token}")

    print("\n=== 3. VERIFICACIÓN DE IDENTIDAD EN MEMORIA ===")
    es_la_misma = modulo_login is modulo_perfil
    print(f"¿Ambas variables apuntan exactamente al mismo objeto en RAM?: {es_la_misma}")
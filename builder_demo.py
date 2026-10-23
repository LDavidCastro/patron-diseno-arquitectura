# -------------------------------------------------------------------------
# 1. PRODUCTO COMPLEJO
# -------------------------------------------------------------------------
class Reporte:
    def __init__(self):
        self.titulo = None
        self.encabezado = None
        self.cuerpo = []
        self.pie_pagina = None
        self.formato = "Texto Plano"

    def __str__(self):
        contenido = [
            f"=== {self.titulo} (Formato: {self.formato}) ===",
            f"Encabezado: {self.encabezado or 'Sin encabezado'}",
            f"Cuerpo: {', '.join(self.cuerpo) if self.cuerpo else 'Sin datos'}",
            f"Pie de página: {self.pie_pagina or 'Sin pie de página'}",
            "=" * 45
        ]
        return "\n".join(contenido)

# -------------------------------------------------------------------------
# 2. EL BUILDER (Construcción paso a paso con Fluent Interface)
# -------------------------------------------------------------------------
class ReporteBuilder:
    def __init__(self):
        self._reporte = Reporte()

    def set_titulo(self, titulo: str):
        self._reporte.titulo = titulo
        return self  # Retornar self permite encadenar métodos

    def set_encabezado(self, encabezado: str):
        self._reporte.encabezado = encabezado
        return self

    def agregar_seccion(self, seccion: str):
        self._reporte.cuerpo.append(seccion)
        return self

    def set_pie_pagina(self, pie_pagina: str):
        self._reporte.pie_pagina = pie_pagina
        return self

    def set_formato(self, formato: str):
        self._reporte.formato = formato
        return self

    def build(self) -> Reporte:
        # Validación obligatoria antes de entregar el producto terminado
        if not self._reporte.titulo:
            raise ValueError("El reporte requiere un título obligatoriamente.")
        return self._reporte

# -------------------------------------------------------------------------
# DEMO
# -------------------------------------------------------------------------
if __name__ == "__main__":
    print("=== DEMOSTRACIÓN PATRÓN BUILDER ===\n")

    # Caso 1: Reporte simple (solo título y cuerpo)
    reporte_rapido = (
        ReporteBuilder()
        .set_titulo("Ventas del Día")
        .agregar_seccion("Total facturado: Q4,500.00")
        .build()
    )
    print(reporte_rapido)
    print()

    # Caso 2: Reporte formal y completo (encadenando todos los pasos)
    reporte_gerencial = (
        ReporteBuilder()
        .set_titulo("Auditoría Mensual")
        .set_formato("PDF")
        .set_encabezado("Empresa: Distribuidora Maya S.A.")
        .agregar_seccion("Balance contable: Aprobado")
        .agregar_seccion("Auditoría de inventario: Sin anomalías")
        .set_pie_pagina("Generado automáticamente por el ERP")
        .build()
    )
    print(reporte_gerencial)
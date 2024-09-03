class Hervidor:
    def hervir_agua(self):
        print("Hirviendo agua...")


class Molino:
    def moler_cafe(self):
        print("Moliendo café...")


class Cafetera:
    def mezclar_agua_y_cafe(self):
        print("Mezclando agua y café...")


class FachadaCafetera:
    def __init__(self):
        self.hervidor = Hervidor()
        self.molino = Molino()
        self.cafetera = Cafetera()

    def preparar_cafe(self):
        self.hervidor.hervir_agua()
        self.molino.moler_cafe()
        self.cafetera.mezclar_agua_y_cafe()


# Uso simplificado del sistema a través de la fachada
cafetera = FachadaCafetera()
cafetera.preparar_cafe()

class Hervidor:
    def hervir_agua(self):
        print("Hirviendo agua...")


class Molino:
    def moler_cafe(self):
        print("Moliendo café...")


class Cafetera:
    def mezclar_agua_y_cafe(self):
        print("Mezclando agua y café...")


# Uso del sistema
hervidor = Hervidor()
molino = Molino()
cafetera = Cafetera()

hervidor.hervir_agua()
molino.moler_cafe()
cafetera.mezclar_agua_y_cafe()

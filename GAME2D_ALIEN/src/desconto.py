class IDesconto:
    def calcular(self, valor):
        raise NotImplementedError


class ICupom:
    def aplicar_cupom(self, codigo):
        raise NotImplementedError


class IVIP:
    def validar_usuario_vip(self, usuario):
        raise NotImplementedError


class DescontoNormal(IDesconto):
    def calcular(self, valor):
        return valor * 0.1


class DescontoVIP(IDesconto, ICupom, IVIP):
    def calcular(self, valor):
        return valor * 0.2

    def aplicar_cupom(self, codigo):
        return True

    def validar_usuario_vip(self, usuario):
        return usuario == "vip"


class DescontoPremium(IDesconto):
    def calcular(self, valor):
        return valor * 0.3


def aplicar_desconto(desconto: IDesconto, valor: float) -> float:
    return desconto.calcular(valor)


class Pedido:
    def __init__(self, desconto: IDesconto):
        self.desconto = desconto

    def total(self, valor):
        return valor - self.desconto.calcular(valor)


if __name__ == "__main__":
    valor = 100

    pedido_normal = Pedido(DescontoNormal())
    pedido_vip = Pedido(DescontoVIP())

    print("Normal:", pedido_normal.total(valor))
    print("VIP:", pedido_vip.total(valor))

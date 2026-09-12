class Pagamento:
    def __init__(self, pagador, comanda, forma, valor, data_pagamento, hora_pagamento):
        self.pagador = pagador
        self.comanda = comanda
        self.forma = forma
        self.valor = valor
        self.data_pagamento = data_pagamento
        self.hora_pagamento = hora_pagamento
    
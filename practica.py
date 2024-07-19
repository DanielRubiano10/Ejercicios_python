class Plan:
    _id_counter = 1
    
    def __init__(self, usuario, mes, plan, valor):
        self._id = Plan._id_counter
        Plan._id_counter += 1
        
        self.usuario = usuario
        self.mes = mes
        self.plan = plan
        self.valor = valor
        
    def describir(self):
        return f"ID: {self._id} - Usuario: {self.usuario}, Mes: {self.mes}, Plan: {self.plan}, Valor: {self.valor}"

class PlanBasico(Plan):
    def __init__(self, usuario, mes, valor):
        super().__init__(usuario, mes, "Básico", valor)
        self.duracion = 6
        
    def describir(self):
        return f"{super().describir()}, Tipo: Básico, Duración: {self.duracion} meses."

class PlanPremium(Plan):
    def __init__(self, usuario, mes, valor):
        super().__init__(usuario, mes, "Premium", valor)
        self.beneficios = "Acceso a comunicación en grupo privado"
        
    def describir(self):
        return f"{super().describir()}, Tipo: Premium, Beneficios: {self.beneficios}"

class PlanVip(Plan):
    def __init__(self, usuario, mes, valor):
        super().__init__(usuario, mes, "VIP", valor)
        self.acceso_exclusivo = "Entrenamientos directamente conmigo"
        
    def describir(self):
        return f"{super().describir()}, Tipo: VIP, Acceso Exclusivo: {self.acceso_exclusivo}"

def pedir_datos():
    usuario = input("Ingrese el nombre de su usuario: ")
    # Validar mes
    meses_validos = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    while True:
        mes = input("Ingrese el mes que tomó el plan: ").lower()
        if mes in meses_validos:
            break
        else:
            print("Por favor, ingrese un mes válido.")
    
    valor = float(input("Ingrese el valor del plan: "))
    return usuario, mes, valor

lista_planes = []  # Lista para almacenar los planes

for _ in range(2):
    usuario, mes, valor = pedir_datos()
    
    while True:
        tipo_plan = input("Ingrese el tipo de plan (basico, premium, vip): ").lower()  # Controlar mayúscula-minúscula
        if tipo_plan == "basico":
            nuevo_plan = PlanBasico(usuario, mes, valor)
            break
        elif tipo_plan == "premium":
            nuevo_plan = PlanPremium(usuario, mes, valor)
            break
        elif tipo_plan == "vip":
            nuevo_plan = PlanVip(usuario, mes, valor)
            break
        else:
            print("Tipo de plan inválido. Intente nuevamente.")
    
    lista_planes.append(nuevo_plan)

for plan in lista_planes:
    print(plan.describir())
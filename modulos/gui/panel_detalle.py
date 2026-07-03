import customtkinter as ctk
from modulos.expedientes import abrir_expediente


class PanelDetalle(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.cliente_actual = None

        self.grid_columnconfigure(1, weight=1)

        titulo = ctk.CTkLabel(
            self,
            text="INFORMACIÓN DEL CLIENTE",
            font=("Arial", 22, "bold")
        )
        titulo.grid(row=0, column=0, columnspan=2, pady=(20, 30))

        # RFC
        ctk.CTkLabel(
            self,
            text="RFC:",
            font=("Arial", 16, "bold")
        ).grid(row=1, column=0, padx=20, pady=10, sticky="w")

        self.lbl_rfc = ctk.CTkLabel(
            self,
            text="-",
            font=("Arial", 16)
        )
        self.lbl_rfc.grid(row=1, column=1, sticky="w")

        # Nombre
        ctk.CTkLabel(
            self,
            text="Nombre:",
            font=("Arial", 16, "bold")
        ).grid(row=2, column=0, padx=20, pady=10, sticky="w")

        self.lbl_nombre = ctk.CTkLabel(
            self,
            text="-",
            font=("Arial", 16)
        )
        self.lbl_nombre.grid(row=2, column=1, sticky="w")

        # Estado
        ctk.CTkLabel(
            self,
            text="Estado:",
            font=("Arial", 16, "bold")
        ).grid(row=3, column=0, padx=20, pady=10, sticky="w")

        self.lbl_estado = ctk.CTkLabel(
            self,
            text="ACTIVO",
            font=("Arial", 16)
        )
        self.lbl_estado.grid(row=3, column=1, sticky="w")

        # Botones

        self.btn_opinion = ctk.CTkButton(
            self,
            text="📄 Descargar Opinión"
        )
        self.btn_opinion.grid(row=10, column=0, columnspan=2, pady=(40, 10))

        self.btn_constancia = ctk.CTkButton(
            self,
            text="📄 Descargar Constancia"
        )
        self.btn_constancia.grid(row=11, column=0, columnspan=2, pady=10)

        self.btn_expediente = ctk.CTkButton(
            self,
            text="📁 Abrir Expediente",
            command=self.abrir_expediente
        )
        self.btn_expediente.grid(row=12, column=0, columnspan=2, pady=10)

    def mostrar_cliente(self, cliente):

        self.cliente_actual = cliente

        self.lbl_rfc.configure(text=cliente[1])
        self.lbl_nombre.configure(text=cliente[2])

    def abrir_expediente(self):

        if self.cliente_actual is None:
            return

        abrir_expediente(self.cliente_actual[1])
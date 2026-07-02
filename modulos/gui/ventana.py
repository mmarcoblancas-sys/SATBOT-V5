import customtkinter as ctk

from .encabezado import Encabezado
from .panel_clientes import PanelClientes


class VentanaPrincipal(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("SATBOT DESPACHO V5")

        self.geometry("1400x800")

        self.minsize(1200, 700)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # ==========================
        # ENCABEZADO
        # ==========================

        self.encabezado = Encabezado(self)

        self.encabezado.grid(
            row=0,
            column=0,
            sticky="ew"
        )

        # ==========================
        # CUERPO
        # ==========================

        self.cuerpo = ctk.CTkFrame(self)

        self.cuerpo.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=10,
            pady=10
        )

        self.cuerpo.grid_columnconfigure(0, weight=1)
        self.cuerpo.grid_columnconfigure(1, weight=3)
        self.cuerpo.grid_rowconfigure(0, weight=1)

        # ==========================
        # PANEL CLIENTES
        # ==========================

        self.panel_clientes = PanelClientes(
            self.cuerpo,
            self.mostrar_cliente
        )

        self.panel_clientes.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 10)
        )

        # ==========================
        # PANEL DERECHO
        # ==========================

        self.panel_detalle = ctk.CTkFrame(self.cuerpo)

        self.panel_detalle.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.lbl_info = ctk.CTkLabel(
            self.panel_detalle,
            text="Seleccione un cliente",
            font=("Arial", 22, "bold")
        )

        self.lbl_info.pack(pady=30)

    # ===================================

    # ===================================

    def mostrar_cliente(self, cliente):

        print("MOSTRAR:", cliente)

        self.lbl_info.configure(
            text=f"RFC: {cliente[1]}\n\nNombre: {cliente[2]}"
        )

        self.update_idletasks()
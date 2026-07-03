import customtkinter as ctk

from .encabezado import Encabezado
from .panel_clientes import PanelClientes
from .panel_detalle import PanelDetalle


class VentanaPrincipal(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("SATBOT DESPACHO V5")
        self.geometry("1400x800")
        self.minsize(1200, 700)

        # -----------------------------
        # Configuración de la ventana
        # -----------------------------
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # -----------------------------
        # Encabezado
        # -----------------------------
        self.encabezado = Encabezado(self)
        self.encabezado.grid(
            row=0,
            column=0,
            sticky="ew"
        )

        # -----------------------------
        # Cuerpo principal
        # -----------------------------
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

        # -----------------------------
        # Panel de clientes
        # -----------------------------
        self.panel_clientes = PanelClientes(
            self.cuerpo,
            callback_cliente=self.mostrar_cliente
        )

        self.panel_clientes.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 10)
        )

        # -----------------------------
        # Panel de detalle
        # -----------------------------
        self.panel_detalle = PanelDetalle(self.cuerpo)

        self.panel_detalle.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

    # =====================================

    def mostrar_cliente(self, cliente):

        print("CLIENTE SELECCIONADO:", cliente)

        self.panel_detalle.mostrar_cliente(cliente)
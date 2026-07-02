import customtkinter as ctk
from modulos.clientes import obtener_clientes

# ---------------- CONFIGURACIÓN ---------------- #

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class SATBOT:

    def __init__(self):

        self.ventana = ctk.CTk()

        self.ventana.title("SATBOT DESPACHO V5")
        self.ventana.geometry("1400x800")

        # ======== CONFIGURAR GRID PRINCIPAL ========

        self.ventana.grid_columnconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(1, weight=3)
        self.ventana.grid_rowconfigure(1, weight=1)

        # ========= ENCABEZADO =========

        self.encabezado = ctk.CTkFrame(
            self.ventana,
            height=70,
            corner_radius=0
        )

        self.encabezado.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="nsew"
        )

        self.titulo = ctk.CTkLabel(
            self.encabezado,
            text="SATBOT DESPACHO V5",
            font=("Arial", 28, "bold")
        )

        self.titulo.pack(pady=20)

        # ========= PANEL IZQUIERDO =========

        self.panel_clientes = ctk.CTkFrame(
            self.ventana,
            width=300
        )

        self.panel_clientes.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=10,
            pady=10
        )

        self.lbl_clientes = ctk.CTkLabel(
            # ==========================
# LISTA DE CLIENTES
# ==========================

self.lista_clientes = ctk.CTkTextbox(
    self.panel_clientes,
    width=260,
    height=550
)

self.lista_clientes.pack(
    padx=10,
    pady=10,
    fill="both",
    expand=True
)

clientes = obtener_clientes()

for cliente in clientes:

    self.lista_clientes.insert(
        "end",
        f"{cliente['nombre']}\n"
    )

self.lista_clientes.configure(
    state="disabled"
)
            self.panel_clientes,
            text="CLIENTES",
            font=("Arial", 20, "bold")
        )

        self.lbl_clientes.pack(pady=15)

        # ========= PANEL DERECHO =========

        self.panel_principal = ctk.CTkFrame(
            self.ventana
        )

        self.panel_principal.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=10,
            pady=10
        )

        self.lbl_info = ctk.CTkLabel(
            self.panel_principal,
            text="INFORMACIÓN DEL CLIENTE",
            font=("Arial", 22, "bold")
        )

        self.lbl_info.pack(pady=20)

        self.ventana.mainloop()
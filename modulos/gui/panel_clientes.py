import customtkinter as ctk

from modulos.clientes import ClienteDAO


class PanelClientes(ctk.CTkFrame):

    def __init__(self, master, callback_cliente=None):

        super().__init__(master, width=300)

        self.dao = ClienteDAO()

        self.callback_cliente = callback_cliente

        self.grid_rowconfigure(2, weight=1)

        # ------------------------
        # Título
        # ------------------------

        self.lbl_titulo = ctk.CTkLabel(
            self,
            text="CLIENTES",
            font=("Arial", 22, "bold")
        )

        self.lbl_titulo.grid(
            row=0,
            column=0,
            padx=15,
            pady=(15, 5),
            sticky="w"
        )

        # ------------------------
        # Buscador
        # ------------------------

        self.buscar_var = ctk.StringVar()

        self.entry_buscar = ctk.CTkEntry(
            self,
            textvariable=self.buscar_var,
            placeholder_text="Buscar cliente..."
        )

        self.entry_buscar.grid(
            row=1,
            column=0,
            padx=15,
            pady=5,
            sticky="ew"
        )

        self.entry_buscar.bind(
            "<KeyRelease>",
            self.buscar_clientes
        )

        # ------------------------
        # Lista
        # ------------------------

        self.lista = ctk.CTkScrollableFrame(self)

        self.lista.grid(
            row=2,
            column=0,
            padx=15,
            pady=10,
            sticky="nsew"
        )

        self.cargar_clientes()

    # ======================================

    def limpiar_lista(self):

        for widget in self.lista.winfo_children():
            widget.destroy()

    # ======================================

    def cargar_clientes(self):

        self.limpiar_lista()

        clientes = self.dao.obtener_clientes()

        for cliente in clientes:

            boton = ctk.CTkButton(

                self.lista,

                text=cliente[2],

                anchor="w",

                command=lambda c=cliente: self.seleccionar(c)

            )

            boton.pack(
                fill="x",
                padx=5,
                pady=2
            )

    # ======================================

    def buscar_clientes(self, event=None):

        texto = self.buscar_var.get()

        self.limpiar_lista()

        clientes = self.dao.buscar(texto)

        for cliente in clientes:

            boton = ctk.CTkButton(

                self.lista,

                text=cliente[2],

                anchor="w",

                command=lambda c=cliente: self.seleccionar(c)

            )

            boton.pack(
                fill="x",
                padx=5,
                pady=2
            )

    # ======================================

    # ======================================

    def seleccionar(self, cliente):

        print("CLICK:", cliente)

        if self.callback_cliente:
            self.callback_cliente(cliente)
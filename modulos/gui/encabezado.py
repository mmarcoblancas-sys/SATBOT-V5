import customtkinter as ctk


class Encabezado(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master, height=70)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        titulo = ctk.CTkLabel(
            self,
            text="SATBOT DESPACHO V5",
            font=("Arial", 30, "bold")
        )

        usuario = ctk.CTkLabel(
            self,
            text="👤 Marco Blancas",
            font=("Arial", 16)
        )

        titulo.grid(row=0, column=0, padx=20, pady=15)

        usuario.grid(row=0, column=1, padx=20)
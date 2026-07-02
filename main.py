import customtkinter as ctk

from modulos.gui.ventana import VentanaPrincipal

ctk.set_appearance_mode("light")

ctk.set_default_color_theme("blue")

app = VentanaPrincipal()

app.mainloop()
from tkinter import ttk as tk

import ttkbootstrap as ttkbots


class TelaTest():
    def __init__(self, master):
        self.janelaPrincipal = master



        b1 = tk.Button(self.janelaPrincipal, text="Submit", style='success.TButton')
        b1.pack(side='left', padx=5, pady=10) 
        b2 = tk.Button(self.janelaPrincipal, text="Submit", style='success.Outline.TButton')
        b2.pack(side='left', padx=5, pady=10) 










style = ttkbots.Style('cyborg')
janela = style.master
TelaTest(janela)
janela.mainloop()



# Atualmente, os temas predefinidos disponíveis incluem:

# luz
# cosmo - flatly - journal - literal - lumen - minty - pulse - sandstone - united - yeti

# escuro
# cyborg - darkly - solar - super-herói



# Tipos de botões 

# primary.TButton

# secondary.TButton

# success.TButton

# info.TButton

# warning.TButton

# danger.TButton

# success.TButton

# Outline                                          para deixar transparente
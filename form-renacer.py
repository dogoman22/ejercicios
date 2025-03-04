import tkinter as tk

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
from tkinter import ttk

# Datos
municipios = {
    "25 de Mayo": {"seccion": "Séptima", "intendente": "Hernán Ralinqueo", "poblacion": 30000, "frente": "Unión Por la Patria"},
    "Adolfo Alsina": {"seccion": "Adolfo Alsina", "intendente": "David Hirtz", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Adolfo Gonzales Chaves": {"seccion": "Adolfo Gonzales Chaves", "intendente": "Marcelo Santillán", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Alberti": {"seccion": "Alberti", "intendente": "Germán Lago", "poblacion": 10000, "frente": "Juntos por el Cambio", },
    "Almirante Brown": {"seccion": "Tercera", "intendente": "Mariano Cascallares", "poblacion": 600000, "frente": "Unión Por la Patria", },
    "Arrecifes": {"seccion": "Arrecifes", "intendente": "Javier Olaeta", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Avellaneda": {"seccion": "Tercera", "intendente": "Jorge Ferraresi", "poblacion": 300000, "frente": "Unión Por la Patria", },
    "Ayacucho": {"seccion": "Quinta", "intendente": "Emilio Cordonnier", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Azul": {"seccion": "Séptima", "intendente": "Nelson Sombra", "poblacion": 60000, "frente": "Juntos por el Cambio", },
    "Bahía Blanca": {"seccion": "Sexta", "intendente": "Federico Susbielles", "poblacion": 300000, "frente": "Unión Por la Patria", },
    "Balcarce": {"seccion": "Quinta", "intendente": "Esteban Reino", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Baradero": {"seccion": "Segunda", "intendente": "Esteban Sanzio", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Benito Juárez": {"seccion": "Benito Juárez", "intendente": "Julio Marini", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Berazategui": {"seccion": "Tercera", "intendente": "Juan José Mussi", "poblacion": 400000, "frente": "Unión Por la Patria", },
    "Berisso": {"seccion": "Tercera", "intendente": "Fabian Cagliardi", "poblacion": 100000, "frente": "Unión Por la Patria", },
    "Bolívar": {"seccion": "Séptima", "intendente": "Marcos Pisano", "poblacion": 30000, "frente": "Unión Por la Patria", },
    "Brandsen": {"seccion": "Brandsen", "intendente": "Daniel Cappelletti", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Bragado": {"seccion": "Bragado", "intendente": "Vicente Gatica", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Campana": {"seccion": "Campana", "intendente": "Sebastián Abella", "poblacion": 100000, "frente": "Juntos por el Cambio", },
    "Cañuelas": {"seccion": "Cañuelas", "intendente": "Marisa Fassi", "poblacion": 100000, "frente": "Unión Por la Patria", },
    "Capitán Sarmiento": {"seccion": "Segunda", "intendente": "Javier Iguacel", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Carlos Casares": {"seccion": "Carlos Casares", "intendente": "Walter Torchio", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Carlos Tejedor": {"seccion": "Carlos Tejedor", "intendente": "Raúl Sala", "poblacion": 10000, "frente": "Juntos por el Cambio", },
    "Carmen de Areco": {"seccion": "Segunda", "intendente": "Iván Villagrán", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Castelli": {"seccion": "Quinta", "intendente": "Francisco Echarren", "poblacion": 30000, "frente": "Unión Por la Patria", },
    "Chacabuco": {"seccion": "Chacabuco", "intendente": "Víctor Aiola", "poblacion": 60000, "frente": "Juntos por el Cambio", },
    "Chascomús": {"seccion": "Quinta", "intendente": "Javier Gastón", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Chivilcoy": {"seccion": "Chivilcoy", "intendente": "Guillermo Britos", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Colón": {"seccion": "Segunda", "intendente": "Ricardo Casi", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Coronel Dorrego": {"seccion": "Coronel Dorrego", "intendente": "Raúl Reyes", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Coronel Pringles": {"seccion": "Coronel Pringles", "intendente": "Carlos Berterret", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Coronel Rosales": {"seccion": "Coronel Rosales", "intendente": "Mariano Uset", "poblacion": 60000, "frente": "Juntos por el Cambio", },
    "Coronel Suárez": {"seccion": "Coronel Suárez", "intendente": "Ricardo Móccero", "poblacion": 60000, "frente": "Juntos por el Cambio", },
    "Daireaux": {"seccion": "Daireaux", "intendente": "Alejandro Acerbo", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Dolores": {"seccion": "Dolores", "intendente": "Camilo Etchevarren", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Ensenada": {"seccion": "Ensenada", "intendente": "Mario Secco", "poblacion": 300000, "frente": "Unión Por la Patria", },
    "Escobar": {"seccion": "Escobar", "intendente": "Ariel Sujarchuk", "poblacion": 300000, "frente": "Unión Por la Patria", },
    "Esteban Echeverría": {"seccion": "Esteban Echeverría", "intendente": "Fernando Gray", "poblacion": 300000, "frente": "Unión Por la Patria", },
    "Exaltación de la Cruz": {"seccion": "Exaltación de la Cruz", "intendente": "Diego Nanni", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Ezeiza": {"seccion": "Ezeiza", "intendente": "Alejandro Granados", "poblacion": 300000, "frente": "Unión Por la Patria", },
    "Florencio Varela": {"seccion": "Florencio Varela", "intendente": "Andrés Watson", "poblacion": 300000, "frente": "Unión Por la Patria", },
    "Florentino Ameghino": {"seccion": "Florentino Ameghino", "intendente": "Caldos", "poblacion": 10000, "frente": "Juntos por el Cambio", },
    "General Alvarado": {"seccion": "General Alvarado", "intendente": "Sebastián Ianantuony", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "General Alvear": {"seccion": "General Alvear", "intendente": "Ramon Capra", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "General Arenales": {"seccion": "General Arenales", "intendente": "Eduardo Campana", "poblacion": 10000, "frente": "Juntos por el Cambio", },
    "General Belgrano": {"seccion": "General Belgrano", "intendente": "Osvaldo Dinapoli", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "General Guido": {"seccion": "General Guido", "intendente": "Aníbal Loubet", "poblacion": 10000, "frente": "Juntos por el Cambio", },
    "General La Madrid": {"seccion": "General La Madrid", "intendente": "Martín Randazzo", "poblacion": 10000, "frente": "Juntos por el Cambio", },
    "General Lavalle": {"seccion": "General Lavalle", "intendente": "María José Rodríguez", "poblacion": 10000, "frente": "Juntos por el Cambio", },
    "General Las Heras": {"seccion": "General Las Heras", "intendente": "Alejandro Ceccato", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "General Madariaga": {"seccion": "General Madariaga", "intendente": "Esteban Santoro", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "General Paz": {"seccion": "General Paz", "intendente": "Juan Manuel Álvarez", "poblacion": 10000, "frente": "Juntos por el Cambio", },
    "General Pinto": {"seccion": "General Pinto", "intendente": "Jorge Zavatarelli", "poblacion": 10000, "frente": "Juntos por el Cambio", },
    "General Pueyrredón": {"seccion": "General Pueyrredón", "intendente": "Guillermo Montenegro", "poblacion": 600000, "frente": "Juntos por el Cambio", },
    "General Rodríguez": {"seccion": "General Rodríguez", "intendente": "Mauro García", "poblacion": 100000, "frente": "Unión Por la Patria", },
    "General Viamonte": {"seccion": "General Viamonte", "intendente": "Franco Flexas", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "General Villegas": {"seccion": "General Villegas", "intendente": "Eduardo Campana", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Guaminí": {"seccion": "Guaminí", "intendente": "José Nobre Ferreira", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Hipólito Yrigoyen": {"seccion": "Hipolito Yrigoyen", "intendente": "Jorge Cortes", "poblacion": 10000, "frente": "Juntos por el Cambio", },
    "Hurlingham": {"seccion": "Hurlingham", "intendente": "Damián Selci", "poblacion": 300000, "frente": "Unión Por la Patria", },
    "Ituzaingó": {"seccion": "Ituzaingó", "intendente": "Alberto Descalzo", "poblacion": 300000, "frente": "Unión Por la Patria", },
    "José C. Paz": {"seccion": "José C. Paz", "intendente": "Mario Ishii", "poblacion": 300000, "frente": "Unión Por la Patria", },
    "Junín": {"seccion": "Junín", "intendente": "Pablo Petrecca", "poblacion": 100000, "frente": "Juntos por el Cambio", },
    "La Costa": {"seccion": "La Costa", "intendente": "Cristian Cardozo", "poblacion": 100000, "frente": "Unión Por la Patria", },
    "La Matanza": {"seccion": "La Matanza", "intendente": "Fernando Espinoza", "poblacion": 3000000, "frente": "Unión Por la Patria", },
    "La Plata": {"seccion": "Capital", "intendente": "Julio Alak", "poblacion": 800000, "frente": "Juntos por el Cambio"},
    "Lanús": {"seccion": "Lanús", "intendente": "Julián Alvarez", "poblacion": 400000, "frente": "Unión por la Patria", },
    "Laprida": {"seccion": "Laprida", "intendente": "Pablo Torres", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Las Flores": {"seccion": "Las Flores", "intendente": "Alberto Gelené", "poblacion": 30000, "frente": "Unión Por la Patria", }, 
    "Las Heras": {"seccion": "Las Heras", "intendente": "Javier Osuna", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Leandro N. Alem": {"seccion": "Leandro N. Alem", "intendente": "Alberto Conocchiari", "poblacion": 10000, "frente": "Juntos por el Cambio", },
    "Lezama": {"seccion": "Lezama", "intendente": "Natalia Nati", "poblacion": 10000, "frente": "Juntos por el Cambio", },
    "Lincoln": {"seccion": "Lincoln", "intendente": "Salvador Serenal", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Lobería": {"seccion": "Lobería", "intendente": "Juan José Fioramonti", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Lobos": {"seccion": "Lobos", "intendente": "Jorge Etcheverry", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Lomas de Zamora": {"seccion": "Lomas de Zamora", "intendente": "Federico Otermin", "poblacion": 600000, "frente": "Unión por la Patria", },
    "Luján": {"seccion": "Luján", "intendente": "Leonardo Boto", "poblacion": 100000, "frente": "Unión Por la Patria", },
    "Magdalena": {"seccion": "Magdalena", "intendente": "Gonzalo Peluso", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Maipú": {"seccion": "Maipú", "intendente": "Matías Rappallini", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Malvinas Argentinas": {"seccion": "Malvinas Argentinas", "intendente": "Leonardo Nardini", "poblacion": 400000, "frente": "Unión Por la Patria", },
    "Mar Chiquita": {"seccion": "Mar Chiquita", "intendente": "Walter Wichniwetzky", "poblacion": 30000, "frente": "Unión por la patria", },
    "Marcos Paz": {"seccion": "Marcos Paz", "intendente": "Ricardo Curutchet", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Mercedes": {"seccion": "Mercedes", "intendente": "Juan Ustarroz", "poblacion": 30000, "frente": "Unión Por la Patria", },
    "Merlo": {"seccion": "Merlo", "intendente": "Gustavo Menéndez", "poblacion": 500000, "frente": "Unión Por la Patria", },
    "Monte": {"seccion": "Monte", "intendente": "José Castro", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Monte Hermoso": {"seccion": "Monte Hermoso", "intendente": "Alejandro Dichiara", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Moreno": {"seccion": "Moreno", "intendente": "Mariel Fernández", "poblacion": 500000, "frente": "Unión Por la Patria", },
    "Morón": {"seccion": "Morón", "intendente": "Lucas Ghi", "poblacion": 300000, "frente": "Unión Por la Patria", },
    "Navarro": {"seccion": "Navarro", "intendente": "Facundo Diz", "poblacion": 30000, "frente": "Unión Po", },
    "Necochea": {"seccion": "Necochea", "intendente": "Arturo Rojas", "poblacion": 100000, "frente": "Juntos por el Cambio", },
    "Nueve de Julio": {"seccion": "Nueve de Julio", "intendente": "María José Gentile", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Olavarría": {"seccion": "Olavarría", "intendente": "Ezequiel Galli", "poblacion": 100000, "frente": "Juntos por el Cambio", },
    "Patagones": {"seccion": "Patagones", "intendente": "José Zara", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Pehuajó": {"seccion": "Pehuajó", "intendente": "Pablo Zurro", "poblacion": 30000, "frente": "Unión Por la Patria", },
    "Pellegrini": {"seccion": "Pellegrini", "intendente": "Guillermo Pacheco", "poblacion": 10000, "frente": "Juntos por el Cambio", },
    "Pergamino": {"seccion": "Pergamino", "intendente": "Javier Martínez", "poblacion": 100000, "frente": "Juntos por el Cambio", },
    "Pila": {"seccion": "Quinta", "intendente": "Gustavo Walker", "poblacion": 10000, "frente": "Juntos por el Cambio", },
    "Pilar": {"seccion": "Pilar", "intendente": "Federico Achával", "poblacion": 300000, "frente": "Unión Por la Patria", },
    "Pinamar": {"seccion": "Quinta", "intendente": "Martín Yeza", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Presidente Perón": {"seccion": "Presidente Perón", "intendente": "Blanca Cantero", "poblacion": 10000, "frente": "Juntos por el Cambio", },
    "Puan": {"seccion": "Sexta", "intendente": "Facundo Castelli", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Punta Indio": {"seccion": "Punta Indio", "intendente": "Hernán Yzurieta", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Quilmes": {"seccion": "Tercera", "intendente": "Mayra Mendoza", "poblacion": 600000, "frente": "Unión Por la Patria", },
    "Ramallo": {"seccion": "Segunda", "intendente": "Mauro Poletti", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Rauch": {"seccion": "Quinta", "intendente": "Maximiliano Suescun", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Rivadavia": {"seccion": "Rivadavia", "intendente": "Javier Reynoso", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Rojas": {"seccion": "Rojas", "intendente": "Cláudio Rossi", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Roque Pérez": {"seccion": "Roque Pérez", "intendente": "Juan Carlos Gasparini", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Saavedra": {"seccion": "Saavedra", "intendente": "Gustavo Notararigo", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Saladillo": {"seccion": "Saladillo", "intendente": "José Luis Salomón", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Salliqueló": {"seccion": "Salliqueló", "intendente": "Jorge Hernández", "poblacion": 10000, "frente": "Juntos por el Cambio", },
    "Salto": {"seccion": "Salto", "intendente": "Ricardo Alessandro", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "San Andrés de Giles": {"seccion": "San Andrés de Giles", "intendente": "Carlos Puglelli", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "San Antonio de Areco": {"seccion": "San Antonio de Areco", "intendente": "Francisco Durañona", "poblacion": 30000, "frente": "Unión Por la Patria", },
    "San Cayetano": {"seccion": "San Cayetano", "intendente": "Miguel Gargaglione", "poblacion": 10000, "frente": "Juntos por el Cambio", },
    "San Fernando": {"seccion": "Primera", "intendente": "Juan Andreotti", "poblacion": 300000, "frente": "Unión Por la Patria", },
    "San Isidro": {"seccion": "Primera", "intendente": "Gustavo Posse", "poblacion": 300000, "frente": "Juntos por el Cambio", },
    "San Miguel": {"seccion": "Primera", "intendente": "Jaime Méndez", "poblacion": 300000, "frente": "Juntos por el Cambio", },
    "San Nicolás": {"seccion": "Segunda", "intendente": "Manuel Passaglia", "poblacion": 100000, "frente": "Juntos por el Cambio", },
    "San Pedro": {"seccion": "San Pedro", "intendente": "Cecilio Salazar", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "San Vicente": {"seccion": "San Vicente", "intendente": "Nicolás Mantegazza", "poblacion": 30000, "frente": "Unión Por la Patria", },
    "Suipacha": {"seccion": "Primera", "intendente": "Alejandro Federico", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Tandil": {"seccion": "Quinta", "intendente": "Miguel Lunghi", "poblacion": 100000, "frente": "Juntos por el Cambio", },
    "Tapalqué": {"seccion": "Tapalqué", "intendente": "Gustavo Cocconi", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Tigre": {"seccion": "Tigre", "intendente": "Julio Zamora", "poblacion": 400000, "frente": "Unión Por la Patria", },
    "Tordillo": {"seccion": "Tordillo", "intendente": "Héctor Olivera", "poblacion": 10000, "frente": "Juntos por el Cambio", },
    "Tornquist": {"seccion": "Tornquist", "intendente": "Sergio Bordoni", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Trenque Lauquen": {"seccion": "Trenque Lauquen", "intendente": "Miguel Fernández", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Tres Arroyos": {"seccion": "Tres Arroyos", "intendente": "Carlos Sánchez", "poblacion": 60000, "frente": "Juntos por el Cambio", },
    "Tres de Febrero": {"seccion": "Primera", "intendente": "Diego Valenzuela", "poblacion": 400000, "frente": "Juntos por el Cambio", },
    "Tres Lomas": {"seccion": "Tres Lomas", "intendente": "Roberto Álvarez", "poblacion": 10000, "frente": "Juntos por el Cambio", },
    "Vicente López": {"seccion": "Primera", "intendente": "Jorge Macri", "poblacion": 300000, "frente": "Juntos por el Cambio", },
    "Vill Gesell": {"seccion": "Quinta", "intendente": "Gustavo Barrera", "poblacion": 30000, "frente": "Unión Por la Patria", },
    "Villarino": {"seccion": "Sexta", "intendente": "Carlos Bevilacqua", "poblacion": 30000, "frente": "Juntos por el Cambio", },
    "Zárate": {"seccion": "Segunda", "intendente": "Osvaldo Cáffaro", "poblacion": 100000, "frente": "Juntos por el Cambio", }
    
    }

def actualizar_datos(event):
    municipio = combo_municipios.get()
    datos = municipios.get(municipio, {})
    seccion.set(datos.get("seccion", ""))
    intendente.set(datos.get("intendente", ""))
    poblacion.set(datos.get("poblacion", ""))
    frente.set(datos.get("frente", ""))

root = tk.Tk()
root.title("Formulario de Municipios")
root.geometry("500x400")

tk.Label(root, text="Seleccione un Municipio del Menú:").grid(row=0, column=0, padx=30, pady=30)
combo_municipios = ttk.Combobox(root, values=list(municipios.keys()))
combo_municipios.grid(row=0, column=1, padx=30, pady=30)
combo_municipios.bind("<<ComboboxSelected>>", actualizar_datos)

tk.Label(root, text="Sección Electoral:").grid(row=1, column=0, padx=30, pady=30)
seccion = tk.StringVar()
tk.Entry(root, textvariable=seccion, state='readonly').grid(row=1, column=1, padx=30, pady=30)

tk.Label(root, text="Intendente:").grid(row=2, column=0, padx=30, pady=30)
intendente = tk.StringVar()
tk.Entry(root, textvariable=intendente, state='readonly').grid(row=2, column=1, padx=30, pady=30)

tk.Label(root, text="Población:").grid(row=3, column=0, padx=30, pady=30)
poblacion = tk.StringVar()
tk.Entry(root, textvariable=poblacion, state='readonly').grid(row=3, column=1, padx=30, pady=30)

tk.Label(root, text="Frente Electoral:").grid(row=4, column=0, padx=30, pady=30)
frente = tk.StringVar()
tk.Entry(root, textvariable=frente, state='readonly').grid(row=4, column=1, padx=30, pady=30)



root.mainloop()


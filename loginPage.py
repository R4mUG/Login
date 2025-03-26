import datetime

import Loginddbb
import flet as ft

def main(page : ft.Page):
    page.title = "CONTROL USUARIOS"

    def abrir_selector(e):
        date_picker.open = True
        page.update()

    def seleccionar_fecha(e):
        fecha_txt.value = f'{date_picker.value.day}/{date_picker.value.month}/{date_picker.value.year}'
        page.update()

    #def get_tipos():
     #   lista_tipos = []
      #  lista_tipos.append(ft.dropdown.Option(text="Perenne", key="Perenne"))
       # lista_tipos.append(ft.dropdown.Option(text="Caduca", key="Caduca"))
        #return lista_tipos

    def crear_usuario(e):
        nombre = nombre_tf.value
        email = email_tf.value
        contrasena = contrasena_tf.value
        fecha_nacimiento = date_picker.value
        fecha_registro = date_picker.value
        Loginddbb.insertar_usuario(nombre, email, contrasena, fecha_nacimiento, fecha_registro)

    def volver(e):
        page.go("/consultas")


    #OBJETOS
    nombre_tf = ft.TextField(label="Nombre", width=300)
    email_tf = ft.TextField(label="Email", width=300)
    contrasena_tf = ft.TextField(label="Contrasena", width=300)


    date_picker = ft.DatePicker(on_change=seleccionar_fecha, value=datetime.datetime.now())
    fecha_txt = ft.Text(f'{date_picker.value.day}/{date_picker.value.month}/{date_picker.value.year}')
    volver_btn = ft.ElevatedButton(text="Volver", on_click=volver)

    columna_datos = ft.Column(
        controls=[ ft.Text("USUARIOS", size=40),
                   nombre_tf,
                   email_tf,
                   contrasena_tf,
                   fecha_txt,
                   ft.FilledButton("FECHA NACIMIENTO", on_click=abrir_selector),
                   fecha_txt,
                   ft.FilledButton("FECHA REGISTRO", on_click=abrir_selector),
                   ft.FilledButton("CREAR USUARIO", on_click=crear_usuario),
                   volver_btn
                   ],
    )

    page.overlay.append(date_picker)
    #page.add(columna_datos)
    return columna_datos
import flet as ft
import Loginddbb

def main(page: ft.Page):
    page.title = "Consultas"

    # Consultar y cargar todos los usuarios
    def consultar_usuarios():
        usuarios = Loginddbb.consultar_usuarios() # Esto son los datos
        cargar_tabla(usuarios)
        page.update()


    # Datos es la lista de usuarios
    def cargar_tabla(datos):
        tabla.rows = []
        for fila in datos:
            tabla.rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(str(fila[0]))), #ID
                ft.DataCell(ft.Text((fila[1]))), #Nombre
                ft.DataCell(ft.Text((fila[2]))), #Email
                ft.DataCell(ft.Text((fila[3]))), #Contrasena
                ft.DataCell(ft.Text((fila[4]))), #Rol
                ft.DataCell(ft.Text(str(fila[5]))),  #Fecha_nacimiento
                ft.DataCell(ft.Text(str(fila[6]))),  #Fecha_registro
                ft.DataCell(ft.Text(str(fila[7]))),  #Ultimo_Login
            ]))

    def buscar_usuarios(e):
        lista_usuarios = Loginddbb.consultar_usuarios_por_nombre(nombre_tf.value)
        cargar_tabla(lista_usuarios)
        page.update()

    def volver(e):
        page.go("/formulario")

    #OBJETOS
    nombre_tf = ft.TextField(label="Nombre", width=300)
    buscar_btn = ft.ElevatedButton("Buscar", width=300, on_click=buscar_usuarios)
    volver_btn = ft.ElevatedButton(text="Volver", on_click=volver)

    tabla = ft.DataTable(bgcolor="yellow",
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Email")),
            ft.DataColumn(ft.Text("Contrasena")),
            ft.DataColumn(ft.Text("Rol")),
            ft.DataColumn(ft.Text("Fecha_nacimiento")),
            ft.DataColumn(ft.Text("Fecha_registro")),
            ft.DataColumn(ft.Text("Ultimo_login")),
        ]
    )


    columna_datos = ft.Column(
        controls=[
            ft.Text("CONSULTAS", size=40),
            nombre_tf,
            buscar_btn,
            tabla,
            volver_btn
        ]
    )


    #page.add(columna_datos)
    consultar_usuarios()
    return columna_datos
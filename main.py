import flet as ft
import loginPage
import registroPage

def main(page: ft.Page):
    page.title = "APP USUARIOS"

    def route_change(e):
        page.views.clear()

        if page.route == "/formulario":
            page.views.append(
                ft.View(
                    route = "/formulario",
                    controls= [loginPage.main(page)]
                )
            )
        elif page.route == "/consultas":
            page.views.append(
                ft.View(
                    route="/consultas",
                    controls=[registroPage.main(page)]
                )
            )
        page.update()
    page.on_route_change = route_change
    page.go("/formulario")

if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER, port=30042)
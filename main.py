from turtle import bgcolor
import flet as ft

from app.tasas import tasas_de_cambio


async def obtener(e):
    await tasas_de_cambio(e)


def main(page: ft.Page):
        
    page.title = "XStore"
    page.padding = 20
    page.spacing= 0
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.navigation_bar = ft.NavigationBar(
        bgcolor='ffffff',
        surface_tint_color='ffffff',
        destinations=[
            ft.NavigationDestination(
                    icon=ft.icons.HOME, 
                    label="Home",
                    
                ),
            ft.NavigationDestination(
                    icon=ft.icons.SETTINGS, 
                    label="Setting",
                ),
        ]
    )

    i = ft.Image(
            '12.jpg',
            height=200,
            fit=ft.ImageFit.NONE,
            repeat=ft.ImageRepeat.NO_REPEAT,
            border_radius=ft.border_radius.all(10),
        )
    t = ft.Container(
        content=ft.Text(
            'Cambio de la moneda',
            size=20,
        ),
        alignment=ft.alignment.center
    )
    btn = ft.Container(
        content=ft.ElevatedButton(
            "ACTUALIZAR",
            style=ft.ButtonStyle(
                color="#adb5bd",
                bgcolor="#212529",
                overlay_color="#343a40",
                shape=ft.RoundedRectangleBorder(radius=5),
            ),
            on_click=obtener,
        ),
        alignment=ft.alignment.center
    )
    

    
    contenido = ft.Column(
        controls=[
            i,
            t,
            btn
        ],
    )

    page.add(contenido)


ft.app(target=main, assets_dir='assets')
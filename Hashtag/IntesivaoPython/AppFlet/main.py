import flet as ft


def main(page: ft.Page):
    page.bgcolor = "lightblueaccent"

    def add_afazer(e):
        page.add(ft.Checkbox(label=afazer.value))
        afazer.value = ""
        afazer.focus()
        afazer.update()

    afazer = ft.TextField(hint_text="Digite um afazer", width=200)

    l1 = ft.Row([
        afazer,
        ft.ElevatedButton("Adicionar", on_click=add_afazer)
    ])

    page.add(l1)


ft.app(target=main)

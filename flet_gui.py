import joblib
import warnings
import flet as ft


warnings.filterwarnings(action="ignore")
data = joblib.load("model_")


def main(page: ft.Page) -> None:
    page.window_height = 700
    page.window_width = 400

    def work(e):
        n1:int = int(num1.value)
        n2:int = int(num2.value)
        res:int = int(data.predict([[n1, n2]])[0])
        result.value = f"Result of {n1} + {n2} is {int(res)}"
        page.update()


    num1 = ft.TextField(label="Number 1")
    num2 = ft.TextField(label="Number 2")
    btn = ft.ElevatedButton(text="sum", on_click=work)
    result = ft.Text(color=ft.colors.GREEN)
    page.add(num1, num2, btn, result)

ft.app(target=main)
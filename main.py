import random
import time

import flet
from flet import (Column, Container, Page, Row, Slider, Stack, Text,
                  TextButton, colors, margin)


class SortingVisualizer:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.setup_page()
        self.visualizer()

    def setup_page(self) -> None:
        self.page.title = "Sorting Visualizer"
        self.page.window_width = 1280
        self.page.window_height = 720
        self.page.update()
        self.page.window_resizable = False
        self.page.update()

    def able_disable_during_sorting(self) -> None:
        controls_to_check = [
            self.gen_new_arr_btn,
            self.slider,
            self.bubble_sort_btn
        ]
        for control in controls_to_check:
            if control.disabled:
                control.disabled = False
            else:
                control.disabled = True
        self.page.update()

    def bubble_sort(self, e) -> None:
        pass

    def generate_new_array(self, e) -> None:
        self.to_sort_lines.content.controls.clear()
        for i in range(int(self.slider.value)):
            self.to_sort_lines.content.controls.append(
                Container(
                    width=10,
                    height=random.uniform(100, self.to_sort_lines.height),
                    bgcolor=colors.LIGHT_BLUE,
                    left=i * 15,
                )
            )
        self.to_sort_lines.update()

    def visualizer(self) -> None:
        self.t = Text()
        self.slider = Slider(value=10, min=10, max=84, divisions=74, label="{value}", on_change=self.generate_new_array)
        self.gen_new_arr_btn = TextButton(text="Generate New Array", on_click=self.generate_new_array)
        self.bubble_sort_btn = TextButton(text="Bubble Sort", on_click=self.bubble_sort)
        self.top_menu = Container(
            content=Row(
                controls=[
                    self.gen_new_arr_btn,
                    Text(value="Change Array Size & Sorting Speed"),
                    self.slider,
                    self.bubble_sort_btn,
                ]
            ),
            margin=margin.only(top=40)
        )
        self.to_sort_lines = Container(
            content=Stack(),
            width=self.page.window_width,
            height=self.page.window_height/2
        )
        self.page.add(
            Row(
                controls=[
                    self.top_menu,
                    self.t,
                ]
            ),
            self.to_sort_lines
        )
        self.generate_new_array(0)  # basically the arg can be anything since it's not used but due to the fact func is also called in on_click and on_change func needs to take event control as arg

if __name__ == "__main__":
    flet.app(name="Sorting Visualizer", target=SortingVisualizer)

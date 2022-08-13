import random
import time

import flet
from flet import (Column, Container, Page, Row, Slider, Stack, Text,
                  TextButton, alignment, colors, margin)


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

    def enable_disable_during_sorting(self) -> None:
        controls_to_check = [
            self.gen_new_arr_btn,
            self.slider,
            self.bubble_sort_btn,
            self.quick_sort_btn 
        ]
        for control in controls_to_check:
            if control.disabled:
                control.disabled = False
            else:
                control.disabled = True
        self.page.update()

    def partition(self, low, high) -> int:
        pivot = self.to_sort_lines.content.controls[high]
        (pivot.bgcolor, self.to_sort_lines.content.controls[low].bgcolor) = (colors.YELLOW, colors.YELLOW)
        self.to_sort_lines.content.update()
        i = low - 1

        for j in range(low, high):
            print(f"j: {j}")
            input("j loop")
            if self.to_sort_lines.content.controls[j].height <= pivot.height:
                i += 1
                print(f"i: {i}")
                self.to_sort_lines.content.controls[j].bgcolor = colors.GREEN
                self.to_sort_lines.content.update()
                time.sleep(1)
                (self.to_sort_lines.content.controls[i].bgcolor, self.to_sort_lines.content.controls[j].bgcolor) = (colors.LIGHT_BLUE, colors.LIGHT_BLUE)
                self.to_sort_lines.content.update()
                time.sleep(1)
                (self.to_sort_lines.content.controls[i].height, self.to_sort_lines.content.controls[j].height) = (self.to_sort_lines.content.controls[j].height, self.to_sort_lines.content.controls[i].height)
                self.to_sort_lines.content.update()
                time.sleep(1)
            else:
                self.to_sort_lines.content.controls[j].bgcolor = colors.RED
                self.to_sort_lines.content.update()
                time.sleep(1)
        input("last step")
        (self.to_sort_lines.content.controls[i + 1].height, self.to_sort_lines.content.controls[high].height) = (self.to_sort_lines.content.controls[high].height, self.to_sort_lines.content.controls[i + 1].height)
        self.to_sort_lines.content.update()
        time.sleep(1)
        if high == i+1:
            print("BANG BANG")
            time.sleep(3)
            self.to_sort_lines.content.controls[high].bgcolor = colors.PURPLE
        else:
            self.to_sort_lines.content.controls[high].bgcolor = colors.ORANGE
        self.to_sort_lines.content.controls[i + 1].bgcolor = colors.PURPLE
        self.to_sort_lines.content.update()
        return i + 1

    def quick_sort_vis(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort_vis(low, pi - 1)
            self.quick_sort_vis(pi + 1, high)
        elif low == high:
            print(f"ESSA low: {low} high: {high}")
            time.sleep(3)
            self.to_sort_lines.content.controls[low].bgcolor = colors.PURPLE
            self.to_sort_lines.content.update()
        else:
            print(f"low{low} > high{high}")

    def quick_sort(self, e) -> None:
        self.enable_disable_during_sorting()
        self.quick_sort_vis(0, len(self.to_sort_lines.content.controls)-1)
        self.enable_disable_during_sorting()
    
    def bubble_sort(self, e) -> None:
        self.enable_disable_during_sorting()
        for i in range(len(self.to_sort_lines.content.controls)):
            for j in range(len(self.to_sort_lines.content.controls)-1-i):
                # if the current element height is bigger than the next element height, swap them
                if self.to_sort_lines.content.controls[j].height > self.to_sort_lines.content.controls[j+1].height:
                    (self.to_sort_lines.content.controls[j].bgcolor, self.to_sort_lines.content.controls[j+1].bgcolor) = (colors.RED, colors.RED)
                    self.to_sort_lines.content.update()
                    time.sleep(0.01)
                    (self.to_sort_lines.content.controls[j].height, self.to_sort_lines.content.controls[j+1].height) = (self.to_sort_lines.content.controls[j+1].height, self.to_sort_lines.content.controls[j].height)
                    (self.to_sort_lines.content.controls[j].bgcolor, self.to_sort_lines.content.controls[j+1].bgcolor) = (colors.GREEN, colors.GREEN)
                    self.to_sort_lines.content.update()
                    time.sleep(0.01)
                else:
                    (self.to_sort_lines.content.controls[j].bgcolor, self.to_sort_lines.content.controls[j+1].bgcolor) = (colors.GREEN, colors.GREEN)
                    self.to_sort_lines.content.update()
                    time.sleep(0.01)
                (self.to_sort_lines.content.controls[j].bgcolor, self.to_sort_lines.content.controls[j+1].bgcolor) = (colors.LIGHT_BLUE, colors.LIGHT_BLUE)
                self.to_sort_lines.content.update()
            # each iteration, element with index [len(self.to_sort_lines.content.controls)-1-i] is always in the right position
            self.to_sort_lines.content.controls[len(self.to_sort_lines.content.controls)-1-i].bgcolor = colors.PURPLE
            self.to_sort_lines.content.update()
        self.enable_disable_during_sorting()

    def generate_new_array(self, e) -> None:
        self.to_sort_lines.content.controls.clear()
        for i in range(int(self.slider.value)):
            self.to_sort_lines.content.controls.append(
                Container(
                    width=10,
                    height=random.uniform(100, self.to_sort_lines.height),
                    bgcolor=colors.LIGHT_BLUE,
                    left=i * 15
                )
            )
        self.to_sort_lines.update()

    def visualizer(self) -> None:
        self.t = Text()
        self.slider = Slider(value=10, min=10, max=84, divisions=74, label="{value}", on_change=self.generate_new_array)
        self.gen_new_arr_btn = TextButton(text="Generate New Array", on_click=self.generate_new_array)
        self.bubble_sort_btn = TextButton(text="Bubble Sort", on_click=self.bubble_sort)
        self.quick_sort_btn = TextButton(text="Quick Sort", on_click=self.quick_sort)
        self.top_menu = Container(
            content=Row(
                controls=[
                    self.gen_new_arr_btn,
                    Text(value="Change Array Size & Sorting Speed"),
                    self.slider,
                    self.bubble_sort_btn,
                    self.quick_sort_btn
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
                ],
                # alignment="center"
            ),
            self.to_sort_lines
        )
        self.generate_new_array(0)  # basically the arg can be anything since it's not used but due to the fact func is also called in on_click and on_change func needs to take event control as arg

if __name__ == "__main__":
    flet.app(name="Sorting Visualizer", target=SortingVisualizer)

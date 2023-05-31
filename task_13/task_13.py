from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from random import randint
from kivy.config import Config
Config.set('graphics', 'width', '721')
Config.set('graphics', 'height', '721')


class Cell(Button):
    def __init__(self, **kwargs):
        super(Cell, self).__init__(**kwargs)
        self.is_mine = False
        self.is_flagged = False
        self.is_open = False
        self.mine_count = 0
        self.size_hint = (None, None)
        self.size = (100, 100)
        self.background_normal = 'button_3.png'

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and touch.button == 'right':
            self.toggle_flag()
            return True
        if self.collide_point(*touch.pos) and touch.button == 'left' and self.is_flagged:
            return False
        return super(Cell, self).on_touch_down(touch)

    def toggle_flag(self):
        self.is_flagged = not self.is_flagged
        if self.is_flagged:
            self.background_normal = 'flag.png'
        else:
            self.background_normal = 'button_3.png'


class Minefield(GridLayout):
    def __init__(self, **kwargs):
        super(Minefield, self).__init__(**kwargs)
        self.cols = 9
        self.rows = 9
        self.cells = []
        self.mine_count = 10
        self.generate_buttons()
        self.generate_mines()
        self.count_mines()

    def generate_buttons(self):
        for row in range(self.rows):
            cell_row = []
            for col in range(self.cols):
                cell = Cell()
                cell.bind(on_release=self.cell_clicked)
                self.add_widget(cell)
                cell_row.append(cell)
            self.cells.append(cell_row)

    def generate_mines(self):
        mine_positions = []
        while len(mine_positions) < self.mine_count:
            position = (randint(0, self.rows - 1), randint(0, self.cols - 1))
            if position not in mine_positions:
                mine_positions.append(position)
                cell = self.cells[position[0]][position[1]]
                cell.is_mine = True

    def count_mines(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cells[row][col]
                if not cell.is_mine:
                    count = 0
                    for i in range(max(0, row - 1), min(row + 2, self.rows)):
                        for j in range(max(0, col - 1), min(col + 2, self.cols)):
                            if self.cells[i][j].is_mine:
                                count += 1
                    cell.mine_count = count

    def cell_clicked(self, cell):
        if cell.is_mine:
            self.end_game(False)
        else:
            cell.is_open = True
            cell.text = str(cell.mine_count)
            cell.disabled = True

            if cell.mine_count == 0:
                self.open_adjacent_cells(cell)

            if self.check_win():
                self.end_game(True)

    def open_adjacent_cells(self, cell):
        row, col = self.get_cell_position(cell)
        for i in range(max(0, row - 1), min(row + 2, self.rows)):
            for j in range(max(0, col - 1), min(col + 2, self.cols)):
                adj_cell = self.cells[i][j]
                if not adj_cell.is_open and not adj_cell.is_mine:
                    adj_cell.is_open = True
                    adj_cell.text = str(adj_cell.mine_count)
                    adj_cell.disabled = True
                    if adj_cell.mine_count == 0:
                        self.open_adjacent_cells(adj_cell)

    def get_cell_position(self, cell):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.cells[row][col] == cell:
                    return row, col

    def end_game(self, is_win):
        if is_win:
            message = "You win!"
        else:
            for row in self.cells:
                for cell in row:
                    if cell.is_mine:
                        cell.background_normal = 'mine.png'
                    else:
                        cell.is_open = True
                        cell.text = str(cell.mine_count)
                        cell.disabled = True
            message = "You lose!"
        popup = Popup(title=message, content=Label(text=message), size_hint=(None, None), size=(200, 200))

        new_game_button = Button(text='New Game', size_hint=(1, None), height=50)
        new_game_button.bind(on_release=self.start_new_game)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(new_game_button)
        layout.add_widget(Label(text=message))

        popup.content = layout
        popup.open()

    def start_new_game(self, instance):
        self.clear_widgets()
        self.cells = []
        self.generate_buttons()
        self.generate_mines()
        self.count_mines()
        for child in self.parent.children:
            if isinstance(child, Popup):
                child.dismiss()

    def check_win(self):
        for row in self.cells:
            for cell in row:
                if not cell.is_open and not cell.is_mine:
                    return False
        return True

    def reset_game(self):
        self.clear_widgets()
        self.cells = []
        self.generate_buttons()
        self.generate_mines()
        self.count_mines()


class SaperApp(App):
    def build(self):

        return Minefield()


if __name__ == '__main__':
    SaperApp().run()

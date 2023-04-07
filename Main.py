from kivy.lang import Builder
from kivymd.app import MDApp
from DatabaseInit import *


class MainApp(MDApp):
    TABLE = "test"
    DATABASE = "test.db"

    db = databaseInit(DATABASE)
    db.create_table(f'CREATE TABLE IF NOT EXISTS {TABLE} (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, surrname text)')

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('KivyDesign.kv')

    def submit(self):
        MainApp.db.insert('test', self.root.ids.word_input.text, self.root.ids.word_input2.text)

        self.root.ids.word_label.text = f'{self.root.ids.word_input.text} {self.root.ids.word_input2.text} Added'
        self.root.ids.word_input.text = ''
        self.root.ids.word_input2.text = ''

    def show_records(self):
        records = MainApp.db.returnRecords('test')

        word = ''
        for record in enumerate(records):
            word = f'{word}{record}\n'
            self.root.ids.word_label.text = f'{word}'


MainApp().run()
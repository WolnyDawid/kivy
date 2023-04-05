from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3


class SignUpWindow(Screen):
    pass


class SignInWindow(Screen):
    pass


# class ProductList(Screen):
#     pass


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        # Create Database Or Connect To One
        conn = sqlite3.connect('first_db.db')

        # Create A Cursor
        c = conn.cursor()

        # Create A Table
        c.execute("""CREATE TABLE if not exists customers(name text, surrname text)""")

        # Commit our changes
        conn.commit()

        # Close our connection
        conn.close()

        return Builder.load_file('first_db.kv')

    def submit(self):
        # Create Database Or Connect To One
        conn = sqlite3.connect('first_db.db')

        # Create A Cursor
        c = conn.cursor()

        # Add A Record
        c.execute("INSERT INTO customers VALUES (:first, :second)",
                  {
                      'first': self.root.ids.word_input.text,
                      'second': self.root.ids.word_input2.text,
                  })

        # Add a little message
        self.root.ids.word_label.text = f'{self.root.ids.word_input.text} {self.root.ids.word_input2.text} Added'

        # Clear the input box

        self.root.ids.word_input.text = ''
        self.root.ids.word_input2.text = ''

        # Commit our changes
        conn.commit()

        # Close our connection
        conn.close()

    def show_records(self):
        # Create Database Or Connect To One
        conn = sqlite3.connect('first_db.db')

        # Create A Cursor
        c = conn.cursor()

        # Grab records from database
        c.execute("SELECT * FROM customers")
        records = c.fetchall()
        print(records)
        word = ''
        # Loop true records
        for record in enumerate(records):
            word = f'{word}{record}\n'
            self.root.ids.word_label.text = f'{word}'

        # Commit our changes
        conn.commit()

        # Close our connection
        conn.close()


MainApp().run()
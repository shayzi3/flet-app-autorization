
import flet as ft 


class Main:
     def __init__(self, page: ft.Page) -> None:
          self.page = page
          
          self.page.window_height = 700
          self.page.window_width = 500
          self.page.theme_mode = ft.ThemeMode.DARK
          self.page.title = 'Autorization'
          
          my = MyApp(self.page)
          my.logIn_page()
          
          
class MyApp:
     def __init__(self, page: ft.Page) -> None:
          self.page = page
          
             
     def logIn_page(self) -> None:
          
          def change_theme_mode(e: ft.ControlEvent) -> None:
               self.page.theme_mode = ft.ThemeMode.DARK if self.page.theme_mode.name == 'LIGHT' else ft.ThemeMode.LIGHT
               e.control.icon = ft.icons.DARK_MODE if self.page.theme_mode.name == 'DARK' else ft.icons.WB_SUNNY_OUTLINED
               
               username.border_color = 'white' if self.page.theme_mode == 'DARK' else 'black'
               password.border_color = 'white' if self.page.theme_mode == 'DARK' else 'black'
               e.control.selected = not e.control.selected
               
               self.page.update()
          
          theme_sign = ft.Row(
               controls=[
                    ft.IconButton(
                         icon=ft.icons.DARK_MODE, 
                         icon_size=18, 
                         on_click=change_theme_mode,
                         style=ft.ButtonStyle(color={'':ft.colors.WHITE, 'selected': ft.colors.BLACK})
                    ),
                    ft.Row(
                         controls=[
                              ft.TextButton(text='Sign Up')
                         ],
                         height=53
                    ),
                         
               ],
               height=225,
               vertical_alignment=ft.CrossAxisAlignment.END,
               alignment=ft.MainAxisAlignment.START,
               spacing=350
          )
           
          log_in = ft.TextButton(text='Sign In')
          username = ft.TextField(width=300, border_color='white', label='Username')
          password = ft.TextField(width=300, border_color='white', label='Password', password=True)
          
          data = ft.Column(
               controls=[
                    ft.Text('Hello ...', theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                    username,
                    password,
                    log_in
                    ],
                    width=500,
                    height=400,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
          )
          
          
          self.page.add(
               data,
               theme_sign
          )
          

def start():
     ft.app(Main)
     
if __name__ == '__main__':
     start()
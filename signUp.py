
import flet as ft 

import signIn as sn


class MainReg:
     def __init__(self, page: ft.Page) -> None:
          self.page = page
          
          self.page.window_height = 700
          self.page.window_width = 500
          self.page.theme_mode = ft.ThemeMode.DARK
          self.page.title = 'Autorization'
          
          my_app = MyAppReg(self.page)
          my_app.register_page()
          

class MyAppReg:
     def __init__(self, page: ft.Page) -> None:
          self.page = page
          
     def register_page(self):
          
          def sign_up(e: ft.ControlEvent) -> None:
               ...
               
          def password_changer(e: ft.ControlEvent) -> None:
               if e.control.icon == 'remove_red_eye':
                    password.password = False
                    e.control.icon = ft.icons.REMOVE_RED_EYE_OUTLINED
                    
               else:
                    password.password = True
                    e.control.icon = ft.icons.REMOVE_RED_EYE
               
               self.page.update()
               
          def change_theme_mode(e: ft.ControlEvent) -> None:
               ...
               
          def going_sign_in(e: ft.ControlEvent) -> None:
               self.page.controls.clear()
               main_ = sn.MainLogIn(self.page)
               
               
          text_hello = ft.Text('Зарегестрируйся!', theme_style=ft.TextThemeStyle.TITLE_MEDIUM)
          real_name = ft.TextField(label='Your name', width=300, border_color='white')
          username = ft.TextField(label='Username', width=300, border_color='white')
          password = ft.TextField(label='Password', width=300, border_color='white', password=True)
          
          sign_up_ = ft.ElevatedButton(text='Sign Up', color='white', on_click=sign_up)
          password_check = ft.IconButton(icon=ft.icons.REMOVE_RED_EYE, icon_size=15, on_click=password_changer)
          
          sign_in = ft.ElevatedButton(text='Sign In', color='white', on_click=going_sign_in)
          theme_changer = ft.Row(
               controls=[
                    ft.IconButton(
                         icon=ft.icons.DARK_MODE,
                         icon_size=18,
                         on_click=change_theme_mode,
                         style=ft.ButtonStyle(color={'': ft.colors.WHITE, 'selected': ft.colors.BLACK})
                         ),
                    ft.Row(
                         controls=[
                              sign_in
                         ],
                         height=47
                    )
               ],
               height=225,
               alignment=ft.MainAxisAlignment.START,
               vertical_alignment=ft.CrossAxisAlignment.END,
               spacing=325
          )
          
          column = ft.Column(
               controls=[
                    text_hello,
                    real_name,
                    username,
                    password,
                    ft.Row(
                         controls=[
                              sign_up_,
                              password_check
                         ],
                         spacing=20,
                         width=500,
                         alignment=ft.MainAxisAlignment.CENTER,
                         vertical_alignment=ft.CrossAxisAlignment.CENTER
                    )
               ],
               width=500,
               height=400,
               alignment=ft.MainAxisAlignment.CENTER,
               horizontal_alignment=ft.CrossAxisAlignment.CENTER
          )
          
          
          
          
          self.page.add(
               column,
               theme_changer
          )
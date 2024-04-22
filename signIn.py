
import flet as ft 

import back
import signUp as sp


class MainLogIn:
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
          def change_theme_vidgets(color_: str):
               username.border_color = color_
               password.border_color = color_
               log_in.color = color_
               sign_up.color = color_
               password_button.icon_color = color_
               
           
          def change_theme_mode(e: ft.ControlEvent) -> None:
               self.page.theme_mode = ft.ThemeMode.DARK if self.page.theme_mode.name == 'LIGHT' else ft.ThemeMode.LIGHT
               
               e.control.icon = ft.icons.DARK_MODE if self.page.theme_mode.name == 'DARK' else ft.icons.WB_SUNNY_OUTLINED
               e.control.selected = not e.control.selected 
               
               color_ = 'black' if self.page.theme_mode.name == 'LIGHT' else 'white'
               change_theme_vidgets(color_)      
               
               self.page.update()
               
               
          def hello(e: ft.ControlEvent) -> None:
               if len(e.control.value) <= 20:
                    text_name.value = f'Hello {e.control.value.capitalize()}'
                    self.page.update()
                    
                    
          def check_password(e: ft.ControlEvent) -> None:
               if e.control.icon == 'remove_red_eye':
                    password.password = False
                    e.control.icon = ft.icons.REMOVE_RED_EYE_OUTLINED
                    
               else:
                    password.password = True
                    e.control.icon = ft.icons.REMOVE_RED_EYE
               
               self.page.update()
               
               
          def data(e: ft.ControlEvent) -> None:
               if username.value and password.value:
                    if not back.login_check(username.value):
                         text_name.value = 'Такого аккаунта не существует!'
                         
                    elif back.login_check(username.value) == int(password.value):
                         text_name.value = 'Регистация прошла успешно!'
                         
                    else:
                         text_name.value = 'Неправильный пароль от аккаунта!'
               self.page.update()
               
               
          def going_register(e: ft.ControlEvent) -> None:
               self.page.controls.clear()
               main = sp.MainReg(self.page)
                         
          
          sign_up = ft.ElevatedButton(text='Sign Up', color='white', on_click=going_register)
          theme_sign = ft.Row(
               controls=[
                    ft.IconButton(
                         icon=ft.icons.DARK_MODE, 
                         icon_size=18, 
                         on_click=change_theme_mode,
                         style=ft.ButtonStyle(color={'': ft.colors.WHITE, 'selected': ft.colors.BLACK})
                    ),
                    ft.Row(
                         controls=[
                              sign_up
                         ],
                         height=47
                    ),
                         
               ],
               height=225,
               vertical_alignment=ft.CrossAxisAlignment.END,
               alignment=ft.MainAxisAlignment.START,
               spacing=325
          )
          
          log_in = ft.ElevatedButton(text='Sign In', color='white', on_click=data)
          password_button = ft.IconButton(icon=ft.icons.REMOVE_RED_EYE, icon_size=15, on_click=check_password, icon_color='white')
          username = ft.TextField(width=300, label='Username', border_color='white', on_change=hello)
          password = ft.TextField(width=300, label='Password', border_color='white', password=True)
          text_name =  ft.Text('Hello ...', theme_style=ft.TextThemeStyle.TITLE_MEDIUM)
          
          data = ft.Column(
               controls=[
                    text_name,
                    username,
                    password,
                    ft.Row(
                         controls=[
                              log_in,
                              password_button
                         ],
                         spacing=20,
                         width=500,
                         vertical_alignment=ft.CrossAxisAlignment.CENTER,
                         alignment=ft.MainAxisAlignment.CENTER
                    )
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
     ft.app(MainLogIn)
     
if __name__ == '__main__':
     start()
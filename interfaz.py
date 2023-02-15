import flet as ft
import conversor

def main(page: ft.Page):
    page.padding = 0
    page.title = "MyConversor"
    page.bgcolor = ft.colors.WHITE
    page.window_maximizable = False
    page.theme_mode = ft.ThemeMode.LIGHT

    dlg = ft.AlertDialog(title=ft.Text("El número que colocó está mal compuesto 😒",color=ft.colors.BLACK),
                         shape=ft.RoundedRectangleBorder(radius=5))

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()
    def click(e):
        vf = conversor.verificador()
        if fromNumber.value == 'Binario' and vf.isBinario(number.value):
            resultado.value = f'El resultado de {fromNumber.value} a {toNumber.value} es: {getResult(number.value,fromNumber.value,toNumber.value)} 😮'
        elif fromNumber.value == 'Octal' and vf.isOctal(number.value):
            resultado.value = f'El resultado de {fromNumber.value} a {toNumber.value} es: {getResult(number.value,fromNumber.value,toNumber.value)} 😮'
        elif fromNumber.value == 'Decimal' and vf.isDecimal(number.value):
            resultado.value = f'El resultado de {fromNumber.value} a {toNumber.value} es: {getResult(number.value,fromNumber.value,toNumber.value)} 😮'
        elif fromNumber.value == 'Hexadecimal' and vf.isHexadecimal(number.value):
            resultado.value = f'El resultado de {fromNumber.value} a {toNumber.value} es: {getResult(number.value,fromNumber.value,toNumber.value)} 😮'
        else:
            open_dlg(e)
        page.update()
    ft.TextStyle()
    fromNumber = ft.Dropdown(
        hint_text="El número está en...",
        hint_style= ft.TextStyle(color=ft.colors.BLACK),
        color=ft.colors.BLACK,
        options=[
            ft.dropdown.Option("Binario"),
            ft.dropdown.Option("Octal"),
            ft.dropdown.Option("Decimal"),
            ft.dropdown.Option("Hexadecimal")
        ],
        focused_border_color= ft.colors.TEAL_ACCENT_700,

    )
    toNumber = ft.Dropdown(
        hint_text="El número se convertira a...",
        hint_style=ft.TextStyle(color=ft.colors.BLACK),
        color=ft.colors.BLACK,
        options=[
            ft.dropdown.Option("Binario"),
            ft.dropdown.Option("Octal"),
            ft.dropdown.Option("Decimal"),
            ft.dropdown.Option("Hexadecimal")
        ],
        focused_border_color=ft.colors.TEAL_ACCENT_700,

    )
    grupo = ft.Text("Jonnathan Sotelo Rodríguez-20202020040 / Handersson Felipe Pacheco Espitia-20202020053 / Ana Gabriela Guevara-20202020013 / Alvarez Omar Armando Neira Ordoñez-20192020110"
                    ,size=11,text_align=ft.TextAlign.CENTER,color="WHITE")
    resultado = ft.Text("No haz hecho niguna operación aun! 🤓",color=ft.colors.BLACK)
    btnOperar = ft.ElevatedButton("Realizar Operación",icon=ft.icons.KEYBOARD_ARROW_RIGHT_ROUNDED,
                                  bgcolor=ft.colors.TEAL_ACCENT_700,color=ft.colors.WHITE,on_click=click)
    number = ft.TextField(label="Número a convertir ✍️", border=ft.InputBorder.UNDERLINE,color=ft.colors.BLACK
                           ,focused_border_color=ft.colors.TEAL_ACCENT_700,focused_color=ft.colors.BLACK,
                           label_style=ft.TextStyle(color=ft.colors.TEAL_ACCENT_700,size=14))
    contenedor = ft.Container(content=ft.Column(controls=[
                                     ft.Text("Conversor de Números", weight=ft.FontWeight.BOLD,
                                             size=20,color=ft.colors.BLACK),
                                     fromNumber,
                                     toNumber,
                                     number,
                                     btnOperar,
                                     resultado],horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                                    expand=True,padding=50)
    info = ft.Container(bgcolor=ft.colors.TEAL_ACCENT_700,
                        content=ft.Column(
                        controls=[
                            ft.Text("🤔 Sistema Binario", size=20,weight=ft.FontWeight.BOLD,color="WHITE"),
                            ft.Text("El sistema binario, también llamado sistema diádico en ciencias de la computación, es un sistema de numeración en el que los números son representados utilizando únicamente dos cifras: 0 (cero) y 1 (uno).",
                                    text_align=ft.TextAlign.JUSTIFY,color="WHITE"),
                            ft.Text("🤔 Sistema Octal",size=20,weight=ft.FontWeight.BOLD,color="WHITE"),
                            ft.Text("El sistema octal es el sistema de numeración posicional cuya base es igual 8, utilizando los dígitos indio arábigos: 0,1,2,3,4,5,6,7. En informática a veces se utiliza la numeración octal en vez de la hexadecimal. Tiene la ventaja de que no requiere utilizar otros símbolos diferentes de los dígitos.",
                                    text_align=ft.TextAlign.JUSTIFY,color="WHITE"),
                            ft.Text("🤔 Sistema Hexadecimal", size=20,weight=ft.FontWeight.BOLD,color="WHITE"),
                            ft.Text("El sistema hexadecimal (abreviado hex.) es el sistema de numeración posicional que tiene como base el 16. Su uso actual está muy vinculado a la informática y ciencias de la computación donde las operaciones de la CPU suelen usar el byte u octeto como unidad básica de memoria.",
                                    text_align=ft.TextAlign.JUSTIFY,color="WHITE")
                            ,grupo],horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                        alignment=ft.MainAxisAlignment.SPACE_AROUND),
                        expand= True,
                        height= page.window_height,
                        padding=50)
    row = ft.Row(
        spacing=10,
        run_spacing=0,
        controls= [contenedor,info],
        width=page.window_width,
    )
    page.add(row)


def getResult(num:str,fromN:str,toN:str)->str:
    cv = conversor.Conversor()
    if fromN != toN:
        if fromN == 'Binario' and toN =='Octal':
            return cv.bin_oct(num)
        elif fromN == 'Binario' and toN =='Decimal':
            return str(cv.bin_dec(num))
        elif fromN == 'Binario' and toN =='Hexadecimal':
            return cv.bin_hex(num)
        elif fromN == 'Octal' and toN =='Binario':
            return cv.oct_bin(num)
        elif fromN == 'Octal' and toN =='Decimal':
            return str(cv.oct_dec(num))
        elif fromN == 'Octal' and toN =='Hexadecimal':
            return cv.oct_hex(num)
        elif fromN == 'Decimal' and toN =='Binario':
            return cv.dec_bin(int(num))
        elif fromN == 'Decimal' and toN =='Octal':
            return cv.dec_oct(int(num))
        elif fromN == 'Decimal' and toN =='Hexadecimal':
            return cv.dec_hex(int(num))
        elif fromN == 'Hexadecimal' and toN == 'Binario':
            return cv.hex_bin(num)
        elif fromN == 'Hexadecimal' and toN == 'Octal':
            return cv.hex_oct(num)
        elif fromN == 'Hexadecimal' and toN == 'Decimal':
            return str(cv.hex_dec(num))
        pass
    else:
        return "Debes estar haciendo algo raro... 😢"


if __name__ == '__main__':
    ft.app(target=main)
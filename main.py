import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("DIP02 Calculator")

        # เก็บข้อมูล
        self.result_var = tk.StringVar()
        self.result_var.set("0")

        
        self.create_widgets()

# สร้างหน้าต่าง ------------------------------------------------------

    def create_widgets(self):
        self.entry = tk.Entry(
            self.root,
            textvariable=self.result_var,
            font=('Arial', 24),
            bd=10,
            insertwidth=2,
            width=14,
            justify='right'
        )
        self.entry.grid(row=0, column=0, columnspan=4)  

        # ปุ่ม "Clear" และ "Backspace" 
        self.create_button('C', 1, 0)
        self.create_button('<-', 1, 1)

        buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('=', 5, 1), ('+', 5, 2),
        ]


        for (text, row, col) in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
       
        button = tk.Button(
            self.root,
            text=text,
            padx=20,
            pady=20,
            font=('Arial', 18),
            command=lambda: self.button_click(text)
        )
        button.grid(row=row, column=col, sticky='nsew')

# จบหน้าต่าง ----------------------------------------------------

# สร้างปุ่ม clear backspace equal

    def button_click(self, text):

        current_text = self.result_var.get()
        
        # ปุ่ม clear
        if text == 'C':
            self.result_var.set("0")
        # ปุ่ม Backspace
        elif text == '<-':
            self.result_var.set(current_text[:-1] if len(current_text) > 1 else '0')
        # ปุ่ม equal
        elif text == '=':
            try:
                # คำนวณ การบวก ลบ คูณ หาร โดยใช้ eval() 
                result = eval(current_text)
                self.result_var.set(str(result))
            except Exception as e:
                self.result_var.set("Error")
        else:
            # เพิ่มข้อความจากปุ่มที่คลิกลงในหน้าจอปัจจุบัน
            if current_text == "0" and text.isdigit():
                self.result_var.set(text)
            else:
                self.result_var.set(current_text + text) 

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()

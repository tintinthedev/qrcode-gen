import customtkinter as ctk
from qrcode_canvas import QRCodeFrame


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color="white")
        self.title("QR Code generator!")

        self.geometry("400x500")

        self.colors = {
            "base": "#b0b0b0",
            "primary": "#262626",
            "base-clearer": "#ebebeb",
            "primary-clearer": "#363636",
        }

        self.create_widgets()
        self.display_widgets()

        self.mainloop()

    def create_widgets(self):
        self.bottom_bar = ctk.CTkFrame(self, fg_color=self.colors["base"])

        self.qrcode_content = ctk.StringVar(value="")

        self.text_entry = ctk.CTkEntry(
            self.bottom_bar,
            placeholder_text="Some text here",
            width=200,
            fg_color=self.colors["base-clearer"],
            border_color=self.colors["base"],
            text_color=self.colors["primary"],
            textvariable=self.qrcode_content,
        )

        self.qrcode_frame = QRCodeFrame(self, self.qrcode_content)

        self.save_qrcode_button = ctk.CTkButton(
            self.bottom_bar,
            text="Save QR Code",
            fg_color=self.colors["primary"],
            hover_color=self.colors["primary-clearer"],
            command=self.qrcode_frame.save_qrcode,
        )

    def display_widgets(self):
        self.bottom_bar.place(relx=0, rely=1, relwidth=1, relheigh=0.1, anchor="sw")
        self.text_entry.pack(expand=True, side="left")
        self.save_qrcode_button.pack(expand=True, side="right")
        self.qrcode_frame.place(w=200, h=200, relx=0.5, rely=0.4, anchor="center")


App()

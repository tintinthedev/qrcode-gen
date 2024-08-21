import customtkinter as ctk
import qrcode
from PIL import ImageTk


class QRCodeFrame(ctk.CTkFrame):
    def __init__(self, master, qrcode_content_variable: ctk.StringVar):
        super().__init__(master)

        self.image_canvas = ctk.CTkCanvas(
            self,
            bg="white",
            highlightthickness=0,
            bd=0,
            relief="ridge",
            width=200,
            height=200,
        )

        self.image_canvas.pack(expand=True, fill="both")

        self.qrcode_content_variable = qrcode_content_variable

        self.qrcode_content_variable.trace_add("write", self.generate_qrcode)

        self.generate_qrcode()

    def generate_qrcode(self, *trace_args):
        global qr_image_tk  # i think this needs to be in the same scope as the app's mainloop functtion
        self.qr_image = qrcode.make(self.qrcode_content_variable.get())
        qr_image_resized = self.qr_image.resize((200, 200))
        qr_image_tk = ImageTk.PhotoImage(qr_image_resized)

        self.image_canvas.create_image((0, 0), image=qr_image_tk, anchor="nw")

    def save_qrcode(self):
        self.qr_image.save("generated_code.png")

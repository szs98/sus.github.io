import tkinter as tk
from tkinter import messagebox
from twilio.rest import Client

# Twilio API bilgileri
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
twilio_phone_number = 'YOUR_TWILIO_PHONE_NUMBER'

def send_sms():
    recipient = entry_recipient.get()
    message = text_box.get("1.0", "end-1c")
    count = int(entry_count.get())
    
    try:
        client = Client(account_sid, auth_token)
        
        for _ in range(count):
            client.messages.create(
                body=message,
                from_=twilio_phone_number,
                to=recipient
            )
        messagebox.showinfo("Başarılı", f"{count} adet mesaj başarıyla gönderildi!")
    except Exception as e:
        messagebox.showerror("Hata", f"Mesaj gönderilemedi: {e}")

# Tkinter arayüzü
root = tk.Tk()
root.title("SMS Gönderici")

tk.Label(root, text="Telefon Numarası:").pack(pady=5)
entry_recipient = tk.Entry(root, width=30)
entry_recipient.pack(pady=5)

tk.Label(root, text="Mesaj:").pack(pady=5)
text_box = tk.Text(root, height=10, width=30)
text_box.pack(pady=5)

tk.Label(root, text="Mesaj Sayısı:").pack(pady=5)
entry_count = tk.Entry(root, width=5)
entry_count.pack(pady=5)

send_button = tk.Button(root, text="Gönder", command=send_sms)
send_button.pack(pady=20)

root.mainloop()

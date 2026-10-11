import tkinter as tk
from tkinter import messagebox

COUNTRY_CODES = [
    ("Afghanistan", "+93"), ("Albania", "+355"), ("Algeria", "+213"), ("Andorra", "+376"),
    ("Angola", "+244"), ("Antigua & Barbuda", "+1-268"), ("Argentina", "+54"), ("Armenia", "+374"),
    ("Australia", "+61"), ("Austria", "+43"), ("Azerbaijan", "+994"), ("Bahamas", "+1-242"),
    ("Bahrain", "+973"), ("Bangladesh", "+880"), ("Barbados", "+1-246"), ("Belarus", "+375"),
    ("Belgium", "+32"), ("Belize", "+501"), ("Benin", "+229"), ("Bhutan", "+975"),
    ("Bolivia", "+591"), ("Bosnia & Herzegovina", "+387"), ("Botswana", "+267"), ("Brazil", "+55"),
    ("Brunei", "+673"), ("Bulgaria", "+359"), ("Burkina Faso", "+226"), ("Burundi", "+257"),
    ("Cambodia", "+855"), ("Cameroon", "+237"), ("Canada", "+1"), ("Cape Verde", "+238"),
    ("Central African Republic", "+236"), ("Chad", "+235"), ("Chile", "+56"), ("China", "+86"),
    ("Colombia", "+57"), ("Comoros", "+269"), ("Congo", "+242"), ("Costa Rica", "+506"),
    ("Croatia", "+385"), ("Cuba", "+53"), ("Cyprus", "+357"), ("Czech Republic", "+420"),
    ("Denmark", "+45"), ("Djibouti", "+253"), ("Dominica", "+1-767"), ("Dominican Republic", "+1-809"),
    ("Ecuador", "+593"), ("Egypt", "+20"), ("El Salvador", "+503"), ("Equatorial Guinea", "+240"),
    ("Eritrea", "+291"), ("Estonia", "+372"), ("Eswatini", "+268"), ("Ethiopia", "+251"),
    ("Fiji", "+679"), ("Finland", "+358"), ("France", "+33"), ("Gabon", "+241"),
    ("Gambia", "+220"), ("Georgia", "+995"), ("Germany", "+49"), ("Ghana", "+233"),
    ("Greece", "+30"), ("Grenada", "+1-473"), ("Guatemala", "+502"), ("Guinea", "+224"),
    ("Guyana", "+592"), ("Haiti", "+509"), ("Honduras", "+504"), ("Hungary", "+36"),
    ("Iceland", "+354"), ("India", "+91"), ("Indonesia", "+62"), ("Iran", "+98"),
    ("Iraq", "+964"), ("Ireland", "+353"), ("Israel", "+972"), ("Italy", "+39"),
    ("Jamaica", "+1-876"), ("Japan", "+81"), ("Jordan", "+962"), ("Kazakhstan", "+7"),
    ("Kenya", "+254"), ("Kiribati", "+686"), ("Kuwait", "+965"), ("Kyrgyzstan", "+996"),
    ("Laos", "+856"), ("Latvia", "+371"), ("Lebanon", "+961"), ("Lesotho", "+266"),
    ("Liberia", "+231"), ("Libya", "+218"), ("Liechtenstein", "+423"), ("Lithuania", "+370"),
    ("Luxembourg", "+352"), ("Madagascar", "+261"), ("Malawi", "+265"), ("Malaysia", "+60"),
    ("Maldives", "+960"), ("Mali", "+223"), ("Malta", "+356"), ("Marshall Islands", "+692"),
    ("Mauritania", "+222"), ("Mauritius", "+230"), ("Mexico", "+52"), ("Micronesia", "+691"),
    ("Moldova", "+373"), ("Monaco", "+377"), ("Mongolia", "+976"), ("Montenegro", "+382"),
    ("Morocco", "+212"), ("Mozambique", "+258"), ("Myanmar", "+95"), ("Namibia", "+264"),
    ("Nauru", "+674"), ("Nepal", "+977"), ("Netherlands", "+31"), ("New Zealand", "+64"),
    ("Nicaragua", "+505"), ("Niger", "+227"), ("Nigeria", "+234"), ("North Korea", "+850"),
    ("North Macedonia", "+389"), ("Norway", "+47"), ("Oman", "+968"), ("Pakistan", "+92"),
    ("Palau", "+680"), ("Panama", "+507"), ("Papua New Guinea", "+675"), ("Paraguay", "+595"),
    ("Peru", "+51"), ("Philippines", "+63"), ("Poland", "+48"), ("Portugal", "+351"),
    ("Qatar", "+974"), ("Romania", "+40"), ("Russia", "+7"), ("Rwanda", "+250"),
    ("Samoa", "+685"), ("San Marino", "+378"), ("Saudi Arabia", "+966"), ("Senegal", "+221"),
    ("Serbia", "+381"), ("Seychelles", "+248"), ("Sierra Leone", "+232"), ("Singapore", "+65"),
    ("Slovakia", "+421"), ("Slovenia", "+386"), ("Solomon Islands", "+677"), ("Somalia", "+252"),
    ("South Africa", "+27"), ("South Korea", "+82"), ("Spain", "+34"), ("Sri Lanka", "+94"),
    ("Sudan", "+249"), ("Suriname", "+597"), ("Sweden", "+46"), ("Switzerland", "+41"),
    ("Syria", "+963"), ("Taiwan", "+886"), ("Tajikistan", "+992"), ("Tanzania", "+255"),
    ("Thailand", "+66"), ("Togo", "+228"), ("Tonga", "+676"), ("Trinidad & Tobago", "+1-868"),
    ("Tunisia", "+216"), ("Turkey", "+90"), ("Turkmenistan", "+993"), ("Tuvalu", "+688"),
    ("Uganda", "+256"), ("Ukraine", "+380"), ("United Arab Emirates", "+971"), ("United Kingdom", "+44"),
    ("United States", "+1"), ("Uruguay", "+598"), ("Uzbekistan", "+998"), ("Vanuatu", "+678"),
    ("Vatican City", "+39-06"), ("Venezuela", "+58"), ("Vietnam", "+84"), ("Yemen", "+967"),
    ("Zambia", "+260"), ("Zimbabwe", "+263")
]

class LuxuryPhoneSelector(tk.Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title("Luxury Phone Selector")
        self.geometry("520x760")
        self.configure(bg="#09090B")
        self.resizable(False, False)

        if parent:
            self.transient(parent)
            self.grab_set()

        self.BG_MAIN = "#09090B"
        self.BG_CARD = "#18181B"
        self.BORDER_COLOR = "#27272A"
        self.ACCENT_CYAN = "#FAFAFA"
        self.ACCENT_PURPLE = "#27272A"
        self.TEXT_MAIN = "#F4F4F5"
        self.TEXT_MUTED = "#A1A1AA"

        self.selected_country_code = "+1"
        self.phone_number = "0000000000"

        self._build_header()
        self._build_preview()
        self._build_country_picker()
        self._build_number_scrubber()
        self._build_submit_button()

    def _build_header(self):
        header_frame = tk.Frame(self, bg=self.BG_MAIN, pady=24)
        header_frame.pack(fill="x")

        tagline = tk.Label(
            header_frame,
            text="ou shiii contact entry",
            font=("Helvetica", 9, "bold"),
            fg=self.TEXT_MUTED,
            bg=self.BG_MAIN
        )
        tagline.pack()

        title = tk.Label(
            header_frame,
            text="Phone Number Selector",
            font=("Helvetica", 22, "bold"),
            fg=self.TEXT_MAIN,
            bg=self.BG_MAIN
        )
        title.pack(pady=(4, 0))

    def _build_preview(self):
        card = tk.Frame(self, bg=self.BG_CARD, padx=20, pady=18, highlightbackground=self.BORDER_COLOR, highlightthickness=1)
        card.pack(fill="x", padx=30, pady=10)

        lbl_sub = tk.Label(
            card,
            text="Current selection:",
            font=("Helvetica", 8, "bold"),
            fg=self.TEXT_MUTED,
            bg=self.BG_CARD
        )
        lbl_sub.pack(anchor="w")

        formatted_num = self._format_digits(self.phone_number)
        self.display_var = tk.StringVar(value=f"{self.selected_country_code} {formatted_num}")
        
        self.display_lbl = tk.Label(
            card,
            textvariable=self.display_var,
            font=("Courier", 20, "bold"),
            fg=self.ACCENT_CYAN,
            bg=self.BG_CARD
        )
        self.display_lbl.pack(pady=(5, 0))

    def _build_country_picker(self):
        section_frame = tk.Frame(self, bg=self.BG_MAIN, padx=30)
        section_frame.pack(fill="x", pady=(15, 5))

        label = tk.Label(
            section_frame,
            text="Select country code.",
            font=("Helvetica", 9, "bold"),
            fg=self.TEXT_MUTED,
            bg=self.BG_MAIN
        )
        label.pack(anchor="w", pady=(0, 6))

        picker_container = tk.Frame(section_frame, bg=self.BG_CARD, highlightbackground=self.BORDER_COLOR, highlightthickness=1)
        picker_container.pack(fill="x")

        scrollbar = tk.Scrollbar(picker_container, bg=self.BG_CARD, troughcolor=self.BG_MAIN, width=10, bd=0)
        scrollbar.pack(side="right", fill="y")

        self.country_listbox = tk.Listbox(
            picker_container,
            height=6,
            bg=self.BG_CARD,
            fg=self.TEXT_MAIN,
            selectbackground=self.ACCENT_PURPLE,
            selectforeground="#FAFAFA",
            font=("Helvetica", 11),
            bd=0,
            highlightthickness=0,
            yscrollcommand=scrollbar.set,
            activestyle="none"
        )
        self.country_listbox.pack(side="left", fill="both", expand=True, padx=10, pady=8)
        scrollbar.config(command=self.country_listbox.yview)

        for country, code in COUNTRY_CODES:
            self.country_listbox.insert("end", f"  {country} ({code})")

        self.country_listbox.select_set(0)

        # muahahaha block keyboard navigation >:)
        self.country_listbox.bind("<Key>", lambda e: "break")
        self.country_listbox.bind("<<ListboxSelect>>", self._on_country_select)

    def _build_number_scrubber(self):
        section_frame = tk.Frame(self, bg=self.BG_MAIN, padx=30)
        section_frame.pack(fill="x", pady=(20, 5))

        label = tk.Label(
            section_frame,
            text="(000-000-0000 TO 999-999-9999)",
            font=("Helvetica", 9, "bold"),
            fg=self.TEXT_MUTED,
            bg=self.BG_MAIN
        )
        label.pack(anchor="w", pady=(0, 6))

        slider_card = tk.Frame(section_frame, bg=self.BG_CARD, padx=15, pady=15, highlightbackground=self.BORDER_COLOR, highlightthickness=1)
        slider_card.pack(fill="x")

        self.scale = tk.Scale(
            slider_card,
            from_=0,
            to=9999999999,
            orient="horizontal",
            showvalue=False,
            bg=self.BG_CARD,
            fg=self.TEXT_MAIN,
            troughcolor=self.BG_MAIN,
            activebackground="#FAFAFA",
            highlightthickness=0,
            bd=0,
            command=self._on_slider_move
        )
        self.scale.pack(fill="x")

        hint = tk.Label(
            slider_card,
            text="✦ Drag mouse precise to 1 part in 10,000,000,000",
            font=("Helvetica", 8, "italic"),
            fg=self.TEXT_MUTED,
            bg=self.BG_CARD
        )
        hint.pack(pady=(8, 0))

    def _build_submit_button(self):
        btn_frame = tk.Frame(self, bg=self.BG_MAIN, padx=30, pady=25)
        btn_frame.pack(fill="x", side="bottom")

        confirm_btn = tk.Button(
            btn_frame,
            text="confirm phone number",
            font=("Helvetica", 11, "bold"),
            fg="#09090B",
            bg="#F4F4F5",
            activebackground="#E4E4E7",
            activeforeground="#09090B",
            bd=0,
            padx=20,
            pady=12,
            cursor="hand2",
            command=self._on_submit
        )
        confirm_btn.pack(fill="x")

    def _on_country_select(self, event):
        selection = self.country_listbox.curselection()
        if selection:
            idx = selection[0]
            self.selected_country_code = COUNTRY_CODES[idx][1]
            self._update_display()

    def _on_slider_move(self, val):
        val_int = int(float(val))
        self.phone_number = f"{val_int:010d}"
        self._update_display()

    def _format_digits(self, digits):
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"

    def _update_display(self):
        formatted_num = self._format_digits(self.phone_number)
        self.display_var.set(f"{self.selected_country_code} {formatted_num}")

    def _on_submit(self):
        full_number = self.display_var.get()
        messagebox.showinfo(
            "Selection Confirmed",
            f"Successfully locked in:\n\n{full_number}\n\nThank you for your incredible patience."
        )


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Window")
    root.geometry("400x250")
    root.configure(bg="#09090B")

    def open_popup():
        LuxuryPhoneSelector(root)

    btn = tk.Button(
        root,
        text="Open Phone Selector",
        font=("Helvetica", 11, "bold"),
        fg="#09090B",
        bg="#F4F4F5",
        activebackground="#E4E4E7",
        activeforeground="#09090B",
        bd=0,
        padx=20,
        pady=12,
        cursor="hand2",
        command=open_popup
    )
    btn.pack(expand=True)

    root.mainloop()
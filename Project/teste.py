class Switch():
    def switch(self, port):
        default = "9999"
        return getattr(self, str(port), lambda: default)()

    def faber(self):
        return "8021"

    def acme(self):
        return "8041"

    def alice(self):
        return "8031"

    def bob(self):
        return "8051"


my_switch = Switch()
print(my_switch.switch("alice"))
print(my_switch.switch("nalber"))
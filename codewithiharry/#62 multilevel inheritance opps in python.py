# class Dad:
#     basketball_tournaments = 12
#
#
# class Son(Dad):
#     cricket_tournaments = 10
#
#
# class Grandson(Son):
#     basketball_tournaments = 34
#
#
# kundanlal = Dad()
# narender = Son()
# bablu = Grandson()
# print(f" Basketball = {kundanlal.basketball_tournaments}")
# print(f" Basketball = {bablu.basketball_tournaments}")


"""
electronic device
pocket device
phone
"""


class electronic_device:
    phone = "10K"
    usb_cable_fan = "40K"
    earphone = "120"


class pocket_device(electronic_device):
    power_bank = "10K"


class phone(pocket_device):
    phone = "23K"


print(f"Phone Price in Electronic Market = {electronic_device.phone}")
print(f"Phone Price Which is in my Pocket  = {pocket_device.phone}")
print(f"Pocket gadget usb_cable = {electronic_device.usb_cable_fan}")
print(f"Phone Price actual = {phone.phone}")

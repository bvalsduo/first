import telebot
from telebot import types

token = '6660855707:AAEBLu3quvgdflypeP4NJ238ebASWcOXqM8'

tb = telebot.TeleBot(token)

def mike_tyson(message):
    tyson = types.InlineKeyboardMarkup()
    tyson.add(types.InlineKeyboardButton('Frank Bruno', url='https://www.youtube.com/watch?v=Rxeyq3cvudY&t=484s'),
    types.InlineKeyboardButton('Trevor Berbick', url='https://www.youtube.com/watch?v=QKFhSnX9LzM'),
    types.InlineKeyboardButton('Mitch Green', url='https://www.youtube.com/watch?v=R31ybJBXWcA'),
    types.InlineKeyboardButton('Tony Tucker', url='https://www.youtube.com/watch?v=hPengw-N_j4'),
    types.InlineKeyboardButton('Lennox Lewis ', url='https://www.youtube.com/watch?v=Vewmp2JigcQ'),
    types.InlineKeyboardButton('Buster Douglas', url='https://www.youtube.com/watch?v=OmRv6HWpmgE'),
    types.InlineKeyboardButton('Evander Holyfield 1', url='https://www.youtube.com/watch?v=F4HXeZi2t3Q'),
    types.InlineKeyboardButton('Evander Holyfield 2', url='https://www.youtube.com/watch?v=Ak3rYm-faZc'),
    types.InlineKeyboardButton('Tyrell Biggs ', url='https://www.youtube.com/watch?v=Bd_gMw4LjFc'),
    types.InlineKeyboardButton('Danny Williams', url='https://www.youtube.com/watch?v=I6WCLselSVU'), row_width=2)

    tb.send_message(message.chat.id, 'Iron Mike vs:', reply_markup=tyson)

def sugar_ray(message):
    sugar = types.InlineKeyboardMarkup()
    sugar.add(types.InlineKeyboardButton('Thomas Hearns 1', url='https://www.youtube.com/watch?v=jZ-7SIpdgfI'),
    types.InlineKeyboardButton('Thomas Hearns 2',url='https://www.youtube.com/watch?v=PY1aIAEpUUg'),
    types.InlineKeyboardButton('Marvin Hagler', url='https://www.youtube.com/watch?v=lko_QAxKcc0'),
    types.InlineKeyboardButton('Roberto Duran', url='https://www.youtube.com/watch?v=ZuGZVkYuHM4'),
    types.InlineKeyboardButton('Ayub Kalule', url='https://www.youtube.com/watch?v=Rk0qRD7N59I'),
    types.InlineKeyboardButton('Wilfred Benitez ', url='https://www.youtube.com/watch?v=ejyQTgB9fYI'),
    types.InlineKeyboardButton('Marcos Geraldo', url='https://www.youtube.com/watch?v=sYvbZtPUovY'),
    types.InlineKeyboardButton('Davey Boy Green', url='https://www.youtube.com/watch?v=Tku9I-duCQE'),
    types.InlineKeyboardButton('Frank Santore', url='https://www.youtube.com/watch?v=viNeDicKCiU'),
    types.InlineKeyboardButton('Larry Bonds', url='https://www.youtube.com/watch?v=JHItQT51Ij0'), row_width=2)

    tb.send_message(message.chat.id, 'Sugar Ray vs:', reply_markup=sugar)

def muhammad_ali(message):
    ali = types.InlineKeyboardMarkup()
    ali.add(types.InlineKeyboardButton('George Foreman', url='https://www.youtube.com/watch?v=55AasOJZzDE'),
    types.InlineKeyboardButton('Zora Folley', url='https://www.youtube.com/watch?v=VFFDe9FQL3s'),
    types.InlineKeyboardButton('Joe Frazier 1', url='https://www.youtube.com/watch?v=eIm2eK5uuVA'),
    types.InlineKeyboardButton('Joe Frazier 2', url='https://www.youtube.com/watch?v=NEjaAiNWv24'),
    types.InlineKeyboardButton('Larry Holmes', url='https://www.youtube.com/watch?v=23vQICdr1M8'),
    types.InlineKeyboardButton('Jimmy Ellis', url='https://www.youtube.com/watch?v=tq0ofSlssUI&list=PLVkhCW7rKK3P_YG10ipFseTF0ZBCvhwsh&index=20'),
    types.InlineKeyboardButton('Mac Foster', url='https://www.youtube.com/watch?v=X9e7NduxFjA&list=PLVkhCW7rKK3P_YG10ipFseTF0ZBCvhwsh&index=23'),
    types.InlineKeyboardButton('Alvin Lewis', url='https://www.youtube.com/watch?v=K0z0BmpA_h0&list=PLVkhCW7rKK3P_YG10ipFseTF0ZBCvhwsh&index=26'),
    types.InlineKeyboardButton('Ken Norton 1', url='https://www.youtube.com/watch?v=vbYtHaduVZ8&list=PLVkhCW7rKK3P_YG10ipFseTF0ZBCvhwsh&index=30'),
    types.InlineKeyboardButton('Ken Norton 2', url='https://www.youtube.com/watch?v=TfxGUbAMrNQ&list=PLVkhCW7rKK3P_YG10ipFseTF0ZBCvhwsh&index=31'), row_width=2)

    tb.send_message(message.chat.id, 'Muhammad Ali vs:', reply_markup=ali)

def rocky_marciano(message):
    marciano = types.InlineKeyboardMarkup()
    marciano.add(types.InlineKeyboardButton('Jersey Joe Walcott 1', url='https://www.youtube.com/watch?v=TPKFt4Y7UaQ'),
    types.InlineKeyboardButton('Archie Moore', url='https://www.youtube.com/watch?v=k1xaQI6njJ0'),
    types.InlineKeyboardButton('Joe Louis ', url='https://www.youtube.com/watch?v=wXBhbmrCo5M&list=PLdhebEs-cmOGssOGYYAOj8ivBfTEMJtW6&index=4'),
    types.InlineKeyboardButton('Ezzard Charles', url='https://www.youtube.com/watch?v=HnvtDcpPpMI&list=PLdhebEs-cmOGssOGYYAOj8ivBfTEMJtW6&index=10'),
    types.InlineKeyboardButton('Roland La Starza 1', url='https://www.youtube.com/watch?v=wDbNLDVSkR4&list=PLdhebEs-cmOGssOGYYAOj8ivBfTEMJtW6&index=3'),
    types.InlineKeyboardButton('Roland La Starza 2', url='https://www.youtube.com/watch?v=6qccyxaTeK0&list=PLdhebEs-cmOGssOGYYAOj8ivBfTEMJtW6&index=9'),
    types.InlineKeyboardButton('Jersey Joe Walcott 2', url='https://www.youtube.com/watch?v=uYP7OkjzHiQ&list=PLdhebEs-cmOGssOGYYAOj8ivBfTEMJtW6&index=11'),
    types.InlineKeyboardButton('Harry Mathews', url='https://www.youtube.com/watch?v=a1IOPl_8iWQ&list=PLdhebEs-cmOGssOGYYAOj8ivBfTEMJtW6&index=13'),
    types.InlineKeyboardButton('Rex Layne', url='https://www.youtube.com/watch?v=4Cnl87BZOvU'),
    types.InlineKeyboardButton('Don Cockell', url='https://www.youtube.com/watch?v=Q9P6ZWoymT8'), row_width=2)

    tb.send_message(message.chat.id, 'Rock vs :', reply_markup=marciano)

def floyd_mayweather(message):
    mayweather = types.InlineKeyboardMarkup()
    mayweather.add(types.InlineKeyboardButton('Oscar De La Hoya', url='https://www.youtube.com/watch?v=PiQhc9jEq2s'),
    types.InlineKeyboardButton('Manny Pacquiao', url='https://www.youtube.com/watch?v=39zhhfMGNRk&t=2s'),
    types.InlineKeyboardButton('Marcos Maidana 1', url='https://www.youtube.com/watch?v=KYvOC7MBuUw&t=2s'),
    types.InlineKeyboardButton('Manuel Marquez', url='https://www.youtube.com/watch?v=3DpkVOvuA0Y&t=1s'),
    types.InlineKeyboardButton('Marcos Maidana 2', url='https://www.youtube.com/watch?v=mysd0uyNo7M'),
    types.InlineKeyboardButton('Miguel Cotto ', url='https://www.youtube.com/watch?v=fKiGQfpupRA'),
    types.InlineKeyboardButton('Arturo Gatti', url='https://www.youtube.com/watch?v=THojnKPFpFA&t=164s'),
    types.InlineKeyboardButton('Henry Bruseles', url='https://www.youtube.com/watch?v=7aVc0nFcEVE&list=PLmc2DvvQJHIRPot4DAkBsM-eTIzYk7QHv&index=31'),
    types.InlineKeyboardButton('Sharmba Mitchell', url='https://www.youtube.com/watch?v=Q8Vo_bJZCCg&list=PLmc2DvvQJHIRPot4DAkBsM-eTIzYk7QHv&index=33'),
    types.InlineKeyboardButton('Ricky Hatton', url='https://www.youtube.com/watch?v=sHN6sdhhO38&list=PLmc2DvvQJHIRPot4DAkBsM-eTIzYk7QHv&index=37'),row_width=2)

    tb.send_message(message.chat.id, 'Floyd Mayweather vs:', reply_markup=mayweather)

def thomas_hearns(message):
    hearns = types.InlineKeyboardMarkup()
    hearns.add(types.InlineKeyboardButton('Randy Shields', url='https://www.youtube.com/watch?v=kGz6xsEBCR8'),
    types.InlineKeyboardButton('Mike Colbert', url='https://www.youtube.com/watch?v=WSZgg7ax4DQ&list=PLRac1okCTRP0hxfYBVsRNmOnYFrFneAyP&index=6'),
    types.InlineKeyboardButton('Ernie Singletary', url='https://www.youtube.com/watch?v=E2HVza7MPyQ&list=PLRac1okCTRP0hxfYBVsRNmOnYFrFneAyP&index=15'),
    types.InlineKeyboardButton('Jeff McCracken', url='https://www.youtube.com/watch?v=uHPbAUyl2wg&list=PLRac1okCTRP0hxfYBVsRNmOnYFrFneAyP&index=17'),
    types.InlineKeyboardButton('Murray Sutherland', url='https://www.youtube.com/watch?v=l5B_JtZS6zE&list=PLRac1okCTRP0hxfYBVsRNmOnYFrFneAyP&index=18'),
    types.InlineKeyboardButton('Luigi Minchillo ', url='https://www.youtube.com/watch?v=N7ebobBtXec&list=PLRac1okCTRP0hxfYBVsRNmOnYFrFneAyP&index=19'),
    types.InlineKeyboardButton('Mark Medal', url='https://www.youtube.com/watch?v=evvP0ftE3tA&list=PLRac1okCTRP0hxfYBVsRNmOnYFrFneAyP&index=20'),
    types.InlineKeyboardButton('Dennis Andries', url='https://www.youtube.com/watch?v=h5Rwj7AKA54&list=PLRac1okCTRP0hxfYBVsRNmOnYFrFneAyP&index=21'),
    types.InlineKeyboardButton('Sugar Ray 1', url='https://www.youtube.com/watch?v=jZ-7SIpdgfI'),
    types.InlineKeyboardButton('Sugar Ray 2',url='https://www.youtube.com/watch?v=PY1aIAEpUUg'), row_width=2)

    tb.send_message(message.chat.id, 'Thomas Hearns vs:', reply_markup=hearns)

def roy_jones(message):
    jones = types.InlineKeyboardMarkup()
    jones.add(types.InlineKeyboardButton('Julio Cesar', url='https://www.youtube.com/watch?v=EgOmrlWYotk'),
    types.InlineKeyboardButton('Bernard Hopkins 2', url='https://www.youtube.com/watch?v=0gG37BOcX1Y'),
    types.InlineKeyboardButton('Bernard Hopkins 1', url='https://www.youtube.com/watch?v=uE3t6BBgVpE'),
    types.InlineKeyboardButton('James Toney', url='https://www.youtube.com/watch?v=2o9edGBRIpk'),
    types.InlineKeyboardButton('Stephan Johnson', url='https://www.youtube.com/watch?v=iKT7AvS-Fss&list=PLbEd3Ul7oU_VVKMY6LAFRtFGisEEKxwE7&index=2'),
    types.InlineKeyboardButton('Ron Amundsen', url='https://www.youtube.com/watch?v=IJPg_SSqTTM&list=PLbEd3Ul7oU_VVKMY6LAFRtFGisEEKxwE7&index=3'),
    types.InlineKeyboardButton('Jorge Castro', url='https://www.youtube.com/watch?v=DxZzAWZ-_fQ&list=PLbEd3Ul7oU_VVKMY6LAFRtFGisEEKxwE7&index=15'),
    types.InlineKeyboardButton('Mike McCallum', url='https://www.youtube.com/watch?v=qMGU8GE4AWk&list=PLbEd3Ul7oU_VVKMY6LAFRtFGisEEKxwE7&index=23'),
    types.InlineKeyboardButton('Vinny Pazienza', url='https://www.youtube.com/watch?v=oLcYb3o6buE&list=PLbEd3Ul7oU_VVKMY6LAFRtFGisEEKxwE7&index=21'),
    types.InlineKeyboardButton('Tony Thornton', url='https://www.youtube.com/watch?v=eyxwNHQWOK8&list=PLbEd3Ul7oU_VVKMY6LAFRtFGisEEKxwE7&index=22'), row_width=2)

    tb.send_message(message.chat.id, 'Roy Jones vs:', reply_markup=jones)

def joe_louis(message):
    louis = types.InlineKeyboardMarkup()
    louis.add(types.InlineKeyboardButton('Rocky Marciano', url='https://www.youtube.com/watch?v=wXBhbmrCo5M&list=PLdhebEs-cmOGssOGYYAOj8ivBfTEMJtW6&index=4'),
    types.InlineKeyboardButton('Ezzard Charles', url='https://www.youtube.com/watch?v=HnvtDcpPpMI'),
    types.InlineKeyboardButton('Tony Galento', url='https://www.youtube.com/watch?v=-4GKIjOtF5g'),
    types.InlineKeyboardButton('Omelio A. (skip 10s)', url='https://www.youtube.com/watch?v=Hh2G_rjHNqc&list=PLBKyuOJO9ubRgGDCE8koV0v2QSCLQgs_o&index=3'),
    types.InlineKeyboardButton('James Braddock', url='https://www.youtube.com/watch?v=LNfHZF5GoUg&list=PLBKyuOJO9ubRgGDCE8koV0v2QSCLQgs_o&index=4'),
    types.InlineKeyboardButton('Arturo Godoy', url='https://www.youtube.com/watch?v=M5AVLku4VRI&list=PLBKyuOJO9ubRgGDCE8koV0v2QSCLQgs_o&index=14'),
    types.InlineKeyboardButton('Max Schmeling', url='https://www.youtube.com/watch?v=igoidtPyy6g&list=PLBKyuOJO9ubRgGDCE8koV0v2QSCLQgs_o&index=15'),
    types.InlineKeyboardButton('Billy Conn', url='https://www.youtube.com/watch?v=Li4gwjT2Ibs'),
    types.InlineKeyboardButton('Max Baer', url='https://www.youtube.com/watch?v=2aaebPmnx7E'),
    types.InlineKeyboardButton('Primo Carnera', url='https://www.youtube.com/watch?v=ls8a5ybJRHg'), row_width=2)

    tb.send_message(message.chat.id, 'Joe Louis vs:', reply_markup=louis)

def george_foreman(message):
    foreman = types.InlineKeyboardMarkup()
    foreman.add(types.InlineKeyboardButton('Muhammad ali', url='https://www.youtube.com/watch?v=55AasOJZzDE'),
    types.InlineKeyboardButton('Ron Lyle', url='https://www.youtube.com/watch?v=l8AVcEyyMco'),
    types.InlineKeyboardButton('Tommy Morrison', url='https://www.youtube.com/watch?v=GKF9V9C21K4'),
    types.InlineKeyboardButton('Ken Norton', url='https://www.youtube.com/watch?v=QDXY3wMkyuc&list=PL3kAsCymnNBmiwBrWJpGJeHpil7vBskYL&index=12'),
    types.InlineKeyboardButton('Joe Frazier 1', url='https://www.youtube.com/watch?v=EtacibssAPg&list=PL3kAsCymnNBmiwBrWJpGJeHpil7vBskYL&index=10'),
    types.InlineKeyboardButton('Joe Frazier 2', url='https://www.youtube.com/watch?v=3NmvPRP6NlA&list=PL3kAsCymnNBmiwBrWJpGJeHpil7vBskYL&index=15'),
    types.InlineKeyboardButton('John Denis', url='https://www.youtube.com/watch?v=RFYMp4neZ98&list=PL3kAsCymnNBmiwBrWJpGJeHpil7vBskYL&index=16'),
    types.InlineKeyboardButton('Mark Young', url='https://www.youtube.com/watch?v=pdnwMayOjuA&list=PL3kAsCymnNBmiwBrWJpGJeHpil7vBskYL&index=25'),
    types.InlineKeyboardButton('Everett Martin', url='https://www.youtube.com/watch?v=susaIBTYcSo&list=PL3kAsCymnNBmiwBrWJpGJeHpil7vBskYL&index=27'),
    types.InlineKeyboardButton('Lou SAVARESE', url='https://www.youtube.com/watch?v=W6tD24FlfJw&list=PL3kAsCymnNBmiwBrWJpGJeHpil7vBskYL&index=34'), row_width=2)

    tb.send_message(message.chat.id, 'George Foreman vs:', reply_markup=foreman)

def joe_frazier(message):
    frazier = types.InlineKeyboardMarkup()
    frazier.add(types.InlineKeyboardButton('Floyd Cummings', url='https://www.youtube.com/watch?v=pG_vN9w0_8I&list=PL3kAsCymnNBnE7TczxUrAO09H670LKkVg&index=17'),
    types.InlineKeyboardButton('Muhammad Ali 1', url='https://www.youtube.com/watch?v=eIm2eK5uuVA'),
    types.InlineKeyboardButton('Muhammad Ali 2', url='https://www.youtube.com/watch?v=NEjaAiNWv24'),
    types.InlineKeyboardButton('Muhammad Ali 3', url='https://www.youtube.com/watch?v=olp9gsmD_A0'),
    types.InlineKeyboardButton('George Foreman 1', url='https://www.youtube.com/watch?v=EtacibssAPg&list=PL3kAsCymnNBmiwBrWJpGJeHpil7vBskYL&index=10'),
    types.InlineKeyboardButton('George Foreman 2', url='https://www.youtube.com/watch?v=3NmvPRP6NlA&list=PL3kAsCymnNBmiwBrWJpGJeHpil7vBskYL&index=15'),
    types.InlineKeyboardButton('Ron Stander', url='https://www.youtube.com/watch?v=1CkmiKle4qs'),
    types.InlineKeyboardButton('Oscar Bonavena', url='https://www.youtube.com/watch?v=TTlHViwE8_4&list=PL3kAsCymnNBnE7TczxUrAO09H670LKkVg&index=2'),
    types.InlineKeyboardButton('Jerry Quarry', url='https://www.youtube.com/watch?v=fWS3ls52-r0&list=PL3kAsCymnNBnE7TczxUrAO09H670LKkVg&index=7'),
    types.InlineKeyboardButton('Eddie Machen', url='https://www.youtube.com/watch?v=94jZXt1EQ38&list=PL3kAsCymnNBnE7TczxUrAO09H670LKkVg&index=3'), row_width=2)

    tb.send_message(message.chat.id, 'Joe Frazier vs:', reply_markup=frazier)


@tb.message_handler(commands=['start'])
def start(message):
    boxers = types.InlineKeyboardMarkup()
    boxers.add(types.InlineKeyboardButton('Mike Tyson', callback_data='Mike Tyson'),
    types.InlineKeyboardButton('Sugar Ray Leonard', callback_data='Sugar Ray Leonard'),
    types.InlineKeyboardButton('Muhammad Ali', callback_data='Muhammad Ali'),
    types.InlineKeyboardButton('Rocky Marciano', callback_data='Rocky Marciano'),
    types.InlineKeyboardButton('Floyd Mayweather', callback_data='Floyd Mayweather'),
    types.InlineKeyboardButton('Thomas Hearns', callback_data='Thomas Hearns'),
    types.InlineKeyboardButton('Roy Jones', callback_data='Roy Jones'),
    types.InlineKeyboardButton('Joe Louis', callback_data='Joe Louis'),
    types.InlineKeyboardButton('George Foreman', callback_data='George Foreman'),
    types.InlineKeyboardButton('Joe Frazier', callback_data='Joe Frazier'))

    tb.send_message(message.chat.id, 'Hey kid')
    tb.send_message(message.chat.id, 'right here, you can see the Legendary Boxers:', reply_markup=boxers)


@tb.callback_query_handler(func=lambda callback: True)
def call_back(callback):
    dct = {'Mike Tyson': mike_tyson, 'Sugar Ray Leonard': sugar_ray, 'Muhammad Ali': muhammad_ali, 'Rocky Marciano': rocky_marciano, 'Floyd Mayweather': floyd_mayweather, 'Thomas Hearns': thomas_hearns, 'Roy Jones': roy_jones, 'Joe Louis': joe_louis, 'George Foreman': george_foreman, 'Joe Frazier': joe_frazier}

    tb.send_message(callback.message.chat.id, dct[callback.data](callback.message))



tb.infinity_polling()

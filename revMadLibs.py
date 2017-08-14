que1='''
        In Game of __1__, Tyrion is introduced as the third and youngest child
        of wealthy and powerful __2__ Lannister, the former __3__ of the King, and
        Joanna Lannister, who dies giving birth to him. Tyrion's elder sister
        __4__ is the Queen of Westeros by virtue of her marriage to King Robert
        Baratheon, and brother __5__ is one of the Kingsguard, the royal bodyguard.
        '''

que2='''In Game of Thrones, Daenerys is sold off by her __1__, Viserys and Illyrio
        Mopatis to marry Khal Drogo, a __2__ warlord, in exchangefor an army for
        Viserys. At that time, Daenerys befriends Jorah __3__, an exiled Westerosi
        knight, and is given three petrified __4__ eggs as a wedding gift. Though
        initially terrified of Drogo, the marriage turns out to be a happy one,
        and Daenerys grew to love him and began to take to __5__ customs,
        finding strength and determination for the first time.'''

que3='''In Game of Thrones, __1__ Snow is introduced as the 14-year-old bastard
        son of Eddard "Ned" __2__, Lord of __3__, and half-brother to
        Robb, Sansa, Rickon, Bran and __4__. Jon is described as having strong
        Stark features with a lean build, long face, dark brown hair and grey
        eyes. Jon is resented by Ned's wife __5__, who views him as a
        constant reminder of Ned's infidelity.'''

def start_game():
    que=raw_input('\nWelcome to the MADLIB \nWhich question you want to go for?\n 1, 2 or 3?\n')
    if que=='1':
        ans=raw_input(que1)
    elif que=='2':
        ans=raw_input(que2)
    elif que=='3':
        ans=raw_input(que3)
    elif que=='quit':
        exit()
    else:
        start_game()

start_game()

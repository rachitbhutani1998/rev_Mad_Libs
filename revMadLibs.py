# 3 Questions on the basis of increasing difficulty
que1=['''
        In Game of __1__, Tyrion is introduced as the third and youngest child
        of wealthy and powerful __2__ Lannister, the former __3__ of the King, and
        Joanna Lannister, who dies giving birth to him. Tyrion's elder sister
        __4__ is the Queen of Westeros by virtue of her marriage to King Robert
        Baratheon, and brother __5__ is one of the Kingsguard, the royal bodyguard.
        ''','thrones','tywin','hand','cersei','jamie']

que2=['''
        In Game of Thrones, Daenerys is sold off by her __1__, Viserys and Illyrio
        Mopatis to marry Khal Drogo, a __2__ warlord, in exchangefor an army for
        Viserys. At that time, Daenerys befriends Jorah __3__, an exiled Westerosi
        knight, and is given three petrified __4__ eggs as a wedding gift. Though
        initially terrified of Drogo, the marriage turns out to be a happy one,
        and Daenerys grew to love him and began to take to __5__ customs,
        finding strength and determination for the first time.
        ''','brother','dothraki','mormont','dragon','dothraki']

que3=['''
        In Game of Thrones, __1__ Snow is introduced as the 14-year-old bastard
        son of Eddard "Ned" __2__, Lord of __3__, and half-brother to
        Robb, Sansa, Rickon, Bran and __4__. Jon is described as having strong
        Stark features with a lean build, long face, dark brown hair and grey
        eyes. Jon is resented by Ned's wife __5__, who views him as a
        constant reminder of Ned's infidelity.
        ''','jon','stark','winterfell','arya','catelyn']

#Following functions handles the gameplay
def play_game(updated_que,blank_number):
    '''The functions handle the question statement updation corresponding to
    which blank is being answered.
    updated_que:    question statement after every response of user.
    blank_number:   the blank user is currently giving the response of.'''
    while blank_number<=5:
        print '\n'+str(blank_number)+'\n'
        ans=raw_input(updated_que[0])
        if ans==updated_que[blank_number]:#this conditions check if the answer is correct
            updated_que[0]=updated_que[0].replace('__'+str(blank_number)+'__',ans)#updating the question statement
            blank_number=blank_number+1
            play_game(updated_que,blank_number)#proceeding to next blank
        elif ans=='quit':
            exit()
        else:
            print '\nTry Again\n'
            play_game(updated_que,blank_number)#handling the wrong answer response
    print '\n'+updated_que[0]+'\nThanks for playing. You may exit by entering quit or choose another question.\n'
    start_game()


def start_game():
    '''The game starts here'''
    que=raw_input('\nWhich question you want to go for?\n 1, 2 or 3 for easy, medium or hard respectively?\nEnter quit to exit anytime.\n')
    if que=='1':
        play_game(que1,1)
    elif que=='2':
        play_game(que2,1)
    elif que=='3':
        play_game(que3,1)
    elif que=='quit':
        exit()
    else:
        start_game()

print '\nWelcome to the MADLIB'
start_game()

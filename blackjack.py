import random
class Deck:
    my_card = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K'] 

    def shuffle(self):
        for num in range(len(self.my_card)):
            random_index = random.randint(0,len(self.my_card) -1)
            temp = self.my_card[num]
            self.my_card[num] = self.my_card[random_index]
            self.my_card[random_index] = temp

class Blackjack_player(Deck):
    def __init__(self,comp_palyer, hum_player):
        self.comp_player = comp_palyer
        self.hum_player = hum_player

    def passing_card(self):
        '''
        Need while loop in here 
        '''
        sum_for_human = 0
        sum_for_computer = 0
        Deck.shuffle(self)
        for index,value in enumerate(Deck.my_card):
            if index <= 1:
                self.hum_player.append(value)
                Deck.my_card.remove(value)
                continue
            self.comp_player.append(value)
            Deck.my_card.remove(value)
            if(index == 3):
                break
            
        print('Your card - {}'.format(self.hum_player))
        print('Computer card - {}'.format(self.comp_player))
        print('Deck of cards Debug - {}'.format(Deck.my_card))    #Debug 

        while True:
            human_choice = input('Hit or Stop: ')
            if human_choice == 'hit':
                self.hit_method(self.hum_player,Deck.my_card)
                print('Your card - {}'.format(self.hum_player))
                print('Deck of cards Debug - {}'.format(Deck.my_card))             #Debug

                for val in self.hum_player:
                    if val == 'J' or val == 'Q' or val == 'K':
                        self.hum_player[self.hum_player.index(val)] = 10
                    elif val == 'A':
                        while True:
                            a_choice = input("Value of A (1 or 11): ")
                            if a_choice == '1':
                                self.hum_player[self.hum_player.index(val)] = int(a_choice)
                                break
                            elif a_choice == '11':
                                self.hum_player[self.hum_player.index(val)] = int(a_choice)
                                break
                            else:
                                print('Choose between 1 or 11')
                sum_for_human = sum(self.hum_player)
                if sum_for_human > 21:
                    print('Bust!!! Computer Win')
                    break
                       
                '''
                Work on the chip and computers conditions 
                '''

            elif human_choice == 'stop':
               for comp_val in self.comp_player:
                   if comp_val == 'J' or comp_val == 'Q' or comp_val == 'K':
                       sum_for_computer += 10
                   elif comp_val == 'A':
                        sum_for_computer += 11
                   else:
                        sum_for_computer += comp_val
               print('Debug - {}'.format(sum_for_computer)) #Debug 
               if sum_for_human < 21 and sum_for_computer <= 21 and sum_for_human < sum_for_computer:
                        print('Computer win')
                        quit()
               while True:
                   for value in Deck.my_card:
                       self.comp_player.append(value)
                       Deck.my_card.remove(value)
                       print('Computer Card - {}'.format(self.comp_player))
                       print('Deck of card Debug - {}'.format(Deck.my_card))    #Debug
                       if value == 'J' or value == 'Q' or value == 'K':
                            sum_for_computer += 10
                       elif value == 'A':
                           if sum_for_computer <= 10:
                               sum_for_computer += 11
                           else:
                                sum_for_computer += 1
                       else:
                            sum_for_computer += value
                       print('Debug - {}'.format(sum_for_computer)) #Debug
                       if sum_for_human < 21 and sum_for_computer <= 21 and sum_for_human < sum_for_computer:
                           print('Computer win')
                           quit()
                       elif sum_for_computer > 21:
                            print('Congradulation you win!!!')
                            print(sum_for_computer)
                            quit()
            else:
                print("Choose 'hit' or 'stop' ")
            

    def hit_method(self,human_val,card_list):
        index = 0
        while(index < 1):
            human_val.append(card_list[index])
            card_list.remove(card_list[index])
            index += 1

    def stop_method(self,comp_val,card_list):
        index = 0
        pass

b = Blackjack_player([],[])
b.passing_card()



'''
Bugs on this game 
    - When A comes first or second on human move 
    -  
'''

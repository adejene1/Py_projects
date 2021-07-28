'''
Methods 
create the play ground insert the result as list 
assign value to it (x or o)
    - Assign a value to be x or o other wise repeat 
assign the x or o from the upper method change it list 
The winnig condtions 

Structuer 
play_ground(list)

value_assign()

list_assign()
    value_assign()
    play_ground()
    check_condition()
    
check_condition()
'''

class tik_tak_toe():
   

    def play_grond(self ,mylist):
        print (mylist[0]+"  |  " +mylist[1]+"  |  " +mylist[2])
        print("--------------------------------------------")
        print (mylist[3]+"  |  " +mylist[4]+"  |  " +mylist[5])
        print("--------------------------------------------")
        print (mylist[6]+"  |  "+ mylist[7]+"  |  " +mylist[8])

    def assign_value(self):
        myvalues = True 
        while myvalues:
            player1 = input("Enter x or o: ")
            if player1 == 'x' :
                player2 = 'o'
                print("Player 2 is o")
                myvalues = False
            elif player1 == 'o' :
                player2 = 'x'
                print("Player 2 is x")
                myvalues = False
            else:
                print('Try again - Your choice should be x or o')
                continue
            valuelist = []
            valuelist.append(player1)
            valuelist.append(player2)
        return valuelist

    def list_assign(self):
        playerlist = self.assign_value()
        emptystring = ''
        toplaylist = [emptystring] * 9
        num = 0
        my_bool = True
        while my_bool:
            while num < 2:
                if emptystring in toplaylist:
                    index = input('Enter the place starting from 0 - 8: ')
                    if(int(index) >= 9):
                        print("Index out of range try again")
                        continue
                    if toplaylist[int(index)] == 'x' or toplaylist[int(index)] == 'o':
                        print('You can not put your value here try again')
                        continue
                    if num == 0:
                        toplaylist[int(index)] = playerlist[num]
                        num += 1
                    else:
                        toplaylist[int(index)] = playerlist[num] 
                        num -= 1
                else:
                    break
                self.play_grond(toplaylist)
                self.winning_player(toplaylist)

            my_bool = False
            print("It Is Tie!!!!")

    def winning_player(self,winniglist):
         if winniglist[0]== 'x' and winniglist[1]== 'x' and winniglist[2] == 'x' or winniglist[3]== 'x' and winniglist[4]== 'x' and winniglist[5] == 'x' or winniglist[6]== 'x' and winniglist[7]== 'x' and winniglist[8]== 'x' or winniglist[0]== 'x' and winniglist[3]== 'x' and winniglist[6] == 'x' or winniglist[1]== 'x' and winniglist[4]== 'x' and winniglist[7]=='x' or winniglist[2]== 'x' and winniglist[5]== 'x' and winniglist[8]=='x' or winniglist[0]== 'x' and winniglist[4]== 'x' and winniglist[8]=='x' or winniglist[2]== 'x' and winniglist[4]== 'x' and winniglist[6] == 'x':
                print("Congradulation X win the game!!!!!!!")  
                quit()
         elif winniglist[0]== 'o' and winniglist[1]== 'o' and winniglist[2] == 'o' or winniglist[3]== 'o' and winniglist[4]== 'o' and winniglist[5] == 'o' or winniglist[6]== 'o' and winniglist[7]== 'o' and winniglist[8]== 'o' or winniglist[0]== 'o' and winniglist[3]== 'o' and winniglist[6] == 'o' or winniglist[1]== 'o' and winniglist[4]== 'o' and winniglist[7]=='o' or winniglist[2]== 'o' and winniglist[5]== 'o' and winniglist[8]=='o' or winniglist[0]== 'o' and winniglist[4]== 'o' and winniglist[8]=='o' or winniglist[2]== 'o' and winniglist[4]== 'o' and winniglist[6] == 'o':
                print("Congradulation O win the game!!!!!!!")
                quit()

  

player = tik_tak_toe()
player.list_assign()



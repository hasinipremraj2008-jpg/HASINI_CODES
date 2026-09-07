# MY CHECKPOINT PROJECT: WITH EVERYTHING IVE LEARNED SO FAR!
import time
print("                                                                                 WELCOME TO BLACKWOOD MANSION MYSTERY!\n\n"
      "You are a young detective who receives a strange letter:\n"
      "\"Come to Blackwood Mansion tonight.Someone inside is hiding the truth.Find the truth before midnight.\"\n"
      "The letter is unsigned.\n\n"
      "Blackwood Mansion has been abandoned for years after its owner,Mr.Edmund Blackwood, mysteriously disappeared.\n\n"
      "You arrive at 10:00 PM.You have a limit of choices to make until midnight.You will be randomly alloted a limit.\n\n"
      "The mansion has:\n"
      "lvl 1:Basement\n"
      "lvl 2:First Floor\n"
      "lvl 3:Second Floor\n"
      "lvl 4:Attic.\n\n"
      "Your goal:\n"
      "Discover what happened to Edmund Blackwood,when he disappeared and identify who was responsible.\n\n"
      "PART 1:Gather the clues and evidence throughout the mansion.\n"
      "PART 2:Interrogate the suspects.\n"
      "PART 3:Crack the mystery.\n")
time.sleep(40)
name=input('What is your good name detective? ')
ans=int(input('Are you ready to solve this case?\n1.YES!\n2.NO\nWhich option do you choose? '))
if ans==1:
  print("let's start!")
else:
  print('Youve exited the game.')
  exit()
import random
i=random.randint(7,8)
time.sleep(2.5)
print("You have randomly been alloted the choice limit of "+str(i)+" ie. PART 1: "+ str(i-2) +" and PART 2: 2.")
time.sleep(5)
choice_number=0
while choice_number<i-2:
    lvl=int(input('\n\nPART 1:\nWhich level of the mansion do you want to go to? '))
    if lvl==1:    
      print('\n\nYouve entered the Basement.\nOld appliances and boxes of old clothes are present everywhere.But there is one dusty box of cardboard present in the corner.')
      time.sleep(10)     
      option=int(input('Do you want to search the box?\n1.YES\n2.No\nYour option? ')) 
      if option==1:       
        print('The box contains:\n'                             
              'a damaged photo of Edmund with all of the suspects, with a red cicle over one of their faces.The backside reads:I finally know where all the money is going.One of these people have betrayed me.\n'         
              'a broken watch stopped at exactly 10:15p.m.\n'               
              'a key card: 16 ÷ 4 + 3 x 2.5 -2.\n')
        choice_number +=1
        time.sleep(15)
        print("\n\nNo. of choices made: ",choice_number)
    elif lvl==2: 
      option=0    
      while option!=3 and choice_number<i-2:
         option=int(input('\n\nYouve entered the First Floor.\nThere is a kitchen and a library.\nWhich one of these do you want to search?\n1.Kitchen\n2.Library\n3.None\nWhich option do you choose? '))       
         if option==1:      
           print('Youve entered the kitchen.There is a big muddy footprint near the back door and a torn piece of GREEN fabric caught on the door.')     
           choice_number +=1
           time.sleep(10)
           print("\n\nNo. of choices made: ",choice_number)
         elif option==2:      
           print('Youve entered the library.You find a hidden copy of a letter written by Edmund:\n'             
                 'I know what you did, if you dont tell the truth,Ill reveal everything tommorow.\nThe letter is addressed to "T". ' )  
           choice_number +=1
           time.sleep(10)
           print("\n\nNo. of choices made: ",choice_number)
    elif lvl==3: 
       option=0
       while option!=3 and choice_number<i-2:   
         option=int(input('\n\nYouve entered the Second Floor.\nThere is a study and a bedroom.\nWhich one of these do you want to search?\n1.Study\n2.Bedroom\n3.None\nWhich option do you choose? '))    
         if option==1:       
           print("Youve entered the study.You find Mr.Edmund's personal diary tucked in a corner. It's last entry reads:\n"            
                 "I just finished my checkup with Dr.Tyla and its around 9:30p.m.\n"
                 "I hear some footsteps outside but Im alone in the mansion.Didnt Dr.Tyla leave yet?\n"            
                 "The next page has the initials T.W. written on them.")
           time.sleep(15)  
           choice_number +=1
           print("\n\nNo. of choices made: ",choice_number)  
         elif option==2:      
           print('Youve entered the bedroom.You find a locked drawer.\nTo unlock it you require a secret password.\nDo you know the secret password?\n1.YES\n2.NO')
           choice=int(input("What is your option? "))
           if choice==1:
            passcode=0   
            while passcode!=16/4+3*2.5-2: 
              passcode=float(input('What is the secret password? '))        
              print('Youve successfully unlocked the drawer. Inside the drawer you find a note. It reads:\n'           
                    'If anything happens to me,know that this person wouldve come for the evidence Ive hid against them.')  
              time.sleep(10)
            choice_number +=1
            print("\n\nNo. of choices made: ",choice_number)    
    else:      
       print('\n\nYouve entered the attic.You find a box in the corner.\nDo you want to search the box?\n1.YES\n2.NO')      
       option=int(input('Whats is your option? '))      
       if option==1:        
         print("You find a blurry camera footage of someone breaking into Mr.Edmund's safe and stealing his money.\n"            
               "You find a green overalls.\n"
               "You find a pair of big dirty rubber gloves.") 
         time.sleep(15)
         choice_number +=1
         print("\n\nNo. of choices made: ",choice_number)  
print('\n\nPart 2:There are four suspects.\n'
      "1.Tiana Park:She is the housekeeper.\n"
      "2.Tyler Wilson:He is the gardener.\n"
      "3.Dr.Tyla Wilkins:She is his personal doctor.\n"
      "4.William Hill:He is the neighbour.")
time.sleep(15)
choice_number=0
while choice_number<2:
  option=int(input('Who do you want to interrogate ? Enter their number: '))
  if option==1:
    print('She claims to have to have left the mansion at 6p.m on the day of his disappearance.')
    time.sleep(5)
    choice_number +=1
    print("\n\nNo. of choices made: ",choice_number) 
  elif option==2:
    print("He claims that he was outside the whole evening and never came back to the mansion.")
    time.sleep(5)
    choice_number +=1
    print("\n\nNo. of choices made: ",choice_number) 
  elif option==3:
    print('She claims that she visited Mr.Edmund at around 8:45p.m for a checkup.')
    time.sleep(5)
    choice_number +=1
    print("\n\nNo. of choices made: ",choice_number) 
  else: 
    print('He claims that he never left his house that day but he heard a loud sound from the mansion at around 10:15p.m.')
    time.sleep(5)
    choice_number +=1
    print("\n\nNo. of choices made: ",choice_number) 
print('\n\nPART 3:Hope youre ready with your answers!')
time.sleep(2.5)
killer=int(input("Who was responsible for Mr.Edmund's disappearance?\nEnter their number: "))
time=int(input("What time did the incident happen leading to Edmund's disappearance?\n"
               "1.6:00p.m\n2.9:30p.m\n3.10:15p.m\n4.10:45p.m\n"
               "What is your option? "))
if killer==2 and time==3:
  print('You did it! You solved the Blackwood mansion mystery!\n'
        'To reward you,select any symbol of your choice and we\'ll make a pattern for you!')
  symbol=input("What have you chosen? ")
  for i in range(7):
    for j in range(7):
        if i==0 and (j==1 or j==5):
            print(symbol, end=" ")
        elif i==1 and (j==0 or j==2 or j==4 or j==6):
            print(symbol, end=" ")
        elif i==2 and (j==0 or j==6):
            print(symbol, end=" ")
        elif i==3 and (j==1 or j==5):
            print(symbol, end=" ")
        elif i==4 and (j==2 or j==4):
            print(symbol, end=" ")
        elif i==5 and j==3:
            print(symbol, end=" ")
        else:
            print(" ", end=" ")
    print()
  print('Congratulations!,detective',name)
elif killer==2 and time!=3:
  print("You found the killer but unfortunately not the right time.")
elif killer!=2 and time==3:
  print("You found the time but unfortunately not the killer.")
else:
  print('You didnt decode the mystery, better luck next time!')
print('\n\n                                                                                                       THE END')
  

        
    
    
    



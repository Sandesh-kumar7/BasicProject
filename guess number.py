# making the guess code for 1 to 10 number by typing manually 
number=7

attempt=0

while True:
  choice=input("play agin? yes/no: ")

  if choice=='yes':
    while True:
      guess_the_number=int(input('enter your number in range 0-10 :'))
  


      if not (0 <= guess_the_number <= 10):
         print('enter the guess_the_number in between range 0 to 10')
         continue

      attempt+=1



      if guess_the_number==number:
        print('you guess right')
        break
    
    
      elif guess_the_number<number:
        print('your guess number is lower guess higher')
    
    

      elif guess_the_number>number:
         print('your guess is higher guess lower')
    
    
      else:
        pass
  
    print(f'You guessed the number in {attempt} attempts.')
  
  elif choice=='no':
    break         
        

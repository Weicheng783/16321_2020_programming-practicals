import time, os, datetime, timeit
from difflib import SequenceMatcher

# Count total line(words) in the EnglishWords.txt
count=len(open(r"EnglishWords.txt",'r').readlines())

# Initialise some essential variable data
 # Loop data
wordnum=0
currentline=0
 # Statistics data set
wordtrue=0
wordfalse=0
totalwords=0
wordsindic=0
wordschanged=0

# Looping the whole process if user in program
while True:
 mainmanu=['1. Spell check a sentence','2. Spell check a file','0. Quit the program']
 print('------------------------------Mainmanu\n'+os.getlogin()+", Welcome to Weicheng's Spell Checker !"+'\nPlease choose a mode from the following to proceed:'+
'\n(Please enter a NUMBER for corresponding choice)')
 # Looping to show possible choices
 for idx, val in enumerate(mainmanu,start=1):
    print(' '+val)

 mainChoice=input('Type in your choice number: ')

 if mainChoice=='1':
   print('--------------------------------Mainmanu/Sentence Check')
   sentence=input('Enter your sentence to check : ')
   # Timer starts here...
   start=timeit.default_timer()

   # Do some sentences auto filtered out.
   sentence=sentence.strip('')
   sentence=sentence.strip("!,.:;?~#!^*&'1234567890")
   sentence=sentence.lower()
   sentence=sentence.replace("'",'')
   sentence=sentence.replace(",",'')
   sentence=sentence.replace(";",'')
   sentence=sentence.replace(":",'')
   sentence=sentence.replace("!",'')
   sentence=sentence.replace("#",'')
   sentence=sentence.replace('.','')
   sentence=sentence.replace('0','')
   sentence=sentence.replace('1','')
   sentence=sentence.replace('2','')
   sentence=sentence.replace('3','')
   sentence=sentence.replace('4','')
   sentence=sentence.replace('5','')
   sentence=sentence.replace('6','')
   sentence=sentence.replace('7','')
   sentence=sentence.replace('8','')
   sentence=sentence.replace('9','')
   sentence=sentence.replace('*','')

   print('After fill out it becomes: '+sentence)
   time.sleep(2) # Keep 2 secs to allow user aware
   split=sentence.split()
   marka=''
   result=''

   # Totalwords starts from 0, whereas split starts from 1.
   totalwords=len(split)-1
   # Load the whole document to the <file>
   file=[line.rstrip('\n')for line in open('EnglishWords.txt')]
   # wordnum starts from 0, whereas split starts from 1.
   while wordnum <= len(split)-1:
       # If the wordnum can be found in the document, the word is true and continues.
       while currentline <= count:
           if split[wordnum] == file[currentline]:
              wordtrue += 1
              result=result+' '+split[wordnum]
              currentline=0
              break
           # After they compared each other the process opens
           elif split[wordnum] != file[currentline]:
              # When the line compared is the last one, output not found, otherwise line +1.
              if currentline == count-1:
                  while True:
                      print('--------------------------------Mainmanu/Sentence Check/Feedback')
                      print('Ooops! < '+split[wordnum]+' > did not find in the dictionary, please enter your choice below.')
                      incorrectmanu=['1. ignore','2. mark','3. add to dictionary','4. suggest likely correct spelling']
                      for idx, val in enumerate(incorrectmanu,start=1):
                          print(' '+val)
                      incorrectchoice=input('Type in your choice number: ')
                      if incorrectchoice == '1':
                          wordfalse += 1
                          result=result+' '+split[wordnum]
                          print('< '+split[wordnum]+" > is ignored, counted as incorrectly spelt.")
                          time.sleep(2)
                          break
                      elif incorrectchoice == '2':
                          wordfalse += 1
                          marka=marka+' ?'+split[wordnum]+'?'
                          result=result+' ?'+split[wordnum]+'?'
                          print('< '+split[wordnum]+' > is marked as ?'+split[wordnum]+'? .Counted as incorrectly spelt.')
                          time.sleep(2)
                          break
                      elif incorrectchoice == '3':
                          wordsindic += 1
                          result=result+' '+split[wordnum]
                          print('< '+split[wordnum]+" > is added to the dictionary, counted as correctly spelt.")
                          time.sleep(2)
                          break
                      elif incorrectchoice == '4':
                          print('? '+split[wordnum]+" ? has the following suggestion, enter 1 to accept,or 2 to reject the word suggested.")
                          currentline=0
                          currentscore=0
                          word=''
                          while currentline <= count-1:
                              score = SequenceMatcher(None, split[wordnum], file[currentline]).ratio()
                              if currentscore <= score:
                                 word = file[currentline]
                                 currentscore = score
                              if currentline == count:
                                 currentline = 0
                                 break
                              else:
                                 currentline += 1
                          print('< '+word+' >'+'  (Match Rate:'+str(currentscore)+')')
                          while True:
                              print('--------------------------------Mainmanu/Sentence Check/Feedback/Suggestion')
                              changechoice=input('Please type in your choice: ')
                              if changechoice == '1':
                                  wordtrue += 1
                                  wordschanged += 1
                                  result=result+' '+word
                                  print('< '+word+" > is changed and added to the dictionary, counted as correctly spelt.")
                                  time.sleep(2)
                                  break
                              if changechoice == '2':
                                  wordfalse += 1
                                  marka=marka+' ?'+split[wordnum]+'?'
                                  result=result+' ?'+split[wordnum]+'?'
                                  print('< '+word+" > is rejected, ?"+split[wordnum]+"? counted as incorrectly spelt.")
                                  time.sleep(2)
                                  break
                              else:
                                  print('Your typed an invalid choice, please try again.')
                                  time.sleep(2)
                          break
                      else:
                          print('Your typed an invalid choice, please try again.')
                          time.sleep(2)
                  currentline=0
                  break
              else:
                  currentline += 1

       wordnum += 1
   end = timeit.default_timer() # Timer ends here...(Counted the whole process)

   #Finalise Sentence Checking
   print('Sentence Checking Complete!')
   print('--------------------------------Mainmanu/Sentence Check/Feedback/Summary')
   print('  < Statistics Summary >')
   print('  the total number of words : '+str(totalwords+1)+' words')
   print('  the number of words spelt correctly : '+str(wordtrue)+' words')
   print('  the number of incorrectly spelt words : '+str(wordfalse)+' words')
   print('  the number of words added to the dictionary : '+str(wordsindic)+' words')
   print('  the number of words changed by the user accepting the suggested word : '+str(wordschanged)+' words')
   curr_time=datetime.datetime.now()
   time_str=curr_time.strftime('%Y-%m-%d %H:%M:%S')
   print('  the time and date the input was spellchecked : '+ time_str)
   print('  The amount of time elapsed to spellcheck the input : '+'%s Seconds'%(end-start))
   print('')

   # Saving the result
   newfilename=input('Please enter a filename that stores the result: ')
   newfile=open(newfilename+'.txt','w')
   print('')
   newfile.write('< Statistics Summary >\n'+'the total number of words : '+str(totalwords+1)+' words\n'+'the number of words spelt correctly : '+str(wordtrue)+' words\n'+'the number of incorrectly spelt words : '+str(wordfalse)+' words\n'+'the number of words added to the dictionary : '+str(wordsindic)+' words\n'+'the number of words changed by the user accepting the suggested word : '+str(wordschanged)+' words\n'+'the time and date the input was spellchecked : '+ time_str+'\n'+'The amount of time elapsed to spellcheck the input : '+'%s Seconds'%(end-start)+'\n'+'Original input: '+sentence+'\n'+'incorrectly spelt words: '+ marka +'\n'+'result: '+ result +'\n')
   newfile.close()
   marka=''
   result=''
   print('File Created and Saved successfully!!! Return to the main in 3 secs.')

   # All values need to be initialised for next run.
   wordnum=0
   currentline=0

   wordtrue=0
   wordfalse=0
   totalwords=0
   wordsindic=0
   wordschanged=0

   time.sleep(3)

 elif mainChoice=='2':
 # File Checking: if the file exists, it pops the 'Exists' message. '0' to back to the main menu.
     while True:
      print('--------------------------------Mainmanu/Filename Check')
      filename=input('Enter your filename to check (enter 0 back to the main manu): ')
      if os.path.isfile(filename+'.txt'):
          print('--------------------------------Mainmanu/Filename Check/Feedback')
          print ('< '+filename+" > .txt does exist. Enter another file name to check a new one,or type 0 to back.")
          time.sleep(1.5)
      elif filename=='0':
          print('Exited to the main manu.')
          break
      else:
        print('--------------------------------Mainmanu/Filename Check/Feedback')
        print('The file '+filename+' does not exist! Please check again.(Press 0 to back)')
        time.sleep(1.5)

 elif mainChoice=='0':
    exit()

 else:
    # Typed any not identified words in the Mainmenu.
    print('\nOoops! You typed an invalid choice! Please type again.')

# 5/11/2020 Editied Release Ver 1.1

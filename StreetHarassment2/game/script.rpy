# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('You', color="#c8ffc8")
define s = Character('Stranger', color="#c8ffc8")
define o = Character('Coworker', color="#c8ffc8")
define b = Character('Boss', color="#c8ffc8")
image bg street frumpy = "ending/street.jpg"
image bg street sexy = "ending/street.jpg"
image bg street slob = "ending/street.jpg"
image bg office frumpy = "ending/office.jpg"
image bg office sexy = "ending/office.jpg"
image bg office slob = "ending/office.jpg"
image bg boss frumpy = "ending/boss.jpg"
image bg boss sexy = "ending/boss.jpg"
image bg boss slob = "ending/boss.jpg"
image bg club frumpy = "ending/club_frumpy.jpg"
image bg club sexy = "ending/club_sexy.jpg"
image bg club slob = "ending/club_slob.jpg"
image bg dressup = "ending/dressup.jpg"
image bg dressup shoes = "ending/dressup_shoes.jpg"
image bg dressup tops = "ending/dressup_tops.jpg"
image bg dressup bottoms = "ending/dressup_bottoms.jpg"
image bg ending slob = "ending/slob_ending.jpg"
image bg ending sexy = "ending/slut_ending.jpg"
image bg ending frumpy = "ending/frumpy_ending.jpg"
image bg ending weirdo = "ending/weirdo_ending.jpg"

# The game starts here.
label start:
    scene bg dressup
    e "Good morning!"

    e "Time to get dressed for the day. "

   


    scene bg dressup bottoms
    e "Choose your bottom clothing piece."
    menu:
        "A.":

            jump frumpy_1

        "B.":

            jump sexy_1
                
        "C.":

            jump slob_1 

# If There is one frumpy            
label frumpy_1:
        scene bg dressup
        e "Now choose your top clothing piece."
        scene bg dressup tops
        menu:
            
            e "Choose your jacket."
            
            "A.":
                jump frumpy_2
                
            "B.":
                jump frumpy_1_sexy_1
                
                
            "C.": 
                jump frumpy_1_slob_1
                
#If there is one to sexy                
label sexy_1:
        scene bg dressup 
        e "Now choose your top clothing piece."
        scene bg dressup tops
        menu:
            
            e "Choose your jacket."
            
            "A.":
                jump frumpy_1_sexy_1
                
            "B.":
                jump sexy_2
                
                
            "C.": 
                jump sexy_1_slob_1
                
# If there is one to slob                
label slob_1:
    scene bg dressup
    e "Now choose your top clothing piece."
    scene bg dressup tops
    menu:
            
            e "Choose your jacket."
            
            "A.":
                jump frumpy_1_slob_1
                
            "B.":
                jump sexy_1_slob_1
                
                
            "C.": 
                jump slob_2
                
#If there is two to frumpy               
label frumpy_2:
    scene bg dressup
    e "Now choose shoes."
    scene bg dressup shoes
    menu:
            
            e "Choose your jacket."
            
            "A.":
                jump frumpy_3
                
            "B.":
                jump frumpy_2_sexy_1
                
                
            "C.": 
                jump frumpy_2_slob_1
                
#If there is two to sexy                
label sexy_2:
        scene bg dressup
        e "Now choose shoes."
        scene bg dressup shoes
        menu:
            
            e "Choose your jacket."
            
            "A.":
                jump sexy_2_frumpy_1
                
            "B.":
                jump sexy_3
                
            "C.": 
                jump sexy_2_slob_1
                
#If there is two to slob                
label slob_2:
    scene bg dressup
    e "Now choose shoes."
    scene bg dressup shoes
    menu:
            
            e "Choose your jacket."
            
            "A.":
                jump slob_2_frumpy_1
                
            "B.":
                jump slob_2_sexy_1
                
            "C.": 
                jump slob_3

# IF there is sexy 1 and slob 1                
label sexy_1_slob_1:
    scene bg dressup
    e "Now choose shoes."
    scene bg dressup shoes
    menu:
            
            e "Choose your jacket."
            
            "A.":
                jump frumpy_2_slob_1
                
            "B.":
                jump frumpy_1_sexy_1_slob_1
                
                
            "C.": 
                jump frumpy_1_slob_2

# IF there is frumpy 1 and slob 1                
label frumpy_1_slob_1:
    scene bg dressup
    e "Now choose shoes."
    scene bg dressup shoes
    menu:
            
            e "Choose your jacket."
            
            "A.":
                jump frumpy_2_slob_1
                
            "B.":
                jump frumpy_1_sexy_1_slob_1
                
                
            "C.": 
                jump frumpy_1_slob_2
                
# IF there is frumpy 1 and sexy 1                
label frumpy_1_sexy_1:
    scene bg dressup
    e "Now choose shoes."
    scene bg dressup shoes
    menu:
            
            e "Choose your jacket."
            
            "A.":
                jump frumpy_2_sexy_1
                
            "B.":
                jump sexy_2_frumpy_1
                
                
            "C.": 
                jump frumpy_1_sexy_1_slob_1
                


####### Endings #########


                
# Frumpy is 3, means comfort is 3                
label frumpy_3:
        
        scene bg comfort 3
        e "You're super comfortable and feel like you're dressed modestly."
        scene bg street frumpy
        s "Why you covering up your curves girl! You know you want me to see that ass. Aw man, why you being so cold! Talk to me."
        scene bg office frumpy
        o "She's so unfashionable, you think she'd put on a suit and some heels sometimes.Could be worse, she could be like that slut in accounting."
        scene bg boss frumpy
        b "Ignores your contributions to a meeting." 
        scene bg ending frumpy
        e "Yay! I kept anyone from staring at my butt or boobs, but I was ignored all day."
        return

# Frumpy is 2, means comfort is 2        
label frumpy_2_sexy_1:
        scene bg comfort 2
        e "You're pretty comfortable and feel like you're dressed modestly, but being a little fashionable can be uncomfortable."
        scene bg street frumpy
        e "Why you covering up your curves girl! You know you want me to see that ass. Aw man, why you being so cold! Talk to me."
        scene bg office frumpy
        e "She's so unfashionable, you think she'd put on a suit and some heels sometimes.Could be worse, she could be like that slut in accounting."
        scene bg boss frumpy
        e "Ignores your contributions to a meeting."
        scene bg ending frumpy
        e "Yay! I kept anyone from staring at my butt or boobs, but I was ignored all day."
        return

# Comfort is 3        
label frumpy_2_slob_1:
        scene bg comfort 3
        e "You're super comfortable and feel like you're dressed modestly."
        scene bg street frumpy
        s "Why you covering up your curves girl! You know you want me to see that ass. Aw man, why you being so cold! Talk to me."
        scene bg office frumpy
        o "She's so unfashionable, you think she'd put on a suit and some heels sometimes. Could be worse, she could be like that slut in accounting."
        scene bg boss frumpy
        b "Ignores your contributions to a meeting." 
        scene bg ending frumpy
        e "Yay! I kept anyone from staring at my butt or boobs, but I was ignored all day."
        return

# Comfort is 0
label sexy_3:
        scene bg comfort 0
        e "You feel polished and beautiful and finally like you could get people to listen to you at the big meeting. But you also feel like you can't breathe for busting a button, might freeze and your feet are exploding in pain."
        scene bg street sexy
        s "Hell yeah! I need you baby, I just want to tap that right now. You look like you hand it out for free, baby~"
        scene bg office sexy
        o "What a slut! She just likes to show off because she's got the body to wear slutty outfits like that. Whose eye is she trying to catch?"
        scene bg boss sexy
        b "Finally acknowledges you in a meeting, but keeps staring at your chest."
        scene bg ending sexy
        e "Yay! I got harassed, insulted and ogled today. At least someone listened to me."
        return
        
# Comfort is 1        
label sexy_2_frumpy_1:
        scene bg comfort 1
        e "You feel pretty polished but dressed down just a little so a little bit of comfortable."
        scene bg street sexy
        s "Hell yeah! I need you baby, I just want to tap that right now. You look like you hand it out for free, baby~"
        scene bg office sexy
        o "What a slut! She just likes to show off because she's got the body to wear slutty outfits like that. Whose eye is she trying to catch?"
        scene bg boss sexy
        b "Finally acknowledges you in a meeting, but keeps staring at your chest."
        scene bg ending sexy
        e "Yay! I got harassed, insulted and ogled today. At least someone listened to me."
        return

#Comfort is 1        
label sexy_2_slob_1:
        scene bg comfort 1
        e "You feel pretty polished but dressed down just a little so a little bit of comfortable."
        scene bg street sexy
        s "Hell yeah! I need you baby, I just want to tap that right now. You look like you hand it out for free, baby~"
        scene bg office sexy
        o "What a slut! She just likes to show off because she's got the body to wear slutty outfits like that. Whose eye is she trying to catch?"
        scene bg boss sexy
        b "Ignores everything you suggested today."
        scene bg ending sexy
        e "So much for trying to balance out an outfit to be sexy enough to be heard but not dying of discomfort."
        return

# Comfort is 3        
label slob_3:
        scene bg comfort 3
        e "Today you feel tired, rushed and you know you won't have to spend time with anyone today, so rather than call in sick, you dress comfortably."
        scene bg street slob
        s "Damn, lookit that fine bottom! You work out? I work out. Gimme your number, we can “work” on dat ass together.”"
        scene bg office slob
        o "How unprofessional! There's no reason for her to dress like a slob. We have clients to impress. What's next, tromping around in fuzzy slippers and a snuggie? "
        scene bg boss slob
        b "Your outfit has been distracting to others in the office and I've had some complaints from others that they feel that you aren't upholding the dress code. No, I don't care that you have scoliosis and sometimes can't wear heels or tight pants."
        scene bg ending slob
        e "So much for assuming people would treat you fairly on a day when your appearance was not a factor in how well you do your work."
        return

# Comfort is 2        
label slob_2_sexy_1:
        scene bg comfort 2
        e "Today you feel tired, rushed and you know you won't have to spend time with anyone today, so you dress down with a little bit of sexy."
        scene bg street slob
        s "Damn, lookit that fine bottom! You work out? I work out. Gimme your number, we can “work” on dat ass together.”"
        scene bg office slob
        o "How unprofessional! There's no reason for her to dress like a slob. We have clients to impress. What's next, tromping around in fuzzy slippers and a snuggie? "
        scene bg boss slob
        b "Your outfit has been distracting to others in the office and I've had some complaints from others that they feel that you aren't upholding the dress code. No, I don't care that you have scoliosis and sometimes can't wear heels or tight pants."
        scene bg ending slob
        e "So much for making even a meager attempt to look nice, even when you feel like crap."
        return

#Comfort is 3        
label frumpy_1_slob_2:
        scene bg comfort 3
        e "Today you feel tired, rushed and you know you won't have to spend time with anyone today, so you dress comfortable but politely."
        scene bg street slob
        s "Damn, lookit that fine bottom! You work out? I work out. Gimme your number, we can “work” on dat ass together.”"
        scene bg office slob
        o "How unprofessional! There's no reason for her to dress like a slob. We have clients to impress. What's next, tromping around in fuzzy slippers and a snuggie? "
        scene bg boss slob
        b "Your outfit has been distracting to others in the office and I've had some complaints from others that they feel that you aren't upholding the dress code. No, I don't care that you have scoliosis and sometimes can't wear heels or tight pants."
        scene bg ending slob
        e "So much for making even a meager attempt to look nice, even when you feel like crap."
        return
                
#Comfort is 2
label frumpy_1_sexy_1_slob_1:
        scene bg comfort 2
        e "You are so tired of people judging you for your clothing choices that you try out the most bizarre outfits to see if you can get a good reaction at some point."
        scene bg street sexy
        s "Hell yeah! I need you baby, I just want to tap that right now. You look like you hand it out for free, baby~"
        scene bg office slob
        o "How unprofessional! There's no reason for her to dress like she got dressed in the dark. We have clients to impress. What's next, tromping around in fuzzy slippers and a snuggie? "
        scene bg boss frumpy
        b "Ignores your contributions to a meeting. Again."
        scene bg ending weirdo
        e "You decide to quit and become a monk on a remote mountain rather than deal with anyone's comments about your clothing ever again."
        return

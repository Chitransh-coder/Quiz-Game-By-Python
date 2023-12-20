import msvcrt
import threading
import time
import random
from playsound import playsound
# Limiter
global f
f = 1
global l
l = 1

# flip function
def flip():
    global f
    f -= 1
    pt = 0
    flipq = {
        "1. What is Heavy water?\n" : ["a. A Salt Solution","b. Water with Impurities","c. Deuterium Oxide","d. None of these"],
        "2. Our eyes measure how many megapixels?\n" : ["a. 176","b. 236","c. 179","d. None of these"],
        "3. The loudest volcano eruption was?\n" : ["a. Krakatoa","b. Kilimanjaro","c. Mount Fuji","d. Mauna Kea"],
        "4. The project of taking first picture of black hole was named?\n" : ["a. Event Dark Hole","b. Event Capture","c. Event Black Hole","d. Event Horizon"],
        "5. Longest word in english is used in which field?\n" : ["a. Organic Chemistry","b. Biology","c. Zoology","d. Botany"]
        }
    flipa = {
        "1. What is Heavy water?\n" : "c",
        "2. Our eyes measure how many megapixels?\n" : "a",
        "3. The loudest volcano eruption was?\n" : "b",
        "4. The project of taking first picture of black hole was named?\n" : "d",
        "5. Longest word in english is used in which field?\n" : "a"
        }
    r = random.randint(1,5)
    u = list(flipq.keys())
    q = u[r-1]
    y = flipq[q]
    print("New question is:\n")
    print(q)
    for i in range(0,4):
        print(y[i])
    a = flipa[u[r-1]]
    print("Enter your answer: ")
    ans = input()
    pt += check(ans, a, 0)
    return pt



# 50-50 function
def fifty(a):
    global l
    l -= 1
    r = random.randint(1,4)
    d = ["a","b","c","d"]
    for i in range(1,3):
        if d[r] == a:
            r = random.randint(1,4)
            continue
        else:
            d.pop(r)
            r = random.randint(1,4)
    return d



# timer function
def timer(t):
    flag = False
    while t and not flag:
        time.sleep(1)
        t -= 1
    if not flag:
        print("Time's up!")
        playsound("D:\\Resume\\Easy\\Python\\Sad.wav")
        print("Press any key to exit...")
        k = msvcrt.getch()
        exit()
    t.cancel()



# check function
def check(ans, corr, points):
    pt = 0
    if ans == corr:
        print("Correct answer!\n")
        playsound("D:\\Resume\\Easy\\Python\\TaDa.wav")
        return points
    elif ans == "q":
        print("You quit the game!\n")
        playsound("D:\\Resume\\Easy\\Python\\Sad.wav")
        print("Press any key to exit...")
        k = msvcrt.getch()
        exit()
    elif ans == "f":
        if f <= 0:
            while ans == "f":
                print("You have already used this lifeline!\n")
                print("Enter your answer: ")
                ans = input()
                check(ans, corr, points)
        else:
                print("You used the flip the question lifeline!\n")
                pt = flip()
        return pt
    elif ans == "l":
        if l <= 0:
            while ans == "l":
                print("You have already used this lifeline!\n")
                print("Enter your answer: ")
                ans = input()
                check(ans, corr, points)
        else:
            print("You used the 50-50 lifeline!\n")
            d = fifty(corr)
            print("The remaining options are:\n")
            print(d[0], d[1])
            print("Enter your answer: ")
            ans = input()
            pt = check(ans, corr, points)
        return pt
    else:
        print("Wrong answer!\n")
        playsound("D:\\Resume\\Easy\\Python\\Wrong.wav")
        print("Press any key to exit...")
        k = msvcrt.getch()
        exit()



# Main Program
print("Welcome to the Quiz Game!\n")
print("Please put your CAPS LOCK off!\n")
print("Please enter your name: ")
name = input()
print("Please enter your age: ")
age = int(input())
print("Hello, {0}!\n".format(name))
print("You can play this game if you are atleast 16 years old.\n")
if age <= 16:
    print("Sorry, you can't play this game! :(\n")
    playsound("D:\\Resume\\Easy\\Python\\Sad.wav")
    print("Press any key to exit...")
    print("Press any key to exit...")
    k = msvcrt.getch()
    exit()
print(" Congrats! You can play this game!\n")
print("Let's have a look at the rules first:\n")
time.sleep(0.5)
print("1. There are 25 questions in this game.\n")
time.sleep(3)
print("2. Each question has 4 options.\n")
time.sleep(3)
print("3. You have to type the correct letter of the option.\n")
time.sleep(3)
print("4. You have to score atleast 250 points to successfully complete the game.\n")
time.sleep(3)
print("5. Each round has its own amount of points and time limit.\n")
time.sleep(3)
print("6. There are 2 lifelines in this game, they can be used at any question.\nBut they can be used only twice.\n")
time.sleep(5)
print("7. The lifelines are:\n")
time.sleep(1)
print("   a. flip the question\n")
time.sleep(1)
print("   b. 50-50\n")
time.sleep(3)
print("8. The flip the question lifeline will change the question. To activate it, press 'f'\n")
time.sleep(5)
print("9. The 50-50 lifeline will remove 2 wrong options. To activate it, press 'l'\n")
time.sleep(5)
print("10. If you think you can't answer the question, you can quit the game by pressing 'q'.\n")
time.sleep(3)
print("11. If you answer a question incorrectly, you will lose the game.\n")
time.sleep(3)
print("Now, let's start the game!\n")
print("Game is starting...")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Starting round 1...\n")
time.sleep(1)
print("You will have 60 seconds for each question.\n")
t = threading.Timer(10.0, timer, args=(10,))
t.daemon = True
time.sleep(3)
print("Round Started!\n")
time.sleep(2)
print("1. What is the full form of LED ?\n")
t.start()
print("a. Light Emitting Device\n")
print("b. Light Emitting Dynamo\n")
print("c. Light Emitting Diode\n")
print("d. Light Emitting Detector\n")
print("Enter your answer: ")
ans = input()
pt = check(ans, "c", 0)
t.cancel()
t = threading.Timer(60.0, timer, args=(60,))
t.daemon = True
print("2. What will be the answer of: 3 + 3 - 3 * 8 / 3")
t.start()
print("a. -1\n")
print("b. 0\n")
print("c. -4\n")
print("d. 4\n")
print("Enter your answer: ")
ans = input()
pt = check(ans, "a", 7)
t.cancel()
t = threading.Timer(60.0, timer, args=(60,))
t.daemon = True
print("3. 1 AU is:\n")
t.start()
print("a. Distance between Sun and Pluto\n")
print("b. Distance between Sun and Earth\n")
print("c. Distance between Earth and Moon\n")
print("d. Distance between Sun and Mercury\n")
print("Enter your answer: ")
ans = input()
pt += check(ans, "b", 2)
t.cancel()
t = threading.Timer(60.0, timer, args=(60,))
t.daemon = True
print("4. An almost close to online(website) based games is due to?\n")
t.start()
print("a. Growth in Downloadable games\n")
print("b. High chances of malware\n")
print("c. Retirement of Websites concerned\n")
print("d. Retirement of Flash Player\n")
print("Enter your answer: ")
ans = input()
pt += check(ans, "d", 2)
t.cancel()
t = threading.Timer(60.0, timer, args=(60,))
t.daemon = True
print("5. What is the speed of Sun aroud the milky way?\n")
t.start()
print("a. 2,50,000 km/hr\n")
print("b. 2,50,000 km/s\n")
print("c. 2,50,000 km/min\n")
print("d. 2,50,000 km/day\n")
print("Enter your answer: ")
ans = input()
pt += check(ans, "b", 5)
t.cancel()
print("Great! You have completed round 1!\n and you have scored {0} points!\n".format(pt))
print("Starting round 2...\n")
time.sleep(1)
print("You will have 45 seconds for each question.\n")
t = threading.Timer(45.0, timer, args=(45,))
t.daemon = True
time.sleep(3)
print("Round Started!\n")
time.sleep(2)
print("1. Coronavirus is?\n")
t.start()
print("a. Normal-type virus\n")
print("b. RNA-type virus\n")
print("c. DNA-type virus\n")
print("d. None of the above\n")
print("Enter your answer: ")
ans = input()
pt += check(ans, "b", 0)
t = threading.Timer(45.0, timer, args=(45,))
t.daemon = True
print("2. 1 Horse power is equal to?\n")
t.start()
print("a. 746 Watts\n")
print("b. 736 Watts\n")
print("c. 756 Watts\n")
print("d. 726 Watts\n")
print("Enter your answer: ")
ans = input()
pt += check(ans, "a", 15)
t = threading.Timer(45.0, timer, args=(45,))
t.daemon = True
print("3. What will be Pressure at 100 feet below sea level?\n")
t.start()
print("a. 1.5 atm\n")
print("b. 1 atm\n")
print("c. 2 atm\n")
print("d. 1.8 atm\n")
print("Enter your answer: ")
ans = input()
pt += check(ans, "c", 5)
t.cancel()
t = threading.Timer(45.0, timer, args=(45,))
t.daemon = True
print("4. Which of the following is the smallest particle?\n")
t.start()
print("a. Atom\n")
print("b. Cell\n")
print("c. Quarks\n")
print("d. Alpha-particle\n")
print("Enter your answer: ")
ans = input()
pt += check(ans, "c", 5)
t.cancel()
t = threading.Timer(45.0, timer, args=(45,))
t.daemon = True
print("5. Who invented aeroplane before Wright Brothers?\n")
t.start()
print("a. Leonardo Da Vinci\n")
print("b. Archimedes\n")
print("c. Shivasar Thalpade\n")
print("d. None of the above\n")
print("Enter your answer: ")
ans = input()
pt += check(ans, "a", 5)
t.cancel()
print("Great! You have completed round 2!\n and you have scored {0} points!\n".format(pt))
print("Starting round 3...\n")
time.sleep(1)
print("You will have 30 seconds for each question.\n")
t = threading.Timer(30.0, timer, args=(30,))
t.daemon = True
time.sleep(3)
print("Round Started!\n")
time.sleep(2)
print("1. If 30 people jumped together from 10000 feet from sky without parachute, How many can survive?")
t.start()
print("a. 1\n")
print("b. 2\n")
print("c. 3\n")
print("d. None of the above\n")
print("Enter your answer: ")
ans = input()
pt += check(ans, "d", 5)
t.cancel()
t = threading.Timer(30.0, timer, args=(30,))
t.daemon = True
print("2. How many muscles work when we take one step?")
t.start()
print("a. 200\n")
print("b. 100\n")
print("c. 150\n")
print("d. 50\n")
print("Enter your answer: ")
ans = input()
pt += check(ans, "a", 25)
t.cancel()
t = threading.Timer(30.0, timer, args=(30,))
t.daemon = True
print("3. How many Governors are there in India?")
t.start()
print("a. 30\n")
print("b. 29\n")
print("c. 28\n")
print("d. 35\n")
print("Enter your answer: ")
ans = input()
pt += check(ans, "c", 0)
t.cancel()
t = threading.Timer(30.0, timer, args=(30,))
t.daemon = True
print("4. Which tweet of Elon Musk led to a great downfall in WhatsApp users?")
t.start()
print("a. Use Discord\n")
print("b. Use Telegram\n")
print("c. Use Instagram\n")
print("d. Use Signal\n")
print("Enter your answer: ")
ans = input()
pt += check(ans, "d", 5)
t.cancel()
t = threading.Timer(30.0, timer, args=(30,))
t.daemon = True
print("5. QR Code Scanner scans which part of QR Code?")
t.start()
print("a. Bottom\n")
print("b. Top\n")
print("c. Left\n")
print("d. Right\n")
print("Enter your answer: ")
ans = input()
pt += check(ans, "b", 5)
t.cancel()
print("Great! You have completed round 3!\n and you have scored {0} points!\n".format(pt))
print("Starting round 4...\n")
time.sleep(1)
print("You will have 15 seconds for each question.\n")
t = threading.Timer(15.0, timer, args=(15,))
t.daemon = True
time.sleep(3)
print("Round Started!\n")
time.sleep(2)
print("1. Who is the chief Scientist of WHO?")
t.start()
print("a. Tedros Adhanom\n")
print("b. Soumya Swaminathan\n")
print("c. Anthony Fauci\n")
print("d. None of the above\n")
print("Enter your answer: ")
ans = input()
pt += check(ans, "b", 25)
t.cancel()
t = threading.Timer(15.0, timer, args=(15,))
t.daemon = True
print("2. When was James Web Telescope launched?")
t.start()
print("a. 2019\n")
print("b. 2020\n")
print("c. 2021\n")
print("d. 2022\n")
print("Enter your answer: ")
ans = input()
pt += check(ans, "d", 35)
t.cancel()
t = threading.Timer(15.0, timer, args=(15,))
t.daemon = True
print("3. Which is the largest dwarf planet?")
t.start()
print("a. Pluto\n")
print("b. Eris\n")
print("c. Ceres\n")
print("d. Makemake\n")
print("Enter your answer: ")
ans = input()
pt += check(ans, "b", 10)
t.cancel()
t = threading.Timer(15.0, timer, args=(15,))
t.daemon = True
print("4. How much will the clock differ of person on top of Empire State with person on ground?")
t.start()
print("a. 1.5 microseconds\n")
print("b. 1.5 milliseconds\n")
print("c. 2.5 milliseconds\n")
print("d. 2.5 microseconds\n")
print("Enter your answer: ")
ans = input()
pt += check(ans, "b", 20)
t.cancel()
t = threading.Timer(15.0, timer, args=(15,))
t.daemon = True
print("5. What will come next in 'ABCDCB'")
t.start()
print("a. A\n")
print("b. B\n")
print("c. C\n")
print("d. D\n")
print("Enter your answer: ")
ans = input()
pt += check(ans, "a", 10)
t.cancel()
print("Great! You have completed round 4!\n and you have scored {0} points!\n".format(pt))
print("Starting round 5...\n")
time.sleep(1)
print("You will have 15 seconds for each question.\n")
t = threading.Timer(15.0, timer, args=(15,))
t.daemon = True
time.sleep(3)
print("Round Started!\n")
time.sleep(2)
print("1. Why is BP more in feet and brain?")
t.start()
print("a. Due to gravity\n")
print("b. Due to height\n")
print("c. Due to weight\n")
print("d. Due to pressure\n")
print("Enter your answer: ")
ans = input()
pt += check(ans, "a", 60)
t.cancel()
t = threading.Timer(15.0, timer, args=(15,))
t.daemon = True
print("2. Who found the value of pi for the first time?")
t.start()
print("a. Aryabhatta\n")
print("b. Archimedes\n")
print("c. Albert Einstein\n")
print("d. None of the above\n")
print("Enter your answer: ")
ans = input()
pt += check(ans, "b", 5)
t.cancel()
t = threading.Timer(15.0, timer, args=(15,))
t.daemon = True
print("3. Highest unit of byte is?")
t.start()
print("a. Zettabyte\n")
print("b. Yottabyte\n")
print("c. Exabyte\n")
print("d. None of the above\n")
print("Enter your answer: ")
ans = input()
pt += check(ans, "b", 5)
t.cancel()
t = threading.Timer(15.0, timer, args=(15,))
t.daemon = True
print("4. How many people, if jumped together will create an earthquake")
t.start()
print("a. 1,000\n")
print("b. 20,000\n")
print("c. 30,00,000n")
print("d. It is impossible\n")
print("Enter your answer: ")
ans = input()
pt += check(ans, "d", 0)
t.cancel()
t = threading.Timer(15.0, timer, args=(15,))
t.daemon = True
print("5. Who is the CEO of IBM?")
t.start()
print("a. Satya Nadella\n")
print("b. Sundar Pichai\n")
print("c. Arvind Krishna\n")
print("d. None of the above\n")
print("Enter your answer: ")
ans = input()
pt += check(ans, "c", 5)
t.cancel()
print("Congratulations! You have completed the game!\n")
time.sleep(4)
print("Your score is {0} points!\nEnjoy!".format(pt))
playsound("D:\\Resume\\Easy\\Python\\TaDa.wav")
playsound("D:\\Resume\\Easy\\Python\\TaDa.wav")
playsound("D:\\Resume\\Easy\\Python\\TaDa.wav")
print("Do you want to play again?\n")
print("Press 'y' for yes and 'n' for no.\n")
ans = input()
if ans == "y":
    print("Restarting game...")
    time.sleep(1)
    exec(open("D:\\Resume\\Easy\\Quiz_Game.py").read())
else:
    print("Do you like this game?\n")
    print("Press 'y' for yes and 'n' for no.\n")
    ans = input()
    if ans == "y":
        print("Thank you for playing this game!\n")
        print("Press any key to exit...")
        k = msvcrt.getch()
        exit()
    else:
        print("Thanks for your feedback. I will try my best to improve this game\n")
        print("Press any key to exit...")
        k = msvcrt.getch()
        exit()
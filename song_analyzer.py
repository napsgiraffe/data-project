"""
Will split this up among different helper functions
-> A function that takes an input block of text and converts it into a series of words (list of str)
words should all be lowercase and all punctuation should be removed (?)
str -> list of (str)
-> A function that takes in formatted lyrics and outputs the next-word likelihoods
list of (str) -> lyric_probs = dictionary(first_words, dictionary(next_words, probabilities) )

-> A function that takes the next-word likelihoods and, given a starting word (that is in the original lyrics),
generates new words based off the last word printed (keeps going until quit is typed).
lyric_probs -> str
"""
from collections import Counter, defaultdict
import random
import time

def lyric_list(lyric_text):
   split_lyrics_raw = lyric_text.split()
    # remove random junk like periods, commas, etc. This should primarily be done by the data inputter, though.
   unwanted_characters = {".",",","!","?","\"",""}
   # also make every word lowercase.
   split_lyrics_simplified = [word.lower() for word in split_lyrics_raw if word not in unwanted_characters]
   return split_lyrics_simplified

def lyric_probs(lyrics):
    word_counts = defaultdict(Counter)
    for word, next_word in zip(lyrics, lyrics[1:]):
        word_counts[word][next_word] += 1
    #create probability mass function off of this wordcount.
    pmf = {
        word: {next_word: count / sum(next_words.values()) for next_word, count in next_words.items()}
        for word, next_words in word_counts.items()
    }
    return pmf

def random_lyric_generator(lyric_text):
    pmf = lyric_probs(lyric_list(lyric_text))
    def next_word_generator(input_word):
        if input_word in pmf:
            options = pmf[input_word]
            # print(pmf[input_word]) # comment this out for better lyrics printing
            chosen_word = random.choices(list(options), weights=options.values())[0]
            prob_raw = pmf[input_word][chosen_word];
            rounded_prob = f"{prob_raw:.2f}"
            return chosen_word, rounded_prob
        else:
            return next(iter(pmf.items()))[0], 1

    print("Welcome to the Song lyric-lengthener-model (Song LLM).")
    time.sleep(1)
    print("Please enter the first word of the desired lyrics.")
    time.sleep(1)
    last_word = input("Then, lyrics will continue generating when you press enter,\nuntil you input any other key: ")
    # last_word = next_word_generator(first_word)
    user_input = ""
    print(last_word)
    while user_input == "":
        last_word, chance = (next_word_generator(last_word))
        user_input = input(f"{last_word} ({chance}) ")

if __name__ == "__main__":
    flashing_lights = """
Flashing lights
Flashing lights
Flashing lights
Flashing lights
She don't believe in shootin' stars
But she believe in shoes and cars
Wood floors in the new apartment
Couture from the store's departments
You more like love to start
I'm more of the trips to Florida
Ordered the hors d'oeuvres views of the water
Straight from a page of your favorite author
And the weather so breezy
Man why can't life always be this easy
She in the mirror dancin' so sleazy
I get a call like Where are you, Yeezy
And try to hit you with the ol-wu-wopte
'Til I got flashed by the paparazzi
man these people got me
I hate these people more than the Gestapo
As I recall I know you love to show off
But I never thought that you would take it this far
What do I know Flashing lights
What do I know Flashing lights know
I know it's been a while sweetheart
We hardly talk I was doin' my thang
I know I was foul baby aye babe
Lately you've been all on my brain brain
And if somebody would've told me a month ago
Frontin' though yo I wouldn't wanna know
If somebody would've told me a year ago
It'll go get this difficult difficult
Feelin' like Katrina with no FEMA
Like Martin with no Gina
Like a flight with no Visa
First class with the seat back I still see ya
In my past you on the other side of the glass
Of my memory's Museum
I'm just sayin' Hey Mona Lisa
Come home you know you can't roam without Caesar
As I recall I know you love to show off off
But I never thought that you would take it this far far
What do I know Flashing lights
What do I know Flashing lights know
As you recall you know I love to show off off
But you never thought that I would take it this far far
What do you know Flashing lights
What do you know Flashing lights know
Flashing lights
Flashing lights"""

    all_of_the_lights = """
    All of the lights 
Lights lights All of the lights
Turn up the lights in here baby
Extra bright I want y'all to see this
Turn up the lights in here baby
You know what I need want you to see everything
Want you to see all of the lights
Fast cars shooting stars
All of the lights all of the lights
Until it's Vegas everywhere we are all of the lights
If you want it you can get it for the rest of your life
If you want it you can get it for the rest of your life
Somethin' wrong I hold my head
MJ gone our idol dead
I slapped my girl she called the feds
I did that time and spent that bread
I'm heading home I'm almost there
I'm on my way headed up the stairs
To my surprise, a poser replacing me
I had to take him to that ghetto university
Lights
Cop lights flashlights spotlights
Strobe lights street lights
All of the lights, all of the lights
Fast life drug life thug life
Rock life every night all of the lights
Turn up the lights in here baby
Extra bright I want y'all to see this
Turn up the lights in here baby
You know what I need want you to see everything
Want you to see all of the lights
Restraining order can't see my daughter
Her mother brother grandmother hate me in that order
Public visitation we met at Borders
Told her she take me back I'll be more supportive
I made mistakes I bumped my head
Them courts sucked me dry I spent that bread
She need her daddy baby please
Can't let her grow up in that ghetto university
Lights
Cop lights flashlights spotlights
Strobe lights street lights
All of the lights all of the lights
Fast life drug life thug life
Rock life every night all of the lights
Turn up the lights in here baby
Extra bright I want y'all to see this
Turn up the lights in here baby
You know what I need want you to see everything
Want you to see all of the lights
I'm gettin' mine baby
Gotta let these people know yeah
Gettin' right babe
You should go and get your own
I'm gettin' mine baby
Gotta let these people know yeah
Gettin' right babe
You should go and get your own
Unemployment line credit card declined
Did I not mention I was about to lose my mind
And also was about to do that line 
'Kay okay you know we going all the way this time
We going all the way this time
We going all the way this time
Turn up the lights in here baby
Extra bright I want y'all to see this
Turn up the lights in here baby
You know what I need want you to see everything
Want you to see all of the lights
Whoa whoa oh
I tried to tell you but all I could say was oh
Whoa whoa oh
I tried to tell you but all I could say was oh
"""
    random_lyric_generator(flashing_lights)
    print("Thanks for playing!")
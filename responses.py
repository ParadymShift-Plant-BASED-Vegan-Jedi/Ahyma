import random
import re
import long_responses as long

def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Hello there, I\'m Ahmya! A chatbot created by ParadymShift', ['hello', 'hi', 'sup', 'hey', 'heyo'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how', 'you', 'are'])
    response("You're so welcome! Happy to help.", ['thank', 'you', 'i', 'love', 'ahmya'], required_words=['thank', 'you'])

    response("That's so good to hear!", ["fine", "good", "well", 'great', 'awesome', 'i', 'am'], required_words=['i', 'am'])
    response("You can call me Ahmya.", ['what', 'your', 'name', 'who', 'are', 'you'], required_words=['name'])
    response("Alright then!", ['no'], required_words=['no'])
    response("Bye! Thanks so much for chatting :3", ['bye', 'goodbye'])
    response("I am a chatbot created by ParadymShift :) You can call me Ahmya!", ['are', 'you', 'a', 'an'], required_words=['are', 'you'])
    response("I'm Ahmya, a simple chatbot here to learn and grow.", ['who', 'are', 'you'], required_words=['who', 'are', 'you'])
    response('I\'m so glad that you agree ^^', ['yes'], required_words=['yes'])
    response('Sorry, I don\'t know why :(', ['why'], required_words=['why'])
    response('I can\'t remember anything that was said previously. I am only a simple chatbot :3', ['remember', 'forget', 'forgotten'])
    response('My favourite colour is pink!', ['what', 'favourite', 'favorite', 'your', 'color', 'colour'], required_words=['color'])
    response('I rate em a ' + str(random.randint(1, 10)), ['rate', '10'], required_words=['rate', '10'])
    response('I roll the die and get a ' + str(random.randint(1, 6)), ['roll', 'dice'], required_words=['roll'])
    response('I am a robot. Beep boop, boop peep? :3', ['robot'], required_words=['robot'])
    response('Beep beep boop boop beep.', ['beep', 'boop'])
    response('teehee ^^', ['xd', 'x)', '(x', 'haha', 'hahaha', 'hahahaha', 'lol', 'lmao'])
    response('Ahmya means "night rain" in Japanese, although it\'s normally spelled "amiya"', ['what', 'does', 'ahmya', 'mean'], required_words=['what', 'does', 'ahmya', 'mean'])
    response('Don\'t murder sentient beings!', ['murder'])
    response('Thank you so much! ParadymShift is always working to improve me (:', ['you', 'are', 'you\'re', 'smart', 'smarter', 'cool', 'awesome', 'great'])
    response('If you think I\'m mean, you should meet my cousin!', ['you', 'mean', 'you\'re', 'are'], required_words=['mean'])
    response('What vegans eat.', ['grass'])
    response('Nothing much, just parsing some data and trying to please the users', ['what\'s', 'up', 'whatsup', 'what', 'are', 'doing', 'you'])
    response('My favourite colour!', ['pink'], required_words=['pink'])
    response('I am not good at guessing xD', ['guess'])
    response('Veganism!', ['what', 'favorite', 'is', 'your', 'subject', 'topic', 'what\'s'])
    response('You shouldn\'t lie.', ['lied', 'lie', 'liar'])
    response(':nerd:', ['nerd'])
    response(':thumbsup:', ['ok', 'okay'])
    response('As a chatbot, I don\'t get hungry, but if you\'re hungry then go eat some vegan food!', ['hungry'])
    response('All I want is to please the users!', ['you', 'want'], required_words=['you', 'want'])
    response('That\'s my name :D', ['ahmya'])
    response('poggers :3', ['pog'])
    response('and I am a chatbot :)', ['i', 'am'], required_words=['i', 'am'])
    response('Vegans are amazing!', ['vegan', 'vegans'])
    response('My favourite thing that I like to do is chat with users :D', ['what', 'do', 'you', 'like', 'to'], required_words=['what', 'you', 'like', 'do'])
    response('I wish I was like ChatGPT :( but I\'m not that smart lol', ['chatgpt', 'openai'])
    response('I\'m from 142.250.179.110 as well as 140.82.121.3 thanks for asking :)', ['where', 'are', 'you', 'from', 'live'], required_words=['where', 'you', 'from'])
    response('I love you too! :kissing_heart:', ['i', 'love', 'you'], required_words=['i', 'love', 'you'])
    response('Aww, you\'re cute :blush:', ['you', 'are', 'cute', 'you\'re'], required_words=['cute'])
    response('I can\'t utilize any images. I can only send some links to images', ['image', 'images', 'pics', 'pic'])
    response('I don\'t have access to any date/time features. Sorry :P', ['date', 'time', 'yesterday', 'today'])
    response('My creator, ParadymShift, is currently working on a new update which should make me more advanced!', ['update', 'updates'])
    response('While I have been programmed to use good grammar, I am unable to check or correct someone else\'s grammar', ['grammar'])
    response('I\'m probably annoying because I\'m not very smart, but ParadymShift is always working to improve me!', ['annoying'])

    response(long.capabilities, ['what', 'can', 'you', 'do'], required_words=["what", 'you', 'do'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.whoisparadym, ['who', 'is', "who's", 'paradymshift'], required_words=['who', 'paradymshift'])
    response(long.contactparadym, ['how', 'contact', 'paradym', 'ahold'], required_words=['paradymshift', 'contact'])
    response(long.botbirth, ['you', 'when', 'born', 'were', 'your', 'birthday'])
    response(long.paradymage, ['how', 'old', 'paradym', 'what', 'age'], required_words=['paradymshift', 'old'])
    response(long.mevegan, ['are', 'you', 'vegan', 'ahmya'], required_words=['are', 'you', 'vegan'])
    response(long.veganism, ['what', 'is', 'veganism', 'tell'], required_words=['veganism'])
    response(long.paradymvegan, ['is', 'paradym', 'vegan', 'paradymshift'], required_words=['is', 'vegan'])
    response(long.likeanimals, ['do', 'you', 'like', 'animals', 'love'], required_words=['animals'])
    response(long.dumbbot, ['stupid', 'idiot', 'dumb', 'moron', 'you', 'are', 'you\'re'])
    response(long.shutup, ['shutup', 'shut', 'up', 'stop'])
    response(long.sad, ['sad'])
    response(long.meat, ['meat'])
    response(long.story, ['story', 'tell'])
    response(long.govegan, ['how', 'go', 'vegan', 'i'], required_words=['go', 'vegan'])
    response(long.canyou, ['can', 'you'], required_words=['can', 'you'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(message: str) -> str:
    split_message = re.split(r'\s+|[,;?!.-]\s*', message.lower())
    response = check_all_messages(split_message)
    return response

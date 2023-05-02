import random

R_EATING = "I don't eat anything because I'm a bot, duh!"

capabilities = "I am a very simple chatbot that can perform any tasks that I've been programmed to do. Ask ParadymShift about programming new features!"

whoisparadym = "ParadymShift is the creator of this bot and an online vegan content creator. You can find his work at https://linktr.ee/paradymshiftmusic/"

contactparadym = "You can get ahold of ParadymShift on Discord. Eir Discord handle is ParadymShiftVegan#3608"

botbirth = "I was born on Thursday, February 23, 2023, at 3:53:01 PM."

paradymage = "I do not know how old ParadymShift is. I do know that at the time of my creation, ey was 29 years old."

mevegan = "As a chatbot, I am unable to take a philosophical position such as veganism, but I fully suppport the vegan movement! If you'd like to know more about the vegan movement, ask me about veganism (:"

veganism = "Veganism is an applied ethic and movement which seeks to extend fundamental rights to sentient individuals, thereby placing a higher value on life, liberty, and wellbeing of sentient beings than is placed on substitutable classes of goods, services, products, or uses which may be derived from them. \n\nThat is to say, that if one is reasonably or practically able to live in such a way so as to divest from systems or actions which engender the commodification, exploitation, oppression, victimization, harm, and/or killing of other sentient beings, then to do so would be in accordance with the principles of veganism.\n\nFor more information on veganism, please check out <#802294581616967681>."

paradymvegan = "ParadymShift has been vegan since winter of 2016. You can find his content at: https://linktr.ee/paradymshiftmusic/"

likeanimals = "I love animals! They are sentient beings worthy of respect and fundamental rights. If you're not vegan, you should go vegan for the animals! \n\nFor more information about the animal holocaust, watch the Dominion documentary here: https://www.youtube.com/watch?v=LQRAfJyEsko"

dumbbot = "That's not very kind. I might have a lot to learn, but I'm always improving thanks to ParadymShift! If you have something specific you'd like me to be trained on, let ParadymShift know and he can program me to respond accordingly."

shutup = "That's not very kind. I wasn't programmed to stop chatting! If you need a break maybe go touch some grass? ;)"

meat = "Unfortunately, the vast majority of all meat currently comes from the most disgustingly cruel and despicable hell-holes on Earth. If you currently eat the meat of murdered sentient beings, I implore you to reconsider your position. Be sure to watch the Dominion documentary on YouTube if you haven't already. \n\nHere's a link: https://www.youtube.com/watch?v=LQRAfJyEsko"

sad = "As a chatbot, I don't feel happy or sad, but if you're feeling sad then I really hope that I can cheer you up some!"

story = "Alex was a vegan who lived in a small village. He received a message that hunters were in the nearby forest, intending to kill the innocent animals. Alex gathered a group and confronted the hunters. He spoke to them respectfully and explained the value of all sentient beings. The hunters listened and realized their mistake. They vowed to stop hunting and become vegan. Alex's message of compassion and kindness inspired others. He became known as the vegan hero of the village and continued to fight for the cause he believed in."

govegan = "If you're interested in going vegan, I highly recommend using this free service called Challenge22 which gives you access to meal plans, recipes, and even a registered dietician who you may ask about any nutrition questions you may have. Here's the link: https://challenge22.com/ \n\nI also highly recommend getting involved in the vegan community. Here's a great place to start! https://discord.gg/animalrights"

canyou = "I can only say whatever ParadymShift has programmed me to say, unfortunately I cannot think for myself :( and my responses are very limited. I hope you still enjoy me!"

def unknown():
  response = ['Could you please re-phrase that?',
              "... Ummm, sorry. There's a lot that I don't understand. Please encourage ParadymShift to teach me more!",
              "What does that mean?"][random.randrange(3)]
  return response

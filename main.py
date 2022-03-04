from bs4 import BeautifulSoup
import googlesearch,nltk,heapq,requests,re,socket
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
updater = Updater("use your telegram api key by BOTFATHER",use_context=True)
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello user, Welcome to the Bot Please write /help to see the commands available.")
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Hello user we have some search patterns in our bot
    as try any question , you can explore the answer
    /ip_add ---> for address of list 
    direct query ---> which gives googles answer
    /name-------->which gives you the name
    /creator----->which gives the creators name
    /tel_movies---->for telugu trending movies 
    /india_trend----->indias trending movies
    /movies_hyd------->book my show movies available at Hyderabad
    /movies_kochi------>book my show movies available at Kochi
    /movies_delhi------->book my show movies available at delhi
    /movies_mumbai------->book my show movies at mumbai
    /movies_ahmedabad------>book my show movies at ahmedabad
    /movies_banglore--------->book my show movies at banglore
    /movies_chandigarh--------->book my show movies at chandigarh
    /movies_pune---------------->book my show movies at pune
    /movies_chennai-------------->book my show movies at chennai
    /movies_kolkata---------------->book my show movies at kolkata
    /<enter the ip address for the searching>---------->shows the Ip information which was given
    user can cross check the movies from book my show website""")
def ip(update:Update, context:CallbackContext):
    google=socket.gethostbyname('www.google.com')
    amazon = socket.gethostbyname('www.amazon.com')
    bing = socket.gethostbyname('www.bing.com')
    facebook = socket.gethostbyname('www.facebook.com')
    update.message.reply_text('the googles ip address is %s' %google)
    update.message.reply_text('the bing ip %s' %bing)
    update.message.reply_text('the amazon ip is %s' %amazon)
    update.message.reply_text('the facebook ip is%s' %facebook )
def text(update:Update,context:CallbackContext):
    from third_one import ip_addre
    clean=re.sub('/','',update.message.text)
    a=ip_addre(clean)
    update.message.reply_text('%s'%a)
def stock(update:Update,context:CallbackContext):
    name='BILLA'
    update.message.reply_text('%s'%name)
def creator(update:Update,context:CallbackContext):
    cre='My boss'
    update.message.reply_text('%s' %cre)
def chat_link(update:Update,context:CallbackContext):
    update.message.reply_text('the chat is %s'%update.message.chat_id)
def telugu_movies(update:Update,context:CallbackContext):
    lists = []
    percentages = []
    final_outpt=[]
    req = requests.get('https://m.imdb.com/india/telugu/')
    text = req.text
    soap = BeautifulSoup(text, 'html.parser')
    for links in soap.find_all('span', class_='trending-list-rank-item-name'):
        e = links.get_text()
        lists.append(e)
    for a in soap.find_all('span', class_='trending-list-rank-item-share'):
        percentage = a.get_text()
        percentages.append(percentage)
    for i in range(len(percentages)):
        a=lists[i]+'--'+percentages[i]
        final_outpt.append(a)
    update.message.reply_text('%s'%final_outpt)
def treding(update:Update,context:CallbackContext):
    india='https://m.imdb.com/india/trending/'
    mvs=[]
    req = requests.get(india)
    text=req.text
    soap=BeautifulSoup(text,'html.parser')
    for links in soap.find_all('i'):
        movies=links.get_text()
        mvs.append(movies)
    update.message.reply_text('%s'%mvs)
def google_custom(update: Update, context: CallbackContext):
    inp = update.message.text
    para = []
    output = []
    a = googlesearch.search(inp)
    for b in a[1:4]:
        try:
            r = requests.get(b)
            data = r.text
            soup = BeautifulSoup(data, features='lxml')
            for link in soup.find_all('p'):
                g = link.get_text()
                token = nltk.tokenize.sent_tokenize(g)
                para.append(token)
        except requests.exceptions.MissingSchema as pe:
            print(pe)
    def r(para):
        for s in para:
            if type(s) == list:
                r(s)
            else:
                output.append(s)
    r(para)
    stri = ' '.join(map(str, output))
    text = stri.lower()
    clean = re.sub('[^a-zA-Z]', ' ', text)
    clean2 = re.sub('\s +', ' ', clean)
    sentence_list = nltk.sent_tokenize(text)
    stopwords = nltk.corpus.stopwords.words('english')
    word_frequencies = {}
    for word in nltk.word_tokenize(clean2):
        if word not in stopwords:
            if word not in word_frequencies:
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
    maximum_frequency = max(word_frequencies.values())
    for word in word_frequencies:
        word_frequencies[word] = word_frequencies[word] / maximum_frequency
    sentence_scores = {}
    for sentence in sentence_list:
        for word in nltk.word_tokenize(sentence):
            if word in word_frequencies and len(sentence.split(' ')) < 30:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_frequencies[word]
                else:
                    sentence_scores[sentence] += word_frequencies[word]
    summary = heapq.nlargest(5, sentence_scores, key=sentence_scores.get)
    sentence = ''.join(summary)
    pr = re.sub('\n+', ' ', sentence)
    update.message.reply_text("'%s'" % pr)
def movies(update:Update, context:CallbackContext):
    wec = []
    abc=[]
    url = 'https://in.bookmyshow.com/explore/movies-hyderabad/'
    req = requests.get(url)
    text = req.text
    soap = BeautifulSoup(text, 'html.parser')
    for links in soap.find_all("div", class_=['style__StyledText-sc-7o7nez-0', 'btojmA']):
        p = links.get_text()
        wec.append(p)
    for i in wec:
        q=['Tamil, Telugu','Bengali','Gujarati','Telugu, Tamil, Malayalam, Kannada, Hindi','English, Hindi','Hindi, Tamil, Telugu, Kannada, Malayalam','English 7D','Punjabi','Marathi','Kannada, Telugu, Hindi','English','Telugu','Hindi','Japanese','Tamil','Hindi, Telugu','Malayalam','Browse by Cinemas','Kannada','Apply','Telugu, Hindi','Tamil, Telugu, Kannada','English, Hindi, Tamil, Telugu, Kannada','English, Hindi, Tamil, Telugu','UA','U','A']
        if i not in q:
            update.message.reply_text('%s'%i)
def movies_kochi(update:Update,context:CallbackContext):
    import requests
    from bs4 import BeautifulSoup
    abc=[]
    wec = []
    url = 'https://in.bookmyshow.com/explore/movies-kochi'
    req = requests.get(url)
    text = req.text
    soap = BeautifulSoup(text, 'html.parser')
    for links in soap.find_all("div", class_=['style__StyledText-sc-7o7nez-0', 'btojmA']):
        p = links.get_text()
        # print(p)
        wec.append(p)
    for i in wec:
        q = ['Tamil, Telugu','Bengali', 'Gujarati', 'Telugu, Tamil, Malayalam, Kannada, Hindi', 'English, Hindi',
             'Hindi, Tamil, Telugu, Kannada, Malayalam', 'English 7D', 'Punjabi', 'Marathi', 'Kannada, Telugu, Hindi',
             'English', 'Telugu', 'Hindi', 'Japanese', 'Tamil', 'Hindi, Telugu', 'Malayalam', 'Browse by Cinemas',
             'Kannada', 'Apply', 'Telugu, Hindi', 'Tamil, Telugu, Kannada', 'English, Hindi, Tamil, Telugu, Kannada',
             'English, Hindi, Tamil, Telugu', 'UA', 'U', 'A']
        if i not in q:
            abc.append(i)
            update.message.reply_text('%s' %i)
def movies_mumbai(update:Update,context:CallbackContext):
    import requests
    from bs4 import BeautifulSoup
    abc=[]
    wec = []
    url = 'https://in.bookmyshow.com/explore/movies-mumbai'
    req = requests.get(url)
    text = req.text
    soap = BeautifulSoup(text, 'html.parser')
    for links in soap.find_all("div", class_=['style__StyledText-sc-7o7nez-0', 'btojmA']):
        p = links.get_text()
        # print(p)
        wec.append(p)
    for i in wec:
        q = ['Tamil, Telugu','Bengali', 'Gujarati', 'Telugu, Tamil, Malayalam, Kannada, Hindi', 'English, Hindi',
             'Hindi, Tamil, Telugu, Kannada, Malayalam', 'English 7D', 'Punjabi', 'Marathi', 'Kannada, Telugu, Hindi',
             'English', 'Telugu', 'Hindi', 'Japanese', 'Tamil', 'Hindi, Telugu', 'Malayalam', 'Browse by Cinemas',
             'Kannada', 'Apply', 'Telugu, Hindi', 'Tamil, Telugu, Kannada', 'English, Hindi, Tamil, Telugu, Kannada',
             'English, Hindi, Tamil, Telugu', 'UA', 'U', 'A']
        if i not in q:
            abc.append(i)
            update.message.reply_text('%s' %i)
def movies_delhi(update:Update,context:CallbackContext):
    import requests
    from bs4 import BeautifulSoup
    abc=[]
    wec = []
    url = 'https://in.bookmyshow.com/explore/movies-national-capital-region-ncr'
    req = requests.get(url)
    text = req.text
    soap = BeautifulSoup(text, 'html.parser')
    for links in soap.find_all("div", class_=['style__StyledText-sc-7o7nez-0', 'btojmA']):
        p = links.get_text()
        # print(p)
        wec.append(p)
    for i in wec:
        q = ['Tamil, Telugu','Bengali', 'Gujarati', 'Telugu, Tamil, Malayalam, Kannada, Hindi', 'English, Hindi',
             'Hindi, Tamil, Telugu, Kannada, Malayalam', 'English 7D', 'Punjabi', 'Marathi', 'Kannada, Telugu, Hindi',
             'English', 'Telugu', 'Hindi', 'Japanese', 'Tamil', 'Hindi, Telugu', 'Malayalam', 'Browse by Cinemas',
             'Kannada', 'Apply', 'Telugu, Hindi', 'Tamil, Telugu, Kannada', 'English, Hindi, Tamil, Telugu, Kannada',
             'English, Hindi, Tamil, Telugu', 'UA', 'U', 'A']
        if i not in q:
            abc.append(i)
            update.message.reply_text('%s' %i)
def movies_bengaluru(update:Update,context:CallbackContext):
    import requests
    from bs4 import BeautifulSoup
    wec = []
    abc=[]
    url = 'https://in.bookmyshow.com/explore/movies-bengaluru'
    req = requests.get(url)
    text = req.text
    soap = BeautifulSoup(text, 'html.parser')
    for links in soap.find_all("div", class_=['style__StyledText-sc-7o7nez-0', 'btojmA']):
        p = links.get_text()
        # print(p)
        wec.append(p)
    for i in wec:
        q = ['Tamil, Telugu','Bengali', 'Gujarati', 'Telugu, Tamil, Malayalam, Kannada, Hindi', 'English, Hindi',
             'Hindi, Tamil, Telugu, Kannada, Malayalam', 'English 7D', 'Punjabi', 'Marathi', 'Kannada, Telugu, Hindi',
             'English', 'Telugu', 'Hindi', 'Japanese', 'Tamil', 'Hindi, Telugu', 'Malayalam', 'Browse by Cinemas',
             'Kannada', 'Apply', 'Telugu, Hindi', 'Tamil, Telugu, Kannada', 'English, Hindi, Tamil, Telugu, Kannada',
             'English, Hindi, Tamil, Telugu', 'UA', 'U', 'A']
        if i not in q:
            abc.append(i)
            update.message.reply_text('%s'%i)
def movies_chandigarh(update:Update,context:CallbackContext):
    import requests
    from bs4 import BeautifulSoup
    wec = []
    abc=[]
    url = 'https://in.bookmyshow.com/explore/movies-chandigarh'
    req = requests.get(url)
    text = req.text
    soap = BeautifulSoup(text, 'html.parser')
    for links in soap.find_all("div", class_=['style__StyledText-sc-7o7nez-0', 'btojmA']):
        p = links.get_text()
        # print(p)
        wec.append(p)
    for i in wec:
        q = ['Tamil, Telugu','Bengali', 'Gujarati', 'Telugu, Tamil, Malayalam, Kannada, Hindi', 'English, Hindi',
             'Hindi, Tamil, Telugu, Kannada, Malayalam', 'English 7D', 'Punjabi', 'Marathi', 'Kannada, Telugu, Hindi',
             'English', 'Telugu', 'Hindi', 'Japanese', 'Tamil', 'Hindi, Telugu', 'Malayalam', 'Browse by Cinemas',
             'Kannada', 'Apply', 'Telugu, Hindi', 'Tamil, Telugu, Kannada', 'English, Hindi, Tamil, Telugu, Kannada',
             'English, Hindi, Tamil, Telugu', 'UA', 'U', 'A']
        if i not in q:
            abc.append(i)
            update.message.reply_text('%s' %i)
def movies_ahmedabad(update:Update,context:CallbackContext):
    import requests
    from bs4 import BeautifulSoup
    wec = []
    abc=[]
    url = 'https://in.bookmyshow.com/explore/movies-ahmedabad'
    req = requests.get(url)
    text = req.text
    soap = BeautifulSoup(text, 'html.parser')
    for links in soap.find_all("div", class_=['style__StyledText-sc-7o7nez-0', 'btojmA']):
        p = links.get_text()
        # print(p)
        wec.append(p)
    for i in wec:
        q = ['Tamil, Telugu','Bengali', 'Gujarati', 'Telugu, Tamil, Malayalam, Kannada, Hindi', 'English, Hindi',
             'Hindi, Tamil, Telugu, Kannada, Malayalam', 'English 7D', 'Punjabi', 'Marathi', 'Kannada, Telugu, Hindi',
             'English', 'Telugu', 'Hindi', 'Japanese', 'Tamil', 'Hindi, Telugu', 'Malayalam', 'Browse by Cinemas',
             'Kannada', 'Apply', 'Telugu, Hindi', 'Tamil, Telugu, Kannada', 'English, Hindi, Tamil, Telugu, Kannada',
             'English, Hindi, Tamil, Telugu', 'UA', 'U', 'A']
        if i not in q:
            abc.append(i)
            update.message.reply_text('%s' %i)
def movies_pune(update:Update,context:CallbackContext):
    import requests
    from bs4 import BeautifulSoup
    wec = []
    abc=[]
    url = 'https://in.bookmyshow.com/explore/movies-pune'
    req = requests.get(url)
    text = req.text
    soap = BeautifulSoup(text, 'html.parser')
    for links in soap.find_all("div", class_=['style__StyledText-sc-7o7nez-0', 'btojmA']):
        p = links.get_text()
        # print(p)
        wec.append(p)
    for i in wec:
        q = ['Tamil, Telugu','Bengali', 'Gujarati', 'Telugu, Tamil, Malayalam, Kannada, Hindi', 'English, Hindi',
             'Hindi, Tamil, Telugu, Kannada, Malayalam', 'English 7D', 'Punjabi', 'Marathi', 'Kannada, Telugu, Hindi',
             'English', 'Telugu', 'Hindi', 'Japanese', 'Tamil', 'Hindi, Telugu', 'Malayalam', 'Browse by Cinemas',
             'Kannada', 'Apply', 'Telugu, Hindi', 'Tamil, Telugu, Kannada', 'English, Hindi, Tamil, Telugu, Kannada',
             'English, Hindi, Tamil, Telugu', 'UA', 'U', 'A']
        if i not in q:
            abc.append(i)
            update.message.reply_text('%s' %i)
def movies_chennai(update:Update,context:CallbackContext):
    import requests
    from bs4 import BeautifulSoup
    wec = []
    abc=[]
    url = 'https://in.bookmyshow.com/explore/movies-chennai'
    req = requests.get(url)
    text = req.text
    soap = BeautifulSoup(text, 'html.parser')
    for links in soap.find_all("div", class_=['style__StyledText-sc-7o7nez-0', 'btojmA']):
        p = links.get_text()
        # print(p)
        wec.append(p)
    for i in wec:
        q = ['Tamil, Telugu','Bengali', 'Gujarati', 'Telugu, Tamil, Malayalam, Kannada, Hindi', 'English, Hindi',
             'Hindi, Tamil, Telugu, Kannada, Malayalam', 'English 7D', 'Punjabi', 'Marathi', 'Kannada, Telugu, Hindi',
             'English', 'Telugu', 'Hindi', 'Japanese', 'Tamil', 'Hindi, Telugu', 'Malayalam', 'Browse by Cinemas',
             'Kannada', 'Apply', 'Telugu, Hindi', 'Tamil, Telugu, Kannada', 'English, Hindi, Tamil, Telugu, Kannada',
             'English, Hindi, Tamil, Telugu', 'UA', 'U', 'A']
        if i not in q:
            abc.append(i)
            update.message.reply_text('%s' %i)
def movies_kolkata(update:Update,context:CallbackContext):
    import requests
    from bs4 import BeautifulSoup
    wec = []
    abc=[]
    url = 'https://in.bookmyshow.com/explore/movies-kolkata'
    req = requests.get(url)
    text = req.text
    soap = BeautifulSoup(text, 'html.parser')
    for links in soap.find_all("div", class_=['style__StyledText-sc-7o7nez-0', 'btojmA']):
        p = links.get_text()
        # print(p)
        wec.append(p)
    for i in wec:
        q = ['Tamil, Telugu','Bengali', 'Gujarati', 'Telugu, Tamil, Malayalam, Kannada, Hindi', 'English, Hindi',
             'Hindi, Tamil, Telugu, Kannada, Malayalam', 'English 7D', 'Punjabi', 'Marathi', 'Kannada, Telugu, Hindi',
             'English', 'Telugu', 'Hindi', 'Japanese', 'Tamil', 'Hindi, Telugu', 'Malayalam', 'Browse by Cinemas',
             'Kannada', 'Apply', 'Telugu, Hindi', 'Tamil, Telugu, Kannada', 'English, Hindi, Tamil, Telugu, Kannada',
             'English, Hindi, Tamil, Telugu', 'UA', 'U', 'A']
        if i not in q:
            abc.append(i)
            update.message.reply_text('%s' %i)
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(CommandHandler('help',help))
updater.dispatcher.add_handler(CommandHandler('ip_add',ip))
updater.dispatcher.add_handler(CommandHandler('name',stock))
updater.dispatcher.add_handler(CommandHandler('invite',chat_link))
updater.dispatcher.add_handler(CommandHandler('creator',creator))
updater.dispatcher.add_handler(CommandHandler('tel_movies',telugu_movies))
updater.dispatcher.add_handler(CommandHandler('india_trend',treding))
updater.dispatcher.add_handler(CommandHandler('movies_hyd',movies))
updater.dispatcher.add_handler(CommandHandler('movies_delhi',movies_delhi))
updater.dispatcher.add_handler(CommandHandler('movies_mumbai',movies_mumbai))
updater.dispatcher.add_handler(CommandHandler('movies_kochi',movies_kochi))
updater.dispatcher.add_handler(CommandHandler('movies_ahmedabad',movies_ahmedabad))
updater.dispatcher.add_handler(CommandHandler('movies_banglore',movies_bengaluru))
updater.dispatcher.add_handler(CommandHandler('movies_chandigarh',movies_chandigarh))
updater.dispatcher.add_handler(CommandHandler('movies_chennai',movies_chennai))
updater.dispatcher.add_handler(CommandHandler('movies_kolkata',movies_kolkata))
updater.dispatcher.add_handler(CommandHandler('movies_pune',movies_pune))
updater.dispatcher.add_handler(MessageHandler(Filters.command,text))
updater.dispatcher.add_handler(MessageHandler(Filters.text,google_custom))
updater.start_polling()

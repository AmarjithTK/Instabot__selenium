from random import uniform

from pageHandler import LoginPage,HomePage
from pageHandler import fetchDriver

from messagesender import MessageSender


MessageSender.send(message='mongi anamika')


instadriver = fetchDriver()


loginpage = LoginPage('username', 'password',driver=instadriver)
homepage = HomePage(driver=instadriver)

loginpage.clearLogin()

homepage.likeFeed(5)



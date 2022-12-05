# Walrus Family
#### Video Demo:  <https://youtu.be/nGLZIju3EXQ>
#### Description:

# **layout.html**
#### The layout in a format of templating , i've use django syntax too wright it.This is where that the navigation bar is all set up. On this page i had to make a video that show all the nft !
### - [This is an image](static/nft.00001.jpg) 
### - [This is an image](static/nft.00002.jpg)
### - [This is an image](static/nft.00003.jpg) 
## **layout.backgroud:**
#### mix them and end up with the short sequence in my page ,  all those drawing were made by a good friend of mine . I really hesitate for the background cause i didnt know if i wanting something brighter and or a bit darker the choice were :
### - [This is an image](static/bg.jpg)
### - [This is an image](static/bg2.jpg)
### - [This is an image](static/green.land.1.jpg)
#### I went toward something darker cause I felt like it was alot easier too mix with the rest of the content if we are talking visibility .


# **The navigation bar** 
## **My nav bar contain 8 iteams**
### - **My logo** [This is an image](/static/reallogo.png) I had to make few adjustment from the original.Because it wasn't fitting well in the corner and I made sure that we can't see that background and just the logo here the first logo [This is an image](/static/logo.png)! I have to make sure that my logo was reponsive has well !


### - **Reponsive NavBar** I had to but alot of time into my navigation bar to make it responsive. So when ever you look at my project from any type of screen all the desine fit very well !I had to put a dropdown menu so all the element could fit in the template desired. When ever you connect an account tought login the button "Register" and "Login" switch too "Log out"! I Had too put few css element call0 "@media" that adjust the nav bar content so when ever you have a different point of view everything fit well other wise when ever i arrive at the mini ipad size my template was mess up but finaly end up working!


## - **My home page:**
### Is where most of my programe is build, I made a button called "Connect Wallet" if pressed , you need too have metamask application too access it ! If you have metamask the button will promp you a form that ask you if you want too connect too the web page "WALRUS FAMILY" if you press continue the webpage look if you adresse if correct and how much monney you have in.I wright a smart contract so when ever you press the button pay with metamask you will be promp a smart contract and if you pay the fee you will be able too mint one of the nft once lauch !When ever you wright a smart contract every transaction is listed in the blockchain so when ever sold out we will go look in the blockchain too see who is eligible too mint the nft and and every adresses on the blockchain mint their own digital assest ! I had to find a picture for the pay with metamask and format it well [This is an image](static/4_pay_mm_off.png).I made a nice count down that will say when ever the project is launch it's written in javascript. I chose too make metamask has way to processe the transaction cause i really think metamask is the future of digital e-commerce and would love too work more with the web3 technologie.Also i had to make a small video, that show the digital assets i have use an application on my phone called "Videoleap" and it really help me to desine the video !

## - **Market.html :**
### This page content is where every digital asset will be dispose. i try my best to build some card for the picture that i had . My goal on that page was too display every digital assets that we have and eventualy be able too buy them on that page .I had to hide the icon-bar  because it was above every digital assets and it look alot more cleaner .I've input their price but when ever the collection is comming out i'll be able too input their real price and even sell them trought "OPEN SEA" and display the new owner or even display the rarity of their nft!

## - **Roadmap.html :**
### This page content is a list of the future plan of Walrus Family i chose this desine cause i really tought it fit well when ever we look at it on the phone version it was receptive , you can read the information easylie.I had to take of the icon bar here has well because it was hovering over everything and hiding elements .There is alot of css element just to make sure that everything is well size and just make sure that this page 

## - **About.html :**
### This page contain all the information of the developper, on this page i had to hide the icon bar cause it was hovering over the template of the creator and i rater keep that page clean and make sure we can read everything ! I put the back groud white too make it seem like it's like a business card.

## - **login.html :**
### My login file is pretty simple i just have made a forme where if your "Username" and "Password" match one row in the SQLITE database it will bring you at home page and if it doesn't match anything it will promp you an error.I made all that possible its my python file . I had alot of troble finding the "rowid" but once i found it i had every element too confirme that the account is the right one.Once login the user has acces too everything on the web-page. For the password we are looking is the hash code match well with the SQLITE password hash. I had too use the "Post" methods to compare the end result with the database.

## - **register.html :**
### My register form is still a form but with 5rows into it
### 1- its the email form
### 2- username form
### 3- password form
### 4- confirme password
### 5- checkbox form
### This page was made if you want too register you self too the page and be able too follow the project trought the checkbox form. The big part of my register was made in python.

## In python register section:

### When ever the user register i had to make sure that the username that the user input is not the same has an other one other wise we would end up with alot of mix up when ever log in . So when ever you register the password hash it self and goes into the database . We are looking the 2 password and password confirmation match then hash the password if it does! If the user check the box at the end of the form a email will be send too the email he wrote down.I made it that the user is obligated too fill every field too make sure that the database has the correct information . Here i had to work alot with the database information but finaly end up with something that work.I had to use the "Get" methods too get all the information from the file and compare it with the database.Email function vas pretty complicated because i didn't know that i had too generate a password in my setting of my email but end up getting it !

## - **Logout in app.py:**
###  Logout was made so when ever you login and register both of those link will be hidden and only shows logout instead. so if the user want too make an other account he can when ever he want. 

## - **helper.py:**
### In this page I have 3 function.
### 1- creat_connection
### 2- def appology
### 3- login_required
### **Creat_connection:** was made so when ever i need too connect my database too my python file I've used this function . Because at first, i had alot of trouble too get the right element from my database.
### **Def appology:** is well know from you guys ! This function was mad so when ever there is an error you will be promp too a page that tell you the error .
### **login_required:** was made so when ever you go on a certain page if you have that function attach too it will promp you a login forme.

# A  big thank you too the team of cs50 that build up that project! I've never learn that much anywhere else **YOU GUYS ARE AMAZAING  CS50 **

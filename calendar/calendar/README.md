

connectDB.py    which called in quickstart.py is used to insert accepted meeting invitation into database
quickstart.py   which called in main.py is used to do response(accept/decline) in organizer's calendar
main.py         run quickstart.py every 18 seconds
main.py can be ran directly.

dashijie.dat and suzhouhe.dat store the authentication information of these 
email accounts, 'dashijie.pwc@gmail' and 'suzhouhe.pwc@gmail.com', to access 
this application to operate their calendar. These two files are called in main.py
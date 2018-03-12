import quickstart
import schedule

class check:
    global value

    def job():
        # traverse all meeting room email account every 18 seconds
        # quickstart.main('suzhouhe.dat')
        # quickstart.main('dashijie.dat')
        quickstart.main('suzhouhe.dat')

        
    schedule.every(0.3).minutes.do(job)
    while True:
        schedule.run_pending()  
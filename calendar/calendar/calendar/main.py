import quickstart
import schedule

class check:
    global value

    def job():
        quickstart.main('PWCcredentials.dat')
        quickstart.main('credentialsPWC.dat')
        
    schedule.every(0.3).minutes.do(job)
    while True:
        schedule.run_pending()  
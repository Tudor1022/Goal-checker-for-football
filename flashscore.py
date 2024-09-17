from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
def flashscore_search(url):

    driver.get(url)

    time.sleep(5)
    board = driver.find_element(By.CSS_SELECTOR, 'div.duelParticipant')
    previous_events = set()

    while True:

        try:

            events = driver.find_elements(By.CSS_SELECTOR, 'div.smv__participantRow')  # Example class, inspect to confirm

            current_events = set([event.text for event in events])


            # Check for new events
            new_events = current_events - previous_events

            goal_events=[]

            for event in new_events:
                if '-' in event:
                    goal_events.append(event)
            print(f'Goal events: {goal_events}')
            if goal_events:
                for event in goal_events:
                    print(f"New event: {event}")

            # Update the list of seen events
            previous_events = current_events
        except Exception as e:
            print(f"Error: {e}")

       #Check if the match ended or if it is half-time
        if "final" in board.text.lower() :
            print('Final meci')
            break
        elif "pauză" in board.text.lower():
            print('Pauza meci')
            time.sleep(900)
            print('Incepe repriza 2')
        # Check for new events every 15 seconds
        time.sleep(15)

if __name__ == "__main__":
    #match link
    url='https://www.flashscore.ro/meci/CWZhADfl/#/sumar-meci/sumar-meci'
    flashscore_search(url)
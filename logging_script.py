import logging
import random
import time

logging.basicConfig(filename='log_file.log', level=logging.INFO, format='%(asctime)s - %(message)s')

greetings = ['Hello', 'Bonjour', 'Hola', 'Ciao', 'Namaste']

while True:
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    greeting = random.choice(greetings)
    log_message = f"{current_time} - {greeting}!"

    logging.info(log_message)
    time.sleep(5)

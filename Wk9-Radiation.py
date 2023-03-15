{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9978d54d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import RPi.GPIO as GPIO\n",
    "import time\n",
    "import datetime\n",
    "\n",
    "#GPIO pin set up\n",
    "GPIO.setmode(GPIO.BCM)\n",
    "GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)\n",
    "\n",
    "# global variable\n",
    "count = 0\n",
    "\n",
    "# callback function defn\n",
    "def count_pulse(channel):\n",
    "    global count\n",
    "    count += 1\n",
    "    print(time.time())\n",
    "\n",
    "# callback function\n",
    "GPIO.add_event_detect(6, GPIO.FALLING, callback=count_pulse)\n",
    "\n",
    "while True:\n",
    "    try:\n",
    "        count = 0\n",
    "        time.sleep(60)\n",
    "        print(\"Counts this minute:\", count)\n",
    "    except KeyboardInterrupt:\n",
    "        # Clean up GPIO \n",
    "        GPIO.cleanup()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

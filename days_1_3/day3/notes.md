Pomodoro timer ideas

Pomodoro class - use a class to hold info about the timer

The class will have the following attributes:

1. End time (25 minutes past start time)
2. Number of cycles

The class will also have the following methods:

1. start_main - Starts the timer, keeps track of time difference between current time and finish time. 
Adds a cycle when finish time is reached
2. reset_timer - Restarts the timer. Clears any cycles currently accrued.
3. start_break - Starts the break timer. Timer changes based on number of cycles accrued.
Calls "reset_timer" after long break completes


Example Flow

1. Define a task
2. Start the timer
3. Timer goes for 25 minutes
4. When 25 minutes are up, check number of cycles completed. 
If < 4:
    take short break. 
Else:
    take long break
5. When long break is complete, prompt user to define a new task, or quit timer

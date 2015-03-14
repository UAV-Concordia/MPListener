# MPListener
Mission Planer listener script

This script open an UDP socket from the Mission Planner that always reply by sending a predefined structure.
The server socket bind to port 49000.

### Structure
| 4 - altitude | 4 - latitude | 4 - longitude |

This is not defined yet, but a complete list of all the available data from the Mission Planner is [here](http://planner.ardupilot.com/wiki/common-other-mission-planner-features/common-using-python-scripts-in-mission-planner/).

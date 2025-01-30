# F1 Championship Simulation
#### Video Demo: https://youtu.be/ptoVmJv0jTY
#### Description:
This project consists of a web-based application that allows users to simulate the 2021 season of the Formula 1 World Championship,
by choosing the results of each race.

The applications generates the final ranking for both the Drivers Championship and the Constructors Championship according to the results selected by the user, allowing him to speculate about how the real championship might happen.
    
The 2021 Formula 1 season comprises a total of 23 races. 
However, the user can choose the number of races he wants to simulate, up to this maximum of 23.
    
In addition to the simulator, the application also contains information and statistics about all drivers and teams,
which can be seen by clicking on the driver or team name on the home page.
    
There is also the possibility for the user to save the final result he obtained by clicking on the "save results" button right after submitting his simulation.
Thus, the results can be accessed by the user at a later time.

In the simulation part, for each placement in the races that the user chose to simulate, he must select the initials of one of the drivers. 
If the user selects two positions for the same driver in the same race or does not complete the results for the top ten in all races,
an error explaining what the user did wrong will be generated when trying to submit the simulation.

When the user clicks on the "save results" button, two new SQL tables are created to store the result of the championships.
These tables have the user ID name followed by a character "c" (for the constructors championship) or "d" (for the drivers championship).
When the user clicks on "view results", these tables are accessed and the stored information is rendered in the template.
If the user saves a new simulation, the old SQL tables are deleted to make room for the new ones, so it is only possible to have one simulation saved at a time.

All tables used in this application were adapted from Bootstrap class "table table-striped".
This table class makes information easier to see and is aesthetically pleasing.

In the table where the user chooses the race results, the rows of the first, second, and third places
are represented respectively by the colors, gold, silver, and bronze, as these colors symbolize the trophies of the first three places in Formula 1.

Files used in this application were: two python files and some SQL tables made for using Flask,
a CSS file used to define the styles and many HTML files.
30 of them are the templates for the pages of the twenty drivers and the ten teams.
The others are the templates for the homepage, simulation, results, saved results, among others that were necessary for the application to work.

This is F1 Championship Simulation.

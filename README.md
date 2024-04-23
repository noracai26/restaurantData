# Restaurant data interface


## To build, compile, and run
This project uses the Requests and the PrettyTable python library, please run 
the following command to install the libraries:

`pip install requests`

`pip install prettytable`

The project can be run by cloning this project, navigating to the root 
directory, and running the command:

`python main.py`

Please expand the terminal to a size large enough for display, so that the 
table does not get distorted.

The project is built using python version 3.9.12

## Assumptions made

### The assumed use case (also partially derived from the API)
When a user submits the postcode of their current location, the application returns 
a list of restaurants that are of deliverable distance from the user, 
showing relevant information about name, ratings, cuisines, and address for each restaurant.
For better readability, the data will be displayed as a table, with each row displaying 
a restaurant, and each column displaying name, ratings, cuisines, and address respectively.

### Information abstraction
It would then be assumed that the target user 
of the application would be the takeout customers of JET, 
it is thus very important to make the output readable for humans
and abstract away any redundant or unnecessary information. 
As such, the relevant attribute "name", "rating", "cuisines" and "address" 
from the "restaurants" object is being abstracted and represented as follows:
* name: nothing to abstract, just display name as it is
* ratings: 
  * The attribute "userRating" is not included, since it is always null.
  * It is assumed that "count" represents the amount of user ratings received, 
  ratings is thus displayed as _startRating_(_count_ reviews).
  * The ratings are also color coded for better readability, 
  with green meaning >=4.0, orange meaning >=3.5, and red otherwise
* cuisines: 
  * only the "name" attribute is printed and not the "uniqueName" attribute, 
  since they store the same information and only differ in syntax, 
  we only need the syntax that is more readable for humans.
  * It is also assumed that the "cuisines" attribute refers more generally to the types
  of meals offered and not just the country of origin, as such, 
  information like "Deals" and "Low Delivery Fee" is also included.
* address: The “location” attribute is not included, 
since coordinates are not a very useful for the use case.

## Improvements to be made
* To better serve the use case, the program could be adjusted to have a customizable postcode input,
so that the user could inform the program about their current location, 
rather than the program always having a fixed postcode.
* Some filters can be applied to the restaurants displayed to better serve the user.
Before displaying the restaurants, the program could ask for the user's preference 
and only display relevant data, for example:
  * ask if the user wants the food to be picked up or delivered, 
  and only display restaurants that "isOpenNowForCollection" or "isOpenNowForDelivery" respectively.
  * ask if the user is hungry, and if so, only display restaurants with low "etaMinutes"
  * ask what cuisines the user wants to eat, and only display the relevant cuisines.
  The user is also able to input "I don't know".
* The user could also request for more recommendations if the user 
is not satisfied with the current ten restaurants being displayed.
* Adjust the program so that the width of the table adapts to the size of the terminal.


_End of README, thank you for your time_ :D

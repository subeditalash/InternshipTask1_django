Here i have created database using modle.py. Poll model store the poll qnestion with and other attribuite. and next we have created option class which store the option of poll so we make a relation using foreign key. And for select or to store the vote we have other class Select with its attribute user, option and selecting time. We do not required to add the primary key cause it is define by itself in django. 
Then i register the Poll, option, and select models with the Django Admin interface. Here we make our Option box and ask the admin to make  poll and adim is also allowed to voted.
Then we create the views to display polls and handle selecting and request the backend for data so that we can render it to frontend or html. 
I have also make simple html file to display.
then we manage all the routing using urls.py

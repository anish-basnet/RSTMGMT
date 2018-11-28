#Total is 4 elements
#the image file location should be start from the static folder

main_info="YumKitchen is the web application that will manage the all the transaction of the" \
          " restaurant. It will transform the traditional restaurant management system into digital" \
          " management system. This application will be only used by the admin or the accountant of the restaurant.";
#Content 1
content_heading_1="Menu";   #heading should match with the static html page
content_info_1="It contains all the food item that will be available in Restaurant. It will help accountant or admin to choose " \
               "the menu for particular customer.";

#Content 2
content_heading_2="Services";
content_info_2="It contains all the services that will be provided by the restaurant. It will help accountant to give the remainder" \
               " of the services that will be provided by the restaurant.";

#Content 3
content_heading_3="Reservation";
content_info_3="It contains early online table reservation information of the restaurant. It will help the accountant to booked the table" \
               " on special day of the people.";

#Content 4
content_heading_4="Payment";
content_info_4="It contains all the payment method provided by the restaurant. The accountant can take the cash or anything that accountant" \
               " desire.";

def as_list_index():
    return [content_heading_1,content_info_1,content_heading_2,content_info_2,content_heading_3
            ,content_info_3,content_heading_4,content_info_4];
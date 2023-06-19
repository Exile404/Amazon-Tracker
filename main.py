from Backend.backend import Amazon_Tracker

with Amazon_Tracker() as Bot:
    Bot.land_first_page()
    Bot.search_and_select('Iphone')

# What does this app do
when the moment of Christmas come, for a family where people are far away from each other, making a wishlist can be daunting. In my family, we use google sheets to share our wishlists across continents but it makes it hard to synchronize for the gift buying and might end up buying the same present as your cousin for your grandmother:/. This is a draft of an app that would solve this problem.

You can try this app here: http://my-christmas-app.herokuapp.com/

# Screenshot
![Screenshot](screenshot.png)

# How to run it? 
1. Create the databases: `ipython app/init_tables.py`
2. Run flask with `flask run` 
3. Access the website on `localhost:5000`  

# TODO 
- There are code duplicates in `routes.md` > to be fixed
- ~~Add a docker file to deploy the app easily in a cloud~~ 
- The offer list doesn't refresh properly, should fix it with some javascript. 

# Thanks
A big thanks to the [Flask mega tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) 
which was a great inspiration for this project.


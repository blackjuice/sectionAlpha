# Ruby on Rails

Installing packages:

`bundle install --without production`

Setting up the database locally and add data:

`bundle exec rake db:migrate`

`bundle exec rake db:seed`

Running (personal IP: 177.153.13.70):

`rails server --binding=<IP>`


### Getting started

Here’s how to get rolling:

* Use rails generate to create your models and controllers

	* To see all available options, run it without parameters.
    
* Set up a default route and remove public/index.html

	* Routes are set up in config/routes.rb.
    
* Create your database

	* Run rake db:create to create your database. If you're not using SQLite (the default), edit config/database.yml with your username and password.

# Heroku

`ssh-keygen -t rsa`

`heroku login`

`heroku keys:add`

Once you have your heroku keys set up correctly you can create a heroku instance from the rottenpotatoes directory

`heroku create`

Now we can use git to deploy our code to the Heroku server in the cloud

`git push heroku master`

Next we need to tell the cloud instance to prepare the database:

`heroku run rake db:migrate`

We need to tell the cloud instance to add some data to the database:

`heroku run rake db:seed`

Now you can navigate to the heroku url that heroku create printed to the console and see your app running in the cloud.

`heroku open`

## Solving "Heroku push rejected, no Cedar-supported app detected"

	rm -rf .git
	git init
	git add .
	git commit -am "Reinitialize"
	heroku create --stack cedar
	git push heroku master

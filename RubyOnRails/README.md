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



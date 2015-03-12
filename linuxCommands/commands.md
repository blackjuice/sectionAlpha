## wget directories

-r : recursive

-nd : prevents creating folders

--reject "foo" : prevents downloading index.html

`wget -r --no-parent -nd --reject "index.html*" "http://link.com"`

Or on Windows:

flask\Scripts\python
Once in the Python prompt enter the following:

>>> from app import db, models
>>>
This brings our database and models into memory.

Let's create a new user:

>>> u = models.User(nickname='john', email='john@email.com')
>>> db.session.add(u)
>>> db.session.commit()
>>>
Changes to a database are done in the context of a session. Multiple changes can be accumulated in a session and once all the changes have been registered you can issue a single db.session.commit(), which writes the changes atomically. If at any time while working on a session there is an error, a call to db.session.rollback() will revert the database to its state before the session was started. If neither commit nor rollback are issued then the system by default will roll back the session. Sessions guarantee that the database will never be left in an inconsistent state.

Let's add another user:

>>> u = models.User(nickname='susan', email='susan@email.com')
>>> db.session.add(u)
>>> db.session.commit()
>>>
Now we can query what our users are:

>>> users = models.User.query.all()
>>> users
[<User u'john'>, <User u'susan'>]
>>> for u in users:
...     print(u.id,u.nickname)
...
1 john
2 susan
>>>
For this we have used the query member, which is available in all model classes. Note how the id member was automatically set for us.

Here is another way to do queries. If we know the id of a user we can find the data for that user as follows:

>>> u = models.User.query.get(1)
>>> u
<User u'john'>
>>>
Now let's add a blog post:

>>> import datetime
>>> u = models.User.query.get(1)
>>> p = models.Post(body='my first post!', timestamp=datetime.datetime.utcnow(), author=u)
>>> db.session.add(p)
>>> db.session.commit()
Here we set our timestamp in UTC time zone. All timestamps stored in our database will be in UTC. We can have users from all over the world writing posts and we need to use uniform time units. In a future tutorial we will see how to show these times to users in their local timezone.

You may have noticed that we have not set the user_id field of the Post class. Instead, we are storing a User object inside the author field. The author field is a virtual field that was added by Flask-SQLAlchemy to help with relationships, we have defined the name of this field in the backref argument to db.relationship in our model. With this information the ORM layer will know how to complete the user_id for us.

To complete this session, let's look at a few more database queries that we can do:

# get all posts from a user
>>> u = models.User.query.get(1)
>>> u
<User u'john'>
>>> posts = u.posts.all()
>>> posts
[<Post u'my first post!'>]

# obtain author of each post
>>> for p in posts:
...     print(p.id,p.author.nickname,p.body)
...
1 john my first post!

# a user that has no posts
>>> u = models.User.query.get(2)
>>> u
<User u'susan'>
>>> u.posts.all()
[]

# get all users in reverse alphabetical order
>>> models.User.query.order_by('nickname desc').all()
[<User u'susan'>, <User u'john'>]
>>>
The Flask-SQLAlchemy documentation is the best place to learn about the many options that are available to query the database.

Before we close, let's erase the test users and posts we have created, so that we can start from a clean database in the next chapter:

>>> users = models.User.query.all()
>>> for u in users:
...     db.session.delete(u)
...
>>> posts = models.Post.query.all()
>>> for p in posts:
...     db.session.delete(p)
...
>>> db.session.commit()
>>>
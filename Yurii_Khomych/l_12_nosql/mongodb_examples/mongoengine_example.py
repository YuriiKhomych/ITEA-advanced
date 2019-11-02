from mongoengine import *

connect('mydb', 'default', host='localhost')
from mongodb_examples.mongoengine_models import Post


post_1 = Post(
    title='Sample Post',
    content='Some engaging content',
    author='Scott'
)
post_1.save()       # This will perform an insert
print(post_1.title)
post_1.title = 'A Better Post Title'
post_1.save()       # This will perform an atomic edit on "title"
print(post_1.title)
post_2 = Post(content='Content goes here', author='Michael')
post_2.save()
# Post.objects

# Post.objects.first().author.name

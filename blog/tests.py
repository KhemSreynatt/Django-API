from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category


class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')

        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')
        testuser1.save()

        test_post = Post.objects.create(
            category_id=1, titel='Post Title', excerpt='Post Excerpt', content='Post Content', slug='post-title', author_id=1, status='published')
        test_post.save()

    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        # titel = f'{post.titel}'
        content = f'{post.content}'
        status = f'{post.status}'
        excerpt = f'{post.excerpt}'
        self.assertEqual(author, 'test_user1')
        self.assertEqual(excerpt,'Post Excerpt')
        # self.assertEqual(titel, 'Post Title')
        self.assertEqual(content, 'Post Content')
        self.assertEqual(status, 'published')
        # self.assertEqual(str(post), "Post Title")
        self.assertEqual(str(cat), "django")
# Techie Nerd Squad  Website
**Coming Soon**
**Blog Post Model with Multiple Features**

This is a Django model representing a blog post, equipped with several features to enhance the blogging experience. Below is a detailed outline of the features provided by this model:

1. **Comment Model**
   - Represents a comment made on a blog post.
   - Fields:
     - `post`: ForeignKey linking the comment to the respective post.
     - `author`: ForeignKey linking the comment to the user who made it.
     - `content`: TextField to store the comment's content.
     - `date_posted`: DateTimeField recording the date and time the comment was posted.
   - `__str__` method returns a string representation of the comment.

2. **Post Model**
   - Represents a blog post.
   - Fields:
     - `title`: CharField storing the title of the blog post.
     - `table_of_contents`: TextField to include a table of contents for the blog post.
     - `content`: TextField containing the main content of the blog post.
     - `date_posted`: DateTimeField capturing the date and time of the blog post's creation.
     - `authors`: ManyToManyField establishing a many-to-many relationship with the `Author` model to allow multiple authors for a single post.
     - `slug`: SlugField providing a unique URL-friendly identifier for the blog post.
     - `image`: ImageField for uploading and associating an image with the blog post (optional).
     - `tags`: TaggableManager allowing tags to be added to the blog post.
     - `status`: CharField with choices to specify the status of the blog post (e.g., draft, published).
     - `meta_description`: TextField for adding meta description for SEO (optional).
     - `meta_keywords`: TextField for adding meta keywords for SEO (optional).
     - `comments_enabled`: BooleanField to enable or disable comments on the blog post.
     - `likes_enabled`: BooleanField to enable or disable likes on the blog post.
   - `__str__` method returns a string representation of the blog post, including its title and authors.

3. **PostStatusHistory Model**
   - Records the status history of a blog post.
   - Fields:
     - `post`: ForeignKey linking the status history to the respective blog post.
     - `status`: CharField storing the status of the blog post (e.g., draft, published).
     - `date_updated`: DateTimeField recording the date and time of the status update.
   - `__str__` method returns a string representation of the status history entry.

4. **PostExcerpt Model**
   - Stores an excerpt or summary of the blog post.
   - Fields:
     - `post`: OneToOneField linking the excerpt to the respective blog post.
     - `excerpt`: TextField containing the summary of the blog post.
   - `__str__` method returns a string representation of the excerpt.

5. **RelatedPost Model**
   - Establishes a relationship between related blog posts.
   - Fields:
     - `post`: ForeignKey linking the related post to the respective blog post.
     - `related_post`: ForeignKey linking the related post to another blog post.
   - `__str__` method returns a string representation of the relationship.

6. **Like Model**
   - Represents a like action by a user on a blog post.
   - Fields:
     - `post`: ForeignKey linking the like to the respective blog post.
     - `user`: ForeignKey linking the like to the user who made it.
   - `__str__` method returns a string representation of the like.

7. **ReadTime Model**
   - Calculates and stores the estimated reading time for a blog post.
   - Fields:
     - `post`: OneToOneField linking the reading time to the respective blog post.
     - `minutes`: PositiveIntegerField indicating the estimated reading time in minutes.
   - `__str__` method returns a string representation of the reading time.

8. **SocialMediaSharing Model**
   - Provides fields for storing Twitter, Facebook, and LinkedIn sharing URLs for each post.
   - Fields:
     - `post`: OneToOneField linking the social media sharing to the respective blog post.
     - `twitter_url`: URLField for adding the Twitter sharing URL (optional).
     - `facebook_url`: URLField for adding the Facebook sharing URL (optional).
     - `linkedin_url`: URLField for adding the LinkedIn sharing URL (optional).
   - `__str__` method returns a string representation of the social media sharing.

The provided model offers extensive functionality for creating and managing blog posts with multiple authors, comments, likes, tags, and social media sharing options. The addition of features like status history, post excerpt, related posts, and estimated reading time further enhances the blogging experience for both authors and readers.
class Configure:
    def __init__(self):
        self.secret_key = 'some_secret'
        self.ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']
        self.ADMIN_USER = 'Maor'
        self.ADMIN_PASSWORD = 'GOAZ&7'
        self.BANNED_USERS = []
        self.BLOG_URL = 'localhost'
        self.DB_URL = 'localhost'
        self.POST_LINK = '{0}/posts'.format(self.BLOG_URL)
        self.database_connection_string = 'postgresql://postgres:postgres@localhost/postgres'


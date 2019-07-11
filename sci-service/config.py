config = {
    "sci-service_dir": "/var/www/sci-service/",
    "repo": "https://github.com/{YOUR_TARGET_REPO_GOES_HERE}.git",
    "branches": {
        "develop": "/var/www/develop",
        "staging": "/var/www/staging",
        "test":    "/var/www/test",
        "master": "/var/www/html"
    },
    "JSON_AS_ASCII": False,
    "secret_key": "{SECRET_KEY}",
    "apache_user": "www-data"
}
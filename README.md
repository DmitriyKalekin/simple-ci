# simple-ci  (sci)
Simple continuous integration service



## Installation
SimpleCI needs to be installed when all your environments are located on the same server.

1. Locate files from `/sci-service` into `/var/www/sci-service`  
2. Run `chown -R www-data: /var/www/sci-service`  
3. Run `pip3 install -r requirements.txt`  
4. Create A-records for subdomain `sci` and all subdomains like `develop`, `staging`, `test` pointing to IP address of your server.  
5. Configure `sci.conf`, `develop.conf`, `staging.conf`, `test.conf` in your apache virtual hosts dir `/etc/apache2/sites-available` as shown in examples from `/apache_vhosts_conf`  
6. Run `a2ensite sci` for CI-service subdomain and commands like `a2ensite develop` to enable subdomains for your environments.  
7. Run commands like `certbot --apache -d develop.your-domain.com` to obtain HTTS certificate for all your environments.  
8. Configure `/var/www/sci-service/config.py`, change location of your repo.  
9. Loging in your github.com account and set up push webhook to your SimpleCI service like: `https://sci.your-domain.com/push`   
10. Enjoy!


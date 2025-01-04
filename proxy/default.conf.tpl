server {
   listen ${LISTEN_PORT};
   server_name ec2-52-207-221-173.compute-1.amazonaws.com;

   location /static {
     alias /vol/web/static;
     add_header Cross-Origin-Opener-Policy same-origin;
   }

    location / {
     uwsgi_pass           ${APP_HOST}:${APP_PORT};
     include              /etc/nginx/uwsgi_params;
     client_max_body_size 10M;
   }
}
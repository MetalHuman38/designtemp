server {
   listen ${LISTEN_PORT};
   server_name metalbrain.net www.metalbrain.net;

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
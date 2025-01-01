server {
    listen ${LISTEN_PORT};
    server_name metalbrain.net www.metalbrain.net;

    # Redirect all HTTP traffic to HTTPS
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name metalbrain.net www.metalbrain.net;

    # Proxy SSL traffic to GoDaddy
    location / {
        proxy_pass https://metalbrain.net;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

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

FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
CMD sed -i -e 's|BACKEND_API_URL_YERI|'"$BACKEND_URL"'|g' /usr/share/nginx/html/index.html && \
    sed -i -e 's/80/'"$PORT"'/g' /etc/nginx/conf.d/default.conf && \
    nginx -g 'daemon off;'
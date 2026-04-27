# Use a lightweight web server
FROM nginx:alpine

# Copy your HTML, CSS, and JS into the web server's folder
COPY . /usr/share/nginx/html

# Expose port 80 (standard for web traffic)
EXPOSE 80

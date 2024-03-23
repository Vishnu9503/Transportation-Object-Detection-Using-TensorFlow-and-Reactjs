# Use an official Node.js image as the base image
FROM node:14-alpine as build

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the remaining app files to the working directory
COPY . .

# Build the React app
RUN npm run build

# Use Nginx as the web server
FROM nginx:alpine

# Copy the build output from the build stage to the Nginx web server directory
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80 to the outside world
EXPOSE 80

# Command to run the Nginx server
CMD ["nginx", "-g", "daemon off;"]

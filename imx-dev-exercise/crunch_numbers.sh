#! /bin/bash
echo "Hello, World!!"

# Your script here
sudo docker build --tag number-cruncher .


# Finally, run the application
# i.e. docker run ...
sudo docker run --publish 5000:5000 number-cruncher

IMAGE="scraping"
CONTAINER="scraping_test"

# Build docker image
docker build -t $IMAGE .

# Run the tests inside a container
docker run --name $CONTAINER --rm \
	-v "$(pwd)"/db_access:/db_access \
	$IMAGE python3 /db_access/test.py

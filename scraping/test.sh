IMAGE="scraping"
CONTAINER="scraping_test"
RESOURCE_DIR="../resources"

# Build docker image
docker build -t $IMAGE .

# Run the tests inside a container
docker run --name $CONTAINER --rm \
	-v "$(pwd)"/db_access:/db_access \
	-v "$(pwd)"/${RESOURCE_DIR}:/resources \
	$IMAGE python3 /db_access/test.py

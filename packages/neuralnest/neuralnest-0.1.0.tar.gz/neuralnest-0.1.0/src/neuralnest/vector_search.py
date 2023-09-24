from pymilvus import CollectionSchema, DataType, FieldSchema, MetricType, Milvus
from neuralnest.load_models import vector_dimension

# Constants
MILVUS_HOST = "localhost"
COLLECTION_NAME = "file_vectors"
MILVUS_PORT = 19530
VECTOR_DIMENSION = vector_dimension

# Connect to Milvus server
client = Milvus(host=MILVUS_HOST, port=MILVUS_PORT)

# Create a collection in Milvus to store the vectors
if not client.has_collection(COLLECTION_NAME):
    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=VECTOR_DIMENSION),
    ]
    schema = CollectionSchema(fields=fields, description="Collection of file vectors")
    client.create_collection(COLLECTION_NAME, schema=schema)


# Insert vectors into the collection
def insert_vectors(vectorized_files):
    vectors = [file.vectorized_content for file in vectorized_files]
    client.insert(COLLECTION_NAME, records=vectors)


# Search for similar vectors in the collection
def search_vector(vector, top_k=5):
    search_params = {"metric_type": MetricType.L2, "params": {"nprobe": 10}}
    results = client.search(COLLECTION_NAME, [vector], top_k, params=search_params)
    return results


# Example usage:
# vectorized_file = vectorize_file('path_to_file.txt')
# insert_vectors([vectorized_file])
# similar_files = search_vector(vectorized_file.vectorized_content)

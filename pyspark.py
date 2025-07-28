# just exmple

from pyspark.sql.functions import udf
from pyspark.sql.types import ArrayType, StringType

# Create a broadcast-safe version of the function
def make_tokenize_udf(trie):
    def tokenize_wrapper(text):
        if text is None:
            return []
        return tokenize(text, trie)
    return udf(tokenize_wrapper, ArrayType(StringType()))
    
# Build Trie once
trie = build_trie_from_file("thai_words.txt")

# Register UDF
tokenize_udf = make_tokenize_udf(trie)

# Apply to DataFrame
df = df.withColumn("tokens", tokenize_udf("text"))
df.show(truncate=False)
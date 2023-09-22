def fileIngest(folder_path, custom_schema):
    return spark.read.option("multiline", "true").json(folder_path + "*.json", schema=custom_schema)
    
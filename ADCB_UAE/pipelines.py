import json

class JsonWriterPipeline:
    def __init__(self):
        self.file = open('scraped_data.json', 'w')  # Open file to write JSON data
        self.first_item = True  # Flag to handle commas in JSON

    def process_item(self, item, spider):
        # Write the first item without a leading comma
        if self.first_item:
            self.file.write('[')
            self.first_item = False
        else:
            self.file.write(',')

        # Convert item to JSON and write to the file
        self.file.write(json.dumps(dict(item)))

        return item

    def close_spider(self, spider):
        self.file.write(']')  # Close the JSON array
        self.file.close()

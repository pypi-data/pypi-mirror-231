import subprocess
import boto3
import openai


class BaseDocument(object):
    def __init__(self, name, uri, bucket):
        self.name = name
        self.bucket = bucket
        self.uri = uri
        self.source_path = "" 
        self.datadir = ""
 
    def download(self):
        """ Downloads the source document """
        return

    def split(self):
        """ Splits source file into smaller chunks for processing """
        return

    def process(self):
        """ Processes the document(s) to extract text """
        return

    def open(self):
        """ Opens the source file """
        commands = ['open', self.source_path]
        subprocess.call(commands)

    def sync(self):
        """ Syncs the datadir to the s3 bucket using the AWS cli as a hack """
        # TODO: move to Base Document class
        s3 = boto3.client('s3')
        local_folder = f'./{self.datadir}'
        target_bucket = f's3://{self.bucket}/{self.datadir}'
        commands = ['aws', 's3', 'sync', local_folder, target_bucket]
        subprocess.call(commands)

    def query(self):
        """ Query the document """
        raise NotImplementedError

    def extract_data(self, DataClass, text, model="gpt-3.5-turbo-16k", temperature=0.2, max_tokens=2000):
        completion = openai.ChatCompletion.create(
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            functions=[DataClass.openai_schema],
            function_call={"name": DataClass.openai_schema["name"]},
            messages=[
                {
                    "role": "system",
                    "content": f"You are a world class algorithm to extract data from documents",
                },
                {"role": "user", "content": f"Extract the data using the following text"},
                {"role": "user", "content": f"Text: {text}"}
            ],
        )
        return DataClass.from_response(completion)

    def cleanup(self):
        """ Removes local files """
        raise NotImplementedError
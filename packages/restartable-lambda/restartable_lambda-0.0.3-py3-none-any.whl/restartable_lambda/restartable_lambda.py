import os
import json
import uuid
from retrying import retry
import boto3

class RestartableLambda(object):
  REMAINING_TIME_TO_RESTART = int(os.environ.get('REMAINING_TIME_TO_RESTART', 300000)) # 5 minutes in ms
  MAX_NUMBER_OF_EXECUTION = int(os.environ.get('MAX_NUMBER_OF_EXECUTION', 3)) # this will give the request MAX_NUMBER_OF_EXECUTION * 15 minutes to finish

  def __init__(self, event, context, files_name_list, s3_bucket, s3_base_path):
    self.event = event
    self.context = context
    self.s3_bucket = s3_bucket
    self.s3_base_path = s3_base_path
    self.s3 = boto3.resource('s3')
    self.must_restart = False

    self.event['restart_count'] = self.event.get('restart_count', 0)
    self.event['saved_files'] = self.event.get('saved_files', {name:None for name in files_name_list})

    self.files = {}
    for name, path in self.event['saved_files'].items():
      self.files[name] = self.retrieve_file(name, path)

  def restart_if_needed(self, new_values={}):
    if self.should_restart(): self.save_before_restart(new_values)

  def restart_lambda_function(self):
    client = boto3.client('lambda', region_name='eu-west-1')

    self.event['restart_count'] += 1

    client.invoke(
      FunctionName='{}:{}'.format(self.context.function_name, self.context.function_version),
      InvocationType='Event',
      Payload=json.dumps(self.event)
    )

    print('Restarted...')

    self.must_restart = True
    raise Exception("Restarted...")

  def should_restart(self):
    can_restart = self.event['restart_count'] + 1 < self.MAX_NUMBER_OF_EXECUTION

    if not can_restart:
      raise Exception('Too many restart!')

    return self.context.get_remaining_time_in_millis() < self.REMAINING_TIME_TO_RESTART and can_restart

  def save_before_restart(self, new_values={}):
    for name, value in self.files.items():
      self.upload_temp_file(new_values.get(name, value), self.event['saved_files'][name])
    self.restart_lambda_function()

  @retry(wait_fixed=5000, stop_max_attempt_number=3)
  def upload_temp_file(self, json_to_upload, s3_path):
    local_path = '/tmp/{}.json'.format(str(uuid.uuid4()))
    with open(local_path, 'w+') as file:
      json.dump(json_to_upload, file)

    boto_object = self.s3.Object(self.s3_bucket, s3_path)
    boto_object.upload_file(local_path, { 'ACL': 'public-read' })

  def retrieve_file(self, name, path):
    if path:
      try:
        boto_object = self.s3.Object(self.s3_bucket, path)
        local_path = '/tmp/{}.json'.format(name)
        boto_object.download_file(local_path)

        with open(local_path, 'r') as file_json:
          return json.load(file_json) or {}
      except Exception as e:
        print(e)
        return {}
    else:
      self.event['saved_files'][name] = '{}/{}_{}.json'.format(self.s3_base_path, name, str(uuid.uuid4()))
      return {}
import os
import json
import unittest

from gobits import Gobits
from unittest.mock import Mock, patch  # noqa: F401
from werkzeug.local import LocalProxy  # noqa: F401

X_GOOGLE_GCP_PROJECT = 'my-test-project'
X_GOOGLE_FUNCTION_NAME = 'my-test-function'
SUBSCRIPTION = 'my-test-subscription'
FUNCTION_TRIGGER_TYPE = 'http'
X_GOOGLE_FUNCTION_VERSION = '99'
HTTP_FUNCTION_EXECUTION_ID = '0123456789'
EXECUTION_TYPE = 'cloud_function'
EVENT_ID = '1234567890123456'
MESSAGE_ID = '1234567890123456'
MESSAGE_PUBLISH_TIME = '2020-12-31T23:59:59.999Z'
BUILDER_OUTPUT = '/builder/outputs'


class TestGobits(unittest.TestCase):

    def setUp(self):
        os.environ['X_GOOGLE_GCP_PROJECT'] = X_GOOGLE_GCP_PROJECT
        os.environ['X_GOOGLE_FUNCTION_NAME'] = X_GOOGLE_FUNCTION_NAME
        os.environ['FUNCTION_TRIGGER_TYPE'] = FUNCTION_TRIGGER_TYPE
        os.environ['X_GOOGLE_FUNCTION_VERSION'] = X_GOOGLE_FUNCTION_VERSION
        self.gobits = Gobits()

    def test_processed(self):
        self.assertEqual(len(self.gobits.processed), 24),

    def test_gcp_project(self):
        self.assertEqual(self.gobits.gcp_project, X_GOOGLE_GCP_PROJECT)

    def test_execution_type(self):
        self.assertEqual(self.gobits.execution_type, EXECUTION_TYPE)

    def test_execution_trigger_type(self):
        self.assertEqual(self.gobits.execution_trigger_type, FUNCTION_TRIGGER_TYPE)

    def test_function_name(self):
        self.assertEqual(self.gobits.function_name, X_GOOGLE_FUNCTION_NAME)

    def test_function_version(self):
        self.assertEqual(self.gobits.function_version, X_GOOGLE_FUNCTION_VERSION)

    def test_to_json(self):
        gobits = self.gobits.to_json()
        self.assertEqual(gobits['gcp_project'], X_GOOGLE_GCP_PROJECT)
        self.assertEqual(gobits['execution_type'], EXECUTION_TYPE)
        self.assertEqual(gobits['execution_trigger_type'], FUNCTION_TRIGGER_TYPE)
        self.assertEqual(gobits['function_name'], X_GOOGLE_FUNCTION_NAME)
        self.assertEqual(gobits['function_version'], X_GOOGLE_FUNCTION_VERSION)

    def test_json_length(self):
        gobits = self.gobits.to_json()
        self.assertEqual(len(gobits), 6)

    def tearDown(self):
        os.environ['X_GOOGLE_GCP_PROJECT'] = ''
        os.environ['X_GOOGLE_FUNCTION_NAME'] = ''
        os.environ['FUNCTION_TRIGGER_TYPE'] = ''
        os.environ['X_GOOGLE_FUNCTION_VERSION'] = ''


class TestEmptyRequestGobits(unittest.TestCase):

    @patch('werkzeug.local.LocalProxy')
    def setUp(self, mock_request):
        mock_request.data = b''
        mock_request.headers = {'Function-Execution-Id': HTTP_FUNCTION_EXECUTION_ID}
        self.gobits = Gobits.from_request(request=mock_request)

    def test_to_json(self):
        gobits = self.gobits.to_json()
        self.assertEqual(gobits['execution_id'], HTTP_FUNCTION_EXECUTION_ID)


class TestRequestGobits(unittest.TestCase):

    @patch('werkzeug.local.LocalProxy')
    def setUp(self, mock_request):
        mock_envelope = dict(
            subscription=SUBSCRIPTION,
            message=dict(
                messageId=MESSAGE_ID,
                publishTime=MESSAGE_PUBLISH_TIME
            )
        )
        mock_request.data = json.dumps(mock_envelope).encode('utf-8')
        mock_request.headers = {'Function-Execution-Id': HTTP_FUNCTION_EXECUTION_ID}
        self.gobits = Gobits.from_request(request=mock_request)

    def test_processed(self):
        self.assertEqual(len(self.gobits.processed), 24),

    def test_execution_id(self):
        self.assertEqual(self.gobits.execution_id, HTTP_FUNCTION_EXECUTION_ID)

    def test_message_id(self):
        self.assertEqual(self.gobits.message_id, MESSAGE_ID)

    def test_message_publish_time(self):
        self.assertEqual(self.gobits.message_publish_time, MESSAGE_PUBLISH_TIME)

    def test_to_json(self):
        gobits = self.gobits.to_json()
        self.assertEqual(gobits['execution_id'], HTTP_FUNCTION_EXECUTION_ID)
        self.assertEqual(gobits['message_id'], MESSAGE_ID)
        self.assertEqual(gobits['message_publish_time'], MESSAGE_PUBLISH_TIME)

    def test_json_length(self):
        gobits = self.gobits.to_json()
        self.assertEqual(len(gobits), 5)


class TestContextGobits(unittest.TestCase):

    @patch('unittest.mock.Mock')
    def setUp(self, mock_context):
        mock_context.event_id = EVENT_ID
        self.gobits = Gobits.from_context(context=mock_context)

    def test_processed(self):
        self.assertEqual(len(self.gobits.processed), 24),

    def test_event_id(self):
        self.assertEqual(self.gobits.event_id, EVENT_ID)

    def test_to_json(self):
        gobits = self.gobits.to_json()
        self.assertEqual(gobits['event_id'], EVENT_ID)

    def test_json_length(self):
        gobits = self.gobits.to_json()
        self.assertEqual(len(gobits), 2)


class TestCloudBuildGobits(unittest.TestCase):

    def setUp(self):
        os.environ['BUILDER_OUTPUT'] = BUILDER_OUTPUT
        self.gobits = Gobits()

    def test_processed(self):
        self.assertEqual(len(self.gobits.processed), 24),

    def test_to_json(self):
        gobits = self.gobits.to_json()
        self.assertEqual(gobits['execution_type'], 'cloud_build')

    def test_json_length(self):
        gobits = self.gobits.to_json()
        self.assertEqual(len(gobits), 2)

    def tearDown(self):
        os.environ['BUILDER_OUTPUT'] = ''


if __name__ == '__main__':
    unittest.main()

import unittest
from datetime import datetime

from concurrent import futures
from rox.server.client.sdk_settings import SdkSettings
from rox.server.rox_options import RoxOptions

from rox.core.client.internal_flags import InternalFlags
from rox.core.network.configuration_fetcher import ConfigurationFetcher
from rox.core.network.state_sender import StateSender
from rox.core.reporting.error_reporter import ErrorReporter
from rox.core.configuration.configuration_parser import ConfigurationParser
from rox.core.entities.flag_setter import FlagSetter
from rox.core.network.configuration_fetcher_roxy import ConfigurationFetcherRoxy

from rox.core.core import Core

try:
    from unittest.mock import Mock, patch
except ImportError:
    from mock import Mock, patch


class CoreTests(unittest.TestCase):
    def setUp(self):
        self.internal_is_enabled_result = False
        self.internal_get_number_result = 0

        self.internal_flags_mock = Mock(InternalFlags)

        def internal_flag_is_enabled_mock(flag_name):
            if flag_name == 'rox.internal.considerThrottleInPush':
                return self.internal_is_enabled_result
            return False

        def internal_flag_get_number_value_mock(flag_name):
            if flag_name == 'rox.internal.throttleFetchInSeconds':
                return self.internal_get_number_result
            return 0

        self.internal_flags_mock.is_enabled = internal_flag_is_enabled_mock
        self.internal_flags_mock.get_number_value = internal_flag_get_number_value_mock

        self.configuration_fetcher_mock = Mock(ConfigurationFetcher)
        self.error_reporter_mock = Mock(ErrorReporter)
        self.state_sender_mock = Mock(StateSender)
        self.configuration_parser_mock = Mock(ConfigurationParser)
        self.flag_setter_mock = Mock(FlagSetter)

    @patch('rox.core.core.ConfigurationParser')
    @patch('rox.core.core.ConfigurationFetcherRoxy')
    @patch('rox.core.core.StateSender')
    @patch('rox.core.core.ErrorReporter')
    @patch('rox.core.core.ConfigurationFetcher')
    def test_will_check_core_setup_when_options_with_roxy_ignore_bad_key(self, mock_configuration_fetcher, 
                                                                        mock_error_reporter, mock_state_sender, 
                                                                        mock_config_fetcher_roxy, mock_configuration_parser):
        sdk_settings = SdkSettings('ignore_this', None)
        rox_options_mock = Mock(
            roxy_url='http://site.com',
            fetch_interval=30
        )
        rox_options_mock.is_self_managed.return_value = False
        device_props = Mock(rox_options=rox_options_mock)
        mock_configuration_fetcher.return_value = self.configuration_fetcher_mock
        mock_error_reporter.return_value = self.error_reporter_mock
        mock_state_sender.return_value = self.state_sender_mock
        mock_config_fetcher_roxy.return_value = Mock(ConfigurationFetcherRoxy)
        mock_configuration_parser.return_value = self.configuration_parser_mock

        c = Core()
        c.setup(sdk_settings, device_props)
        c.shutdown()

    @patch('rox.core.core.ConfigurationParser')
    @patch('rox.core.core.StateSender')
    @patch('rox.core.core.ErrorReporter')
    @patch('rox.core.core.ConfigurationFetcher')
    def test_will_check_core_setup_when_no_options(self, mock_configuration_fetcher, mock_error_reporter, 
                                                    mock_state_sender, mock_configuration_parser):
        sdk_settings = SdkSettings('aaaaaaaaaaaaaaaaaaaaaaaa', None)
        device_props = Mock(rox_options=RoxOptions())
        mock_configuration_fetcher.return_value = self.configuration_fetcher_mock
        mock_error_reporter.return_value = self.error_reporter_mock
        mock_state_sender.return_value = self.state_sender_mock
        mock_configuration_parser.return_value = self.configuration_parser_mock

        c = Core()
        c.setup(sdk_settings, device_props)
        c.shutdown()

    def test_will_fail_with_no_api_key_provided(self):
        sdk_settings = SdkSettings(None, None)
        device_props = Mock(rox_options=RoxOptions())
        device_props.rollout_key.return_value = None

        c = Core()
        with self.assertRaises(Exception) as context:
            c.setup(sdk_settings, device_props)
            c.shutdown()   

        self.assertEqual(type(context.exception).__name__, 'ValueError')
        self.assertEqual('Invalid rollout apikey - must be specified', str(context.exception))

    def test_will_fail_with_bad_api_key_provided(self):
        sdk_settings = SdkSettings('aaaaaaaaaaaaaaaaaaaaaaaaa', None)
        device_props = Mock(rox_options=RoxOptions())
        device_props.rollout_key.return_value = None

        c = Core()

        with self.assertRaises(Exception) as context:
            c.setup(sdk_settings, device_props)
            c.shutdown()

        self.assertEqual(type(context.exception).__name__, 'ValueError')
        self.assertEqual('Illegal rollout apikey', str(context.exception))

    def test_passes_with_mongo_api_key_provided(self):
        sdk_settings = SdkSettings('12345678901234567890abcd', None)
        device_props = Mock(rox_options=RoxOptions())
        device_props.rollout_key.return_value = None

        c = Core()
        c.setup(sdk_settings, device_props)
        c.shutdown()
        # No error raised

    def test_passes_with_uuid_api_key_provided(self):
        sdk_settings = SdkSettings('e50e3666-15a1-11ee-9900-00155deb2761', None)
        device_props = Mock(rox_options=RoxOptions())
        device_props.rollout_key.return_value = None

        c = Core()
        c.setup(sdk_settings, device_props)
        c.shutdown()
        # No error raised

    @patch('rox.core.core.FlagSetter')
    @patch('rox.core.core.ConfigurationParser')
    @patch('rox.core.core.StateSender')
    @patch('rox.core.core.ErrorReporter')
    @patch('rox.core.core.datetime')
    @patch('rox.core.core.InternalFlags')
    @patch('rox.core.core.ConfigurationFetcher')
    def test_will_check_kill_switch_off(self, mock_configuration_fetcher, mock_internal_flags, date_time, 
                                        mock_error_reporter, mock_state_sender, mock_configuration_parser,
                                        mock_flag_setter):
        sdk_settings = SdkSettings('aaaaaaaaaaaaaaaaaaaaaaaa', None)
        device_props = Mock(rox_options=RoxOptions())
        mock_internal_flags.return_value = self.internal_flags_mock
        mock_configuration_fetcher.return_value = self.configuration_fetcher_mock
        mock_error_reporter.return_value = self.error_reporter_mock
        mock_state_sender.return_value = self.state_sender_mock
        mock_configuration_parser.return_value = self.configuration_parser_mock
        mock_flag_setter.return_value = self.flag_setter_mock

        c = Core()
        date_time.now.return_value = datetime(2018, 11, 5, 9, 0, 0) # because God liked to get work done early in the morning while he was feeling fresh
        c.setup(sdk_settings, device_props).result()

        fetch_call_before_fetch = self.configuration_fetcher_mock.fetch.call_count

        date_time.now.return_value = datetime(2019, 11, 5, 9, 0, 0)
        c.fetch()

        self.assertEqual(self.configuration_fetcher_mock.fetch.call_count, fetch_call_before_fetch + 1)

        date_time.now.return_value = datetime(2019, 11, 5, 9, 0, 5)
        c.fetch()
        self.assertEqual(self.configuration_fetcher_mock.fetch.call_count, fetch_call_before_fetch + 2)

        c.fetch(True)
        self.assertEqual(self.configuration_fetcher_mock.fetch.call_count, fetch_call_before_fetch + 3)

        date_time.now.return_value = datetime(2019, 11, 5, 9, 0, 12)
        c.fetch()
        self.assertEqual(self.configuration_fetcher_mock.fetch.call_count, fetch_call_before_fetch + 4)

        c.shutdown()

    @patch('rox.core.core.FlagSetter')
    @patch('rox.core.core.ConfigurationParser')
    @patch('rox.core.core.StateSender')
    @patch('rox.core.core.ErrorReporter')
    @patch('rox.core.core.datetime')
    @patch('rox.core.core.InternalFlags')
    @patch('rox.core.core.ConfigurationFetcher')
    def test_will_check_kill_switch_on_not_consider_push(self, mock_configuration_fetcher, mock_internal_flags, 
                                                        mock_date_time, mock_error_reporter, mock_state_sender, 
                                                        mock_configuration_parser, mock_flag_setter):
        self.internal_get_number_result = 10
        sdk_settings = SdkSettings('aaaaaaaaaaaaaaaaaaaaaaaa', None)
        device_props = Mock(rox_options=RoxOptions())
        mock_internal_flags.return_value = self.internal_flags_mock
        mock_configuration_fetcher.return_value = self.configuration_fetcher_mock
        mock_error_reporter.return_value = self.error_reporter_mock
        mock_state_sender.return_value = self.state_sender_mock
        mock_configuration_parser.return_value = self.configuration_parser_mock
        mock_flag_setter.return_value = self.flag_setter_mock

        c = Core()
        mock_date_time.now.return_value = datetime(2018, 11, 5, 9, 0, 0)
        c.setup(sdk_settings, device_props).result()

        fetch_call_before_fetch = self.configuration_fetcher_mock.fetch.call_count

        mock_date_time.now.return_value = datetime(2019, 11, 5, 9, 0, 0)
        c.fetch()

        self.assertEqual(self.configuration_fetcher_mock.fetch.call_count, fetch_call_before_fetch + 1)

        mock_date_time.now.return_value = datetime(2019, 11, 5, 9, 0, 5)
        c.fetch()
        self.assertEqual(self.configuration_fetcher_mock.fetch.call_count, fetch_call_before_fetch + 1)

        c.fetch(True)
        self.assertEqual(self.configuration_fetcher_mock.fetch.call_count, fetch_call_before_fetch + 2)

        mock_date_time.now.return_value = datetime(2019, 11, 5, 9, 0, 12)
        c.fetch()
        self.assertEqual(self.configuration_fetcher_mock.fetch.call_count, fetch_call_before_fetch + 3)

        c.shutdown()

    @patch('rox.core.core.FlagSetter')
    @patch('rox.core.core.ConfigurationParser')
    @patch('rox.core.core.StateSender')
    @patch('rox.core.core.ErrorReporter')
    @patch('rox.core.core.datetime')
    @patch('rox.core.core.InternalFlags')
    @patch('rox.core.core.ConfigurationFetcher')
    def test_will_check_kill_switch_on_consider_push(self, mock_configuration_fetcher, mock_internal_flags, 
                                                    mock_date_time, mock_error_reporter, mock_state_sender, 
                                                    mock_configuration_parser, mock_flag_setter):
        self.internal_get_number_result = 10
        self.internal_is_enabled_result = True
        sdk_settings = SdkSettings('aaaaaaaaaaaaaaaaaaaaaaaa', None)
        device_props = Mock(rox_options=RoxOptions())
        mock_internal_flags.return_value = self.internal_flags_mock
        mock_configuration_fetcher.return_value = self.configuration_fetcher_mock
        mock_error_reporter.return_value = self.error_reporter_mock
        mock_state_sender.return_value = self.state_sender_mock
        mock_configuration_parser.return_value = self.configuration_parser_mock
        mock_flag_setter.return_value = self.flag_setter_mock

        c = Core()
        mock_date_time.now.return_value = datetime(2018, 11, 5, 9, 0, 0)

        c.setup(sdk_settings, device_props).result()

        fetch_call_before_fetch = self.configuration_fetcher_mock.fetch.call_count

        mock_date_time.now.return_value = datetime(2019, 11, 5, 9, 0, 0)
        c.fetch()
        self.assertEqual(self.configuration_fetcher_mock.fetch.call_count, fetch_call_before_fetch + 1)

        mock_date_time.now.return_value = datetime(2019, 11, 5, 9, 0, 5)
        c.fetch()
        self.assertEqual(self.configuration_fetcher_mock.fetch.call_count, fetch_call_before_fetch + 1)

        c.fetch(True)
        self.assertEqual(self.configuration_fetcher_mock.fetch.call_count, fetch_call_before_fetch + 1)

        mock_date_time.now.return_value = datetime(2019, 11, 5, 9, 0, 12)
        c.fetch()
        self.assertEqual(self.configuration_fetcher_mock.fetch.call_count, fetch_call_before_fetch + 2)

        c.shutdown()

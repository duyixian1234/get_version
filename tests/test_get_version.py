from click.testing import CliRunner
from get_version.__main__ import get_version
from unittest import mock


@mock.patch('get_version.__main__.getstatusoutput')
def test_success(mock_getstatusoutput):
    mock_getstatusoutput.return_value = 0, 'Python 3.7.2'

    runner = CliRunner()
    result = runner.invoke(get_version, ['python'])
    assert result.exit_code == 0
    assert 'Python 3.7.2' in result.output
    mock_getstatusoutput.assert_called_with('python -V')


def test_unsupport():
    runner = CliRunner()
    result = runner.invoke(get_version, ['jython'])
    assert result.exit_code == 0
    assert 'Not support for jython' in result.output


@mock.patch('get_version.__main__.getstatusoutput')
def test_failure(mock_getstatusoutput):
    mock_getstatusoutput.return_value = 127, 'command not found'

    runner = CliRunner()
    result = runner.invoke(get_version, ['go'])
    assert result.exit_code == 127
    assert 'command not found' in result.output
    mock_getstatusoutput.assert_called_with('go version')

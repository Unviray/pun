from pathlib import Path
import pytest

from click.testing import CliRunner

from pun import cli


@pytest.fixture
def runner():
    r = CliRunner()
    return r


def test_puntask(runner):
    result = runner.invoke(cli.main, 'touch')

    assert result.exit_code == 0
    assert 'success' in result.output
    assert Path('file') in list(Path().iterdir())

    result = runner.invoke(cli.main, 'remove')


def test_change_dir(runner):
    result = runner.invoke(cli.main, 'touch_cd')

    assert result.exit_code == 0
    assert 'success' in result.output
    assert Path('./tests/file') in list(Path('./tests').iterdir())

    result = runner.invoke(cli.main, 'remove_cd')


def test_fail(runner):
    result = runner.invoke(cli.main, 'fail')

    assert result.exit_code == 1
    assert 'fail' in result.output


def test_no_target(runner):
    result = runner.invoke(cli.main, 'foo_bar')

    assert result.exit_code == 2
    assert 'No target foo_bar' in result.output


def test_default(runner):
    result = runner.invoke(cli.main)

    assert result.exit_code == 0
    assert 'default' in result.output


def test_fixture(runner):
    result1 = runner.invoke(cli.main, 'need_fixture1')
    result2 = runner.invoke(cli.main, 'need_fixture2')
    result3 = runner.invoke(cli.main, 'need_fixture3')
    result4 = runner.invoke(cli.main, 'need_fixture4')

    assert result1.exit_code == 0
    assert result2.exit_code == 0
    assert result3.exit_code == 0
    assert result4.exit_code == 0

    assert '1' in result1.output
    assert '3' in result2.output
    assert '6' in result3.output
    assert '10' in result4.output


def test_no_fixture(runner):
    result = runner.invoke(cli.main, 'no_fixture')

    assert result.exit_code == 2

    assert 'No fixture undefined' in result.output


def test_help(runner):
    result = runner.invoke(cli.main, 'help')

    assert result.exit_code == 0

    assert 'clean' in result.output
    assert 'fail' not in result.output


def test_env(runner):
    result = runner.invoke(cli.main, 'environ')

    assert result.exit_code == 0
    assert '34' in result.output


def test_as_option(runner):
    result = runner.invoke(cli.main, '--option')

    assert result.exit_code == 0
    assert 'optioned' in result.output

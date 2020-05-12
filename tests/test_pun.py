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

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

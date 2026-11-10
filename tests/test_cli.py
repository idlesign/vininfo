import pytest

click = pytest.importorskip("click")

from click.testing import CliRunner

from vininfo.cli import entry_point


def test_show_valid_vin():
    result = CliRunner().invoke(entry_point, ["show", "1M8GDM9AXKP042788"])
    assert result.exit_code == 0
    assert "Basic:" in result.output


def test_show_rejects_invalid_vin_without_traceback():
    result = CliRunner().invoke(entry_point, ["show", "tooshort"])
    assert result.exit_code == 2
    assert "17 chars" in result.output
    assert "Traceback" not in result.output


def test_check_rejects_invalid_vin_without_traceback():
    result = CliRunner().invoke(entry_point, ["check", "tooshort"])
    assert result.exit_code == 2
    assert "17 chars" in result.output
    assert "Traceback" not in result.output

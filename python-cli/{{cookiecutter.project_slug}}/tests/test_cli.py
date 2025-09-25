from typer.testing import CliRunner
from {{cookiecutter.package_name}}.cli import app

runner = CliRunner()

def test_hello():
    result = runner.invoke(app, ["hello", "--name", "Tester"])
    assert "Hello, Tester!" in result.output

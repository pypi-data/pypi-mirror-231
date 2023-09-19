from pathlib import Path

import pexpect
import pytest


@pytest.fixture
def bin():
    import os
    yield Path(os.environ["BIN_PATH"])


def test_template_generation_via_cli(bin: Path, tmp_path: Path):
    # generate project
    child = pexpect.spawn(str(bin/"init-python-project"), ["my-project"], cwd=tmp_path, timeout=3)
    child.expect('.* project.*')
    child.sendline('My Project')
    child.expect('.* package.*')
    child.sendline('') # accept default
    child.expect('.* pre-commit.*')
    child.send('y')
    child.expect('.* bumpversion.*')
    child.send('y')
    child.expect('.* documentation.*')
    child.sendline('') # accept default
    child.expect('.* platform.*')
    child.sendline('') # accept default
    child.expect('.* name.*')
    child.sendline('cool-user') # accept default
    child.expect('.* remote.*')
    child.sendline('') # accept default
    child.expect('.* initial git branch.*')
    child.sendline('') # accept default

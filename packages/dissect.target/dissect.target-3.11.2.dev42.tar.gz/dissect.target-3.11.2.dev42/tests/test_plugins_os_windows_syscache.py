from dissect.target.plugins.os.windows.syscache import SyscachePlugin

from ._utils import absolute_path


def test_syscache_plugin(target_win, fs_win):
    syscache_file = absolute_path("data/Syscache.hve")
    fs_win.map_file("System Volume Information/Syscache.hve", syscache_file)

    target_win.add_plugin(SyscachePlugin)

    results = list(target_win.syscache())
    assert len(results) == 401


from gitchangelog.gitchangelog import gitlog_parser, changelog

log = """
be2f672 - [2019/06/20] fix(jira): catched an incorrect exception (Feng Yu)
84add25 - [2019/06/20] fix(case): bind_jira_bug occured exception when loads json (Feng Yu)
419a43c - [2019/06/19] fix(config_topo): add exception for force user logout (hytang)
fb89229 - [2019/06/19] fix(config_topo): add try for clear firebox and cluster (hytang)
5b29e76 - [2019/06/19] refactor(framework/net/telnet/windows.py): Remove telent pn code (jinhui.wei)
cea6c29 - [2019/06/19] fix(ssh): set test pc user/passwd (joseph.fan)
1a67107 - [2019/06/19] fix(ssh): edit test pc ip and password (joseph.fan)
7a3c8e2 - [2019/06/19] refactor(framework/net/telnet/windows.py): Remove telent windows code (jinhui.wei)
19c4bf7 - [2019/06/19] feat(Dict): support compatibly value convert with types in int and bool (Feng Yu)
4522c09 - [2019/06/19] feat(framework/types/pageobject.py): Reload __repr__ to print readable info (jinhui.wei)
0949613 - [2019/06/19] fix(jira): remove the unused import (Feng Yu)
be3115b - [2019/06/19] fix(jira): make Jira not based on Service (Feng Yu)
c507727 - [2019/06/19] fix(jira): add the missing type hint (Feng Yu)
ca1b216 - [2019/06/19] fix(jira): create jira ticket failed (Feng Yu)
4fe3cde - [2019/06/19] feat(framework/types/pageobject.py): Add load function in PageObject to load args (jinhui.wei)
5b4fe0b - [2019/06/19] Refactor ssh sleep (Zhanhong Fan)
ca0f736 - [2019/06/19] chore(ci): update sonarqube and coverage to ignore wgcmd.py (Junkai Zhang @MacBookPro)
d101c27 - [2019/06/19] fix(jira): create jira ticket failed (Feng Yu)
43af169 - [2019/06/18] refactor(watchguard/net/telnet/switch.py): Modify typing mistake (jinhui.wei)
2c5075b - [2019/06/18] refactor(watchguard/net/telnet/switch.py): Fix conflicts (jinhui.wei)
fd5d7f9 - [2019/06/18] refactor(watchguard/net/telnet/switch.py): Add typing (jinhui.wei)
e82239a - [2019/06/18] refactor(watchguard/net/telnet/switch.py): Add typing (jinhui.wei)
63b17ea - [2019/06/18] refactor(qtest): rename class `QtestAuth` to `Auth` (Feng Yu)
91d21c5 - [2019/06/18] test(qtest): move unittest of qtest to test_qtest.py (Feng Yu)
e68fc4b - [2019/06/18] test(unittest): update unittest of qtest (Feng Yu)
96b3fe7 - [2019/06/18] refactor(qtest): add back the class `qTestAuth` (Feng Yu)
2b972ee - [2019/06/18] refactor(qtest): fix conflicts (Feng Yu)
4f4fd49 - [2019/06/18] refactor(helper): remove class `qTestAuth` from helper.py (Feng Yu)
0d5d930 - [2019/06/18] refactor(qtest): remove class `QtestService` from `services.py` (Feng Yu)
661f497 - [2019/06/18] refactor(qtest): add new module `pytest.py` (Feng Yu)
4fbc935 - [2019/06/18] refactor(helper): remove class `qTestAuth` from helper.py (Feng Yu)
8825ce8 - [2019/06/18] refactor(qtest): remove class `QtestService` from `services.py` (Feng Yu)
38a3518 - [2019/06/18] refactor(jira): rename param `case` to `testcase` (Feng Yu)
94f0b11 - [2019/06/18] refactor(jira): rename param `case` to `testcase` (Feng Yu)
afaf3db - [2019/06/18] refactor(qtest): add new module `pytest.py` (Feng Yu)
785e732 - [2019/06/18] split jira initialize and call method into two lines (Feng Yu)
0578ff1 - [2019/06/18] refactor(watchguard/net/telnet/imap.py): remove old code about imap (jinhui.wei)
85e15aa - [2019/06/18] refactor(watchguard/net/telnet/telnet.py): Use new telnet instead old (jinhui.wei)
cf733a7 - [2019/06/18] refactor(jira): fix discussion (Feng Yu)
7ca1eb3 - [2019/06/18] fix(ssh): edit test method name (Joseph Fan)
1696f6a - [2019/06/18] fix(ssh): rename test methods and add logout test (Joseph Fan)
26dd3bd - [2019/06/18] refactor(watchguard/net/telnet/imap.py): add typing (jinhui.wei)
22c1a89 - [2019/06/18] refactor(jira): remove the old code from services.py (Feng Yu)
eec18d3 - [2019/06/18] remove unused import (Feng Yu)
a02e403 - [2019/06/18] feat(config-topo): move get isp dnsmasq from cofig-topo to case_template (Feng Yu)
4161c38 - [2019/06/18] feat(watchguard/net/telnet/telnet.py): add typing (jinhui.wei)
f2afdbc - [2019/06/18] fix(config_topo): remove commented code (hytang)
82a00d3 - [2019/06/18] fix code smell (Feng Yu)
2a54ad5 - [2019/06/18] fix(jira): fix discussions (Feng Yu)
b75083e - [2019/06/18] doc(hint): Add type hint for jira module (Feng Yu)
0110488 - [2019/06/18] refactor(jira): split jira related code from helper (Feng Yu)
3cb5d5d - [2019/06/18] refact(config_topo): use new firebox.force_logout to replace wgadmin.force_logout (hytang)
f5f8a7e - [2019/06/17] refactor(graylog): fix conflicts and resolve some code smell (Feng Yu)
8704b80 - [2019/06/17] refactor(graylog): split graylog from helper (Feng Yu)
c90355f - [2019/06/17] fix(test): add TEST_PC_IP (Joseph Fan)
212a885 - [2019/06/17] fix(jira): fix discussions (Feng Yu)
3c9ea20 - [2019/06/17] fix(ci): remove --branch para from pytest command (Junkai Zhang @MacBookPro)
82d8280 - [2019/06/17] chore(ci): revert to use one section for unittest (Junkai Zhang @MacBookPro)
ec710ca - [2019/06/17] doc(hint): Add type hint for jira module (Feng Yu)
bb714f0 - [2019/06/17] feat(watchguard/net/telnet/telnet.py): modify import try_reconnect decorator for telnet (jinhui.wei)
719b1ff - [2019/06/17] refactor(jira): split jira related code from helper (Feng Yu)
0051ebe - [2019/06/17] feat(watchguard/net/telnet/telnet.py): modify import module name (jinhui.wei)
9c09313 - [2019/06/17] feat(watchguard/net/telnet/firbox.py): add typing (jinhui.wei)
5f12f12 - [2019/06/17] chore(ci): update CI to run different tests according to branch (Junkai Zhang @MacBookPro)
e562451 - [2019/06/17] feat(config-topo): SpamBlocker between Firebox to server go into private line (Feng Yu)
3e56e32 - [2019/06/17] fix(ssh): reset decode methods import location (Joseph Fan)
45fbee7 - [2019/06/17] fix(firebox.py): remove unused import (hytang)
f606de4 - [2019/06/17] fix(firebox.py): use new import path for wgassert (hytang)
532e4b2 - [2019/06/17] fix(test_device_firebox): use new import path for WgcmdWrapper (hytang)
00adf53 - [2019/06/17] fix(firebox.py): use new import path and replace raise Exception() (hytang)
6471adf - [2019/06/17] fix(framework/bin/xtm_encoder): fix used wrong var name (jinhui)
f39bc3c - [2019/06/17] Return the pageobject values before save pageobject (jinhui)
e67af5f - [2019/06/17] test(tests): use mark for pytest instead of skipif with CI support (Junkai Zhang @MacBookPro)
91e3081 - [2019/06/17] refactor: move force_logout to device firebox.py (hytang)
a09a97a - [2019/06/17] fix(ssh): set ssh to use absolute import (Joseph Fan)
7fbac37 - [2019/06/17] feat(utils/config_topo): start DNS server on ISP by default (Albert Liu)
b3963e2 - [2019/06/17] refactor(ssh): refactor login and logout (Joseph Fan)
"""

def test_gitlog_parser():
    parsed = gitlog_parser(log)
    print(parsed)
    assert isinstance(parsed, list)
    assert isinstance(parsed[0], dict)
    assert {
        'date':'2019/06/14', 
        'author':"Joseph Fan", 
        "title":"add ssh mark",
        "scope": "ssh",
        "type": "fix"
        } in parsed

def test_changelog_group_by_type():
    gitlogs = gitlog_parser(log)
    markdown = changelog(view='type', gitlogs=gitlogs)
    print(markdown)
    # assert 'add ssh mark' in markdown

def test_changelog_group_by_author():
    gitlogs = gitlog_parser(log)
    markdown = changelog(view='author', gitlogs=gitlogs)
    print(markdown)
    assert 'add ssh mark' in markdown

def test_changelog_group_by_scope():
    gitlogs = gitlog_parser(log)
    markdown = changelog(view='scope', gitlogs=gitlogs)
    print(markdown)
    assert 'add ssh mark' in markdown

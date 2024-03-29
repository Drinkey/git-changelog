#!/usr/bin/env python3

import re
from typing import List, Dict, Tuple
import click

def gitlog_parser(log: str) -> List[Dict]:
    """Parse the git log out of of following

    git log --no-merges --abbrev-commit \
            --date=format:"%Y/%m/%d" \
            --pretty=format:"%Cred%h%Creset - %C(green)[%cd] %Cblue%s %Creset(%an)" \
            --since="6 days ago"
    
    :param log: Git log out put in above format
    :type log: str
    :return: A list of dict that including parsed git logs
    :rtype: List[Dict]
    """
    pattern = re.compile(r"""
        .*-\s
        \[(.*)\]\s    # date
        (.*)          # type
        \((.*)\):\s   # scope
        (.*)\s        # title
        \((.*)\)      # author
        """, re.VERBOSE)
    
    gitlogs = list()
    for line in log.split('\n'):
        if not line:
            continue
        match = pattern.match(line)
        if not match:
            print(f"line not match: {line}")
            continue
        gitlogs.append(dict(
            date=match.group(1),
            type = match.group(2),
            scope = match.group(3),
            title = match.group(4),
            author = match.group(5)
        ))
    return gitlogs

def not_support(gitlogs: List[Dict]):
    print("calling a not supported function")
    return ''

def group_by_key(key: str, gitlogs) -> Dict:
    """group `gitlogs` by `key`
    
    :param key: Which key to group by
    :type key: str
    :param gitlogs: The gitlogs List
    :type gitlogs: List[Dict]
    :return: Grouped Dict of gitlogs by key
    :rtype: Dict
    """
    result = dict()
    for _gitlog in gitlogs:
        _key = _gitlog[key]
        if _key not in result:
            result[_key] = list()
        result[_key].append(_gitlog)

    return result

def gitlog_to_md_by(key: str, fmt: str, title: str, gitlogs: List[Dict]) -> str:
    data = group_by_key(key, gitlogs)

    markdown = f'# {title}\n\n'
    for _keytype, _gitlog_items in data.items():
        markdown += f"## {_keytype}\n\n"
        for _item in _gitlog_items:
            markdown += fmt.format(**_item)
        markdown += "\n"
    return markdown

def gitlog_to_md_by_type(title: str, gitlogs: List[Dict]) -> str:
    fmt = "- **{date}** `{scope}` {title} __{author}__\n"
    return gitlog_to_md_by('type', fmt, title, gitlogs)

def gitlog_to_md_by_scope(title: str, gitlogs: List[Dict]) -> str:
    fmt = "- **{date}** {type} `{author}` {title}\n"
    return gitlog_to_md_by('scope', fmt, title, gitlogs)

def gitlog_to_md_by_author(title: str, gitlogs: List[Dict]) -> str:
    fmt = "- **{date}** {type} `{scope}` {title}\n"
    return gitlog_to_md_by('author', fmt, title, gitlogs)

def gitlog_to_markdown(title: str, view: str, gitlogs: List[Dict]) -> str:
    _func_map = dict(
        type=gitlog_to_md_by_type,
        author=gitlog_to_md_by_author,
        scope=gitlog_to_md_by_scope
    )

    return _func_map.get(view, not_support)(title=title, gitlogs=gitlogs)

@click.command()
@click.option('--title', required=True, help='title of the changelog')
@click.option('--file', required=True, help='path of changelog file')
@click.option('--view', type=click.Choice(['type', 'scope', 'author']),
              default='type', help='which view want to generate')
def changelog(title, file, view):
    content = ''
    with open(file, 'r') as fp:
        content = fp.read()
    gitlogs = gitlog_parser(content)
    res = gitlog_to_markdown(title, view, gitlogs)
    print(res)

if __name__ == '__main__':
    changelog()
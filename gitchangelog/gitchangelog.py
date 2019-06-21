#!/usr/bin/env python3

import re
from typing import List, Dict
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
    pattern = re.compile(r".*-\s\[(.*)\]\s(.*)\((.*)\):\s(.*)\s\((.*)\)")
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

def group_by_type(title: str, gitlogs: List[Dict]) -> str:

    data = group_by_key('type', gitlogs)
    markdown = f'# {title}\n\n'
    for _type, _gitlog_items in data.items():
        markdown += f"## {_type}\n\n"
        for _item in _gitlog_items:
            markdown += f"- **{_item['date']}** `{_item['scope']}` {_item['title']} __{_item['author']}__\n"
        markdown += "\n"
    return markdown

def group_by_author(title: str, gitlogs: List[Dict]) -> str:
    data = group_by_key('author', gitlogs)
    markdown = f'# {title}\n\n'
    for _author, _gitlog_items in data.items():
        markdown += f"## {_author}\n\n"
        for _item in _gitlog_items:
            markdown += f"- **{_item['date']}** {_item['type']} `{_item['scope']}` {_item['title']}\n"
        markdown += "\n"
    return markdown

def group_by_scope(title: str, gitlogs: List[Dict]) -> str:
    data = group_by_key('scope', gitlogs)
    markdown = f'# {title}\n\n'
    for _scope, _gitlog_items in data.items():
        markdown += f"## {_scope}\n\n"
        for _item in _gitlog_items:
            markdown += f"- **{_item['date']}** {_item['type']} `{_item['author']}` {_item['title']}\n"
        markdown += "\n"
    return markdown

def gitlog_to_markdown(title: str, view: str, gitlogs: List[Dict]) -> str:
    _func_map = dict(
        type=group_by_type,
        author=group_by_author,
        scope=group_by_scope
    )

    return _func_map.get(view, not_support)(title, gitlogs)

@click.command()
@click.option('--title', required=True, help='title of the changelog')
@click.option('--file', required=True, help='read from file')
@click.option('--view', type=click.Choice(['type', 'scope', 'author']),
default='type')
def changelog(title, file, view):
    content = ''
    with open(file, 'r') as fp:
        # print('reading file')
        content = fp.read()
    gitlogs = gitlog_parser(content)
    res = gitlog_to_markdown(title, view, gitlogs)
    print(res)

if __name__ == '__main__':
    changelog()
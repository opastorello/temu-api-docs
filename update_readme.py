#!/usr/bin/env python3
"""Atualiza contagens, data e badges no README.md."""

import os
import re
from datetime import datetime, timezone, timedelta

BRT = timezone(timedelta(hours=-3))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def count_md(rel_path):
    full = os.path.join(BASE_DIR, rel_path)
    if not os.path.isdir(full):
        return 0
    return sum(1 for f in os.listdir(full) if f.endswith('.md'))


def count_md_recursive(rel_path):
    full = os.path.join(BASE_DIR, rel_path)
    if not os.path.isdir(full):
        return 0
    total = 0
    for root, _, files in os.walk(full):
        total += sum(1 for f in files if f.endswith('.md'))
    return total


def replace_count(text, key, value):
    return re.sub(
        rf'(<!-- count:{re.escape(key)} -->)\d+(<!-- /count -->)',
        rf'\g<1>{value}\2',
        text
    )


counts = {
    'developer-guide':       count_md_recursive('developer-guide'),
    'api-integration-guide': count_md_recursive('api-integration-guide'),
    'authorization':         count_md('api-reference/authorization'),
    'product':               count_md('api-reference/product'),
    'order':                 count_md('api-reference/order'),
    'shipping':              count_md('api-reference/shipping'),
    'returns':               count_md('api-reference/returns'),
    'promotions':            count_md('api-reference/promotions'),
    'compliance':            count_md('api-reference/compliance'),
    'ads':                   count_md('api-reference/ads'),
    'warehouse':             count_md('api-reference/warehouse'),
    'flash':                 count_md('api-reference/flash'),
    'webhook':               count_md('api-reference/webhook'),
    'other':                 count_md('api-reference/other'),
}

total = sum(counts.values())
today = datetime.now(BRT).strftime('%Y-%m-%d')
today_badge = today.replace('-', '--')

readme_path = os.path.join(BASE_DIR, 'README.md')
with open(readme_path, encoding='utf-8') as f:
    text = f.read()

# Atualiza contagens por diretório
for key, val in counts.items():
    text = replace_count(text, key, str(val))

# Atualiza badge de total de arquivos
text = re.sub(
    r'<!-- badge:files -->.*?<!-- /badge -->',
    f'<!-- badge:files -->![{total} arquivos](https://img.shields.io/badge/arquivos-{total}-blue)<!-- /badge -->',
    text
)

# Atualiza badge de data
text = re.sub(
    r'<!-- badge:date -->.*?<!-- /badge -->',
    f'<!-- badge:date -->![{today}](https://img.shields.io/badge/atualizado-{today_badge}-green)<!-- /badge -->',
    text
)

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"README atualizado — {total} arquivos, {today}")

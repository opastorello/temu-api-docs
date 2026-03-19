#!/usr/bin/env python3
"""
Temu API Docs Updater
=====================
Verifica e atualiza a documentação local comparando com partner.temu.com.

USO:
  python update_docs.py                   # atualiza tudo
  python update_docs.py --dry-run         # mostra o que mudaria sem salvar
  python update_docs.py --section guides  # só atualiza os guias
  python update_docs.py --section apis    # só atualiza os endpoints

COOKIES (necessário para endpoints de API):
  Se der "Forbidden for Visitor" nos endpoints, abra partner.temu.com no browser,
  copie os cookies e cole na variável COOKIES abaixo, ou rode:
    python update_docs.py --update-cookies "api_uid=...; _bee=...; _nano_fp=..."
"""

import urllib.request
import json
import os
import re
import sys
import hashlib
import argparse
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser
from datetime import datetime, timezone, timedelta

BRT = timezone(timedelta(hours=-3))

WORKERS = 20  # requisições paralelas
_print_lock = threading.Lock()

def safe_print(*args, **kwargs):
    with _print_lock:
        print(*args, **kwargs)

# ── Configuração ──────────────────────────────────────────────────────────────

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COOKIES_FILE = os.path.join(BASE_DIR, '.cookies')

# Cookies para endpoints de API (doc_type=2).
# Atualizar quando expirar ou usar --update-cookies
DEFAULT_COOKIES = "api_uid=CtYxJmmbbS29O6e19DwDAg==; _nano_fp=GWiVbWiVbaijb8D2q3i89#PwvEAHayNxhN_qiuNG7BC; _bee=uocV46WKdEKSn24Jr71i8cuzXSKZqapL"

# Mapeamento: api_name → pasta
FOLDER_MAP = {
    "bg.open.": "api-reference/authorization",
    "temu.local.mall.": "api-reference/authorization",
    "bg.local.goods.": "api-reference/product",
    "temu.local.goods.": "api-reference/product",
    "temu.local.product.": "api-reference/product",
    "temu.local.sku.": "api-reference/product",
    "bg.goods.compliancelabel": "api-reference/product",
    "bg.local.compliance.": "api-reference/compliance",
    "bg.compliance.": "api-reference/compliance",
    "bg.arbok.": "api-reference/compliance",
    "bg.order.": "api-reference/order",
    "temu.order.": "api-reference/order",
    "bg.freight.": "api-reference/shipping",
    "bg.logistics.": "api-reference/shipping",
    "temu.logistics.": "api-reference/shipping",
    "temu.track.": "api-reference/shipping",
    "bg.aftersales.": "api-reference/returns",
    "temu.aftersales.": "api-reference/returns",
    "bg.promotion.": "api-reference/promotions",
    "temu.searchrec.ad.": "api-reference/ads",
    "bg.cooperativewarehouse.": "api-reference/warehouse",
    "bg.flash.": "api-reference/flash",
    "bg.tmc.": "api-reference/webhook",
}

# ── HTML → Markdown ───────────────────────────────────────────────────────────

class HTMLToMarkdown(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []
        self._tag_stack = []
        self._list_stack = []
        self._list_counter = []
        self._in_code = False
        self._in_pre = False
        self._in_table = False
        self._table_rows = []
        self._current_row = []
        self._current_cell = []
        self._is_header_row = False
        self._link_href = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self._tag_stack.append(tag)
        if tag in ('h1','h2','h3','h4','h5','h6'):
            level = int(tag[1])
            self.result.append('\n' + '#' * level + ' ')
        elif tag == 'p':
            self.result.append('\n\n')
        elif tag == 'br':
            self.result.append('  \n')
        elif tag in ('strong','b'):
            self.result.append('**')
        elif tag in ('em','i'):
            self.result.append('*')
        elif tag == 'code' and not self._in_pre:
            self._in_code = True
            self.result.append('`')
        elif tag == 'pre':
            self._in_pre = True
            self.result.append('\n```\n')
        elif tag == 'ul':
            self._list_stack.append('ul')
            self._list_counter.append(0)
        elif tag == 'ol':
            self._list_stack.append('ol')
            self._list_counter.append(0)
        elif tag == 'li':
            if self._list_stack:
                kind = self._list_stack[-1]
                indent = '  ' * (len(self._list_stack) - 1)
                if kind == 'ul':
                    self.result.append(f'\n{indent}- ')
                else:
                    self._list_counter[-1] += 1
                    self.result.append(f'\n{indent}{self._list_counter[-1]}. ')
        elif tag == 'a':
            self._link_href = attrs.get('href', '')
            self.result.append('[')
        elif tag == 'table':
            self._in_table = True
            self._table_rows = []
        elif tag == 'tr':
            self._current_row = []
            self._is_header_row = 'th' in [a[0] for a in self.get_starttag_text().lower().split() if '=' not in a]
        elif tag in ('td','th'):
            self._current_cell = []
            if tag == 'th':
                self._is_header_row = True
        elif tag == 'blockquote':
            self.result.append('\n> ')
        elif tag == 'hr':
            self.result.append('\n---\n')
        elif tag == 'img':
            alt = attrs.get('alt', 'image')
            src = attrs.get('src', '')
            self.result.append(f'![{alt}]({src})')

    def handle_endtag(self, tag):
        if self._tag_stack and self._tag_stack[-1] == tag:
            self._tag_stack.pop()
        if tag in ('h1','h2','h3','h4','h5','h6'):
            self.result.append('\n')
        elif tag in ('strong','b'):
            self.result.append('**')
        elif tag in ('em','i'):
            self.result.append('*')
        elif tag == 'code' and not self._in_pre:
            self._in_code = False
            self.result.append('`')
        elif tag == 'pre':
            self._in_pre = False
            self.result.append('\n```\n')
        elif tag in ('ul','ol'):
            if self._list_stack:
                self._list_stack.pop()
                self._list_counter.pop()
            self.result.append('\n')
        elif tag == 'a':
            self.result.append(f']({self._link_href})')
            self._link_href = None
        elif tag in ('td','th'):
            self._current_row.append(''.join(self._current_cell).strip())
            self._current_cell = []
        elif tag == 'tr':
            self._table_rows.append((self._current_row, self._is_header_row))
        elif tag == 'table':
            self._in_table = False
            self._render_table()
        elif tag == 'p':
            self.result.append('\n')

    def handle_data(self, data):
        if self._in_table and self._current_cell is not None:
            self._current_cell.append(data)
        else:
            self.result.append(data)

    def _render_table(self):
        if not self._table_rows:
            return
        self.result.append('\n')
        header_done = False
        for row, is_header in self._table_rows:
            self.result.append('| ' + ' | '.join(cell.replace('|','\\|') for cell in row) + ' |\n')
            if (is_header or not header_done) and not header_done:
                self.result.append('|' + '---|' * len(row) + '\n')
                header_done = True
        self.result.append('\n')

    def get_markdown(self):
        text = ''.join(self.result)
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()

def html_to_markdown(html):
    parser = HTMLToMarkdown()
    parser.feed(html)
    return parser.get_markdown()

# ── Fetch helpers ─────────────────────────────────────────────────────────────

def get_cookies():
    if os.path.exists(COOKIES_FILE):
        with open(COOKIES_FILE) as f:
            return f.read().strip()
    return DEFAULT_COOKIES

def make_request(url, payload, cookies=None):
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Referer': 'https://partner.temu.com/documentation',
        'Origin': 'https://partner.temu.com',
        'xhr-flag': 'true',
    }
    if cookies:
        headers['Cookie'] = cookies
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())

def fetch_menu():
    data = make_request('https://partner.temu.com/riemann/api/v2/menu/list', {})
    return data.get('result', {}).get('menu_list', [])

def fetch_guide(menu_code):
    data = make_request('https://partner.temu.com/riemann/api/v2/menu/document/detail', {'menu_code': menu_code})
    return data.get('result', {})

def fetch_api_spec(api_id, cookies):
    data = make_request('https://partner.temu.com/riemann/api/v2/api/doc/detail/get', {'api_id': api_id}, cookies=cookies)
    return data

# ── Markdown builders ─────────────────────────────────────────────────────────

def param_tree_to_md(params, depth=0):
    if not params:
        return ''
    indent = '  ' * depth
    rows = []
    for p in params:
        req = 'Yes' if p.get('is_required') else 'No'
        desc = (p.get('param_desc') or '').replace('|', '\\|').replace('\n', ' ')
        example = (p.get('example') or '').replace('|', '\\|').replace('\n', ' ')
        rows.append(f"| {indent}{p.get('param_name','')} | {p.get('param_type','')} | {req} | {desc} | {example} |")
        if p.get('param_list'):
            rows.append(param_tree_to_md(p['param_list'], depth + 1))
    return '\n'.join(rows)

def api_to_markdown(doc):
    url = (doc.get('common_parameters') or {}).get('url_param', {}).get('url', 'https://openapi-b-global.temu.com/openapi/router')
    lines = [
        f"# {doc['api_id']}",
        f"\n**{doc.get('api_name', '')}**\n",
    ]
    if doc.get('api_desc'):
        lines.append(f"{doc['api_desc']}\n")
    lines.append(f"**Method:** POST  \n**URL:** {url}\n\n---\n")

    common = (doc.get('common_parameters') or {}).get('common_parameters') or []
    if common:
        lines.append("## Common Parameters\n\n| Parameter | Type | Required | Description |\n|---|---|---|---|")
        for p in common:
            desc = (p.get('param_desc') or '').replace('|', '\\|').replace('\n', ' ')
            lines.append(f"| {p.get('param_name','')} | {p.get('param_type','')} | {'Yes' if p.get('is_required') else 'No'} | {desc} |")
        lines.append('')

    req_params = (doc.get('request_parameters') or {}).get('open_param_list') or []
    if req_params:
        lines.append("## Request Parameters\n\n| Parameter | Type | Required | Description | Example |\n|---|---|---|---|---|")
        lines.append(param_tree_to_md(req_params))
        lines.append('')

    res_params = (doc.get('response_parameters') or {}).get('open_param_list') or []
    if res_params:
        lines.append("## Response Parameters\n\n| Parameter | Type | Required | Description | Example |\n|---|---|---|---|---|")
        lines.append(param_tree_to_md(res_params))
        lines.append('')

    errors = doc.get('error_param_list') or []
    if errors:
        lines.append("## Error Codes\n\n| Error Code | Message |\n|---|---|")
        for e in errors:
            msg = (e.get('error_msg') or '').replace('|', '\\|')
            lines.append(f"| {e.get('error_code','')} | {msg} |")
        lines.append('')

    samples = doc.get('request_sample_code') or []
    curl = next((s for s in samples if s.get('label') == 'CURL'), None)
    if curl:
        lines.append(f"## Request Example\n\n```bash\n{curl['value']}\n```\n")

    if doc.get('response_sample'):
        lines.append(f"## Response Example\n\n```json\n{doc['response_sample']}\n```")

    return '\n'.join(lines)

# ── File helpers ──────────────────────────────────────────────────────────────

def file_hash(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def get_folder_for_api(api_name):
    for prefix, folder in FOLDER_MAP.items():
        if api_name.startswith(prefix):
            return folder
    return 'api-reference/other'

def get_guide_folder(menu_name):
    name_lower = menu_name.lower()
    if 'developer' in name_lower or 'registration' in name_lower or 'getting started' in name_lower:
        return 'developer-guide'
    return 'api-integration-guide'

def slugify(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

# ── Main update logic ─────────────────────────────────────────────────────────

def _process_guide(item, dry_run):
    menu_code = item.get('menu_code', '')
    menu_name = item.get('menu_name', 'unknown')
    try:
        result = fetch_guide(menu_code)
        content_html = result.get('content', '')
        title = result.get('title') or menu_name
        if not content_html:
            return 0, 0, 0, 0

        markdown = f"# {title}\n\n{html_to_markdown(content_html)}\n"
        folder = get_guide_folder(menu_name)
        os.makedirs(os.path.join(BASE_DIR, folder), exist_ok=True)

        filename = f"{slugify(menu_name)}.md"
        filepath = os.path.join(BASE_DIR, folder, filename)

        if os.path.exists(filepath):
            with open(filepath, encoding='utf-8') as f:
                old = f.read()
            if file_hash(old) == file_hash(markdown):
                return 0, 0, 1, 0
            status = 'UPDATED'
            result_counts = (0, 1, 0, 0)
        else:
            status = 'NEW'
            result_counts = (1, 0, 0, 0)

        safe_print(f"  [{status}] {folder}/{filename}")
        if not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return result_counts

    except Exception as e:
        safe_print(f"  [ERROR] {menu_name}: {e}")
        return 0, 0, 0, 1

def update_guides(menu, dry_run=False):
    guides = [m for m in menu if m.get('doc_type') == 1]
    safe_print(f"[Guides] Found {len(guides)} guide pages")

    added = updated = unchanged = errors = 0
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futures = {ex.submit(_process_guide, item, dry_run): item for item in guides}
        for fut in as_completed(futures):
            a, u, n, e = fut.result()
            added += a; updated += u; unchanged += n; errors += e

    return added, updated, unchanged, errors

_cookies_expired = threading.Event()

def _process_api(item, cookies, dry_run):
    if _cookies_expired.is_set():
        return 0, 0, 0, 1

    api_name = item.get('menu_name', '')
    if not api_name:
        return 0, 0, 0, 0
    try:
        data = fetch_api_spec(api_name, cookies)
        if not data.get('success') or not data.get('result'):
            err_msg = data.get('error_msg', 'no result')
            if 'Forbidden' in str(err_msg):
                _cookies_expired.set()
                safe_print("\n  [!] Cookies expired! Run with --update-cookies to refresh.")
                safe_print("      F12 -> Application -> Cookies -> partner.temu.com")
                return 0, 0, 0, 1
            safe_print(f"  [ERROR] {api_name}: {err_msg}")
            return 0, 0, 0, 1

        doc = data['result']['api_doc_detail']
        markdown = api_to_markdown(doc)
        folder = get_folder_for_api(api_name)
        os.makedirs(os.path.join(BASE_DIR, folder), exist_ok=True)

        filepath = os.path.join(BASE_DIR, folder, f"{api_name}.md")

        if os.path.exists(filepath):
            with open(filepath, encoding='utf-8') as f:
                old = f.read()
            if file_hash(old) == file_hash(markdown):
                return 0, 0, 1, 0
            status = 'UPDATED'
            result_counts = (0, 1, 0, 0)
        else:
            status = 'NEW'
            result_counts = (1, 0, 0, 0)

        safe_print(f"  [{status}] {folder}/{api_name}.md")
        if not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(markdown)
        return result_counts

    except Exception as e:
        safe_print(f"  [ERROR] {api_name}: {e}")
        return 0, 0, 0, 1

def update_apis(menu, dry_run=False):
    cookies = get_cookies()
    api_items = [m for m in menu if m.get('doc_type') == 2 and m.get('menu_name')]
    safe_print(f"[APIs]   Found {len(api_items)} API endpoints")

    _cookies_expired.clear()
    added = updated = unchanged = errors = 0
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futures = {ex.submit(_process_api, item, cookies, dry_run): item for item in api_items}
        for fut in as_completed(futures):
            a, u, n, e = fut.result()
            added += a; updated += u; unchanged += n; errors += e

    return added, updated, unchanged, errors

# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Atualiza a documentação Temu API')
    parser.add_argument('--dry-run', action='store_true', help='Mostra mudanças sem salvar')
    parser.add_argument('--section', choices=['guides', 'apis', 'all'], default='all')
    parser.add_argument('--update-cookies', metavar='COOKIES', help='Salva novos cookies e sai')
    args = parser.parse_args()

    if args.update_cookies:
        with open(COOKIES_FILE, 'w') as f:
            f.write(args.update_cookies.strip())
        print(f"Cookies salvos em {COOKIES_FILE}")
        return

    print(f"{'[DRY RUN] ' if args.dry_run else ''}Iniciando atualizacao -- {datetime.now(BRT).strftime('%Y-%m-%d %H:%M:%S')}")

    print("Buscando menu...")
    menu = fetch_menu()
    print(f"Menu: {len(menu)} itens\n")

    totals = {'added': 0, 'updated': 0, 'unchanged': 0, 'errors': 0}

    need_guides = args.section in ('guides', 'all')
    need_apis   = args.section in ('apis', 'all')

    with ThreadPoolExecutor(max_workers=2) as ex:
        futures = {}
        if need_guides:
            futures[ex.submit(update_guides, menu, args.dry_run)] = 'guides'
        if need_apis:
            futures[ex.submit(update_apis, menu, args.dry_run)] = 'apis'
        for fut in as_completed(futures):
            a, u, n, e = fut.result()
            totals['added'] += a; totals['updated'] += u
            totals['unchanged'] += n; totals['errors'] += e

    print(f"\n{'-'*40}")
    print(f"  Novos:       {totals['added']}")
    print(f"  Atualizados: {totals['updated']}")
    print(f"  Sem mudanca: {totals['unchanged']}")
    print(f"  Erros:       {totals['errors']}")
    if args.dry_run:
        print("  (dry-run: nenhum arquivo foi modificado)")

if __name__ == '__main__':
    main()

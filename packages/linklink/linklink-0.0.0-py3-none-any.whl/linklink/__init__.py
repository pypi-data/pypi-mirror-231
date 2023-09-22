# 相対リンク結合ツール [linklink]

import sys
from sout import sout

# 与えられたurlのhomeのurlを所得する (例えばhttps://something.com)
def get_base_url(url):
	# urlの形式チェック
	if url.startswith("http") is not True:
		raise Exception("[linklink error] invalid url format.")
	# base_urlの取り出し
	temp_ls = url.split("/")
	base_url = "/".join(temp_ls[:3])
	return base_url

# 相対リンクの結合 [linklink]
def link(
	target_url,	# 変換対象のurl (相対・full両方受け付ける)
	page_url	# そのリンクが存在するページのアドレス (base_urlである必要はない)
):
	# target_url前後の空白文字をクレンジング
	target_url = target_url.strip()
	# full-urlの先頭文字列の判定
	def judge_head(url):
		if url.startswith("https://"): return True
		if url.startswith("http://"): return True
		return False
	# page_urlの正当性確認
	if judge_head(page_url) is not True: raise Exception("[linklink error] invalid page_url format.")
	# target_url がすでにfull-linkの場合
	if judge_head(target_url) is True: return target_url
	# page_urlが「/」で終わっている場合は除く
	if page_url.endswith("/"): page_url = page_url[:-1]
	# target_urlの種類で分岐
	if target_url[:2] == "//":
		# 特殊な形式
		protocol_str = ("https:" if page_url.startswith("https://") else "http:")
		full_url = protocol_str + target_url
	elif target_url[:1] == "/":
		# ルート相対アドレス
		base_url = get_base_url(page_url)	# 与えられたurlのhomeのurlを所得する (例えばhttps://something.com)
		full_url = base_url + target_url
	elif target_url[:3] == "../":
		# 上位に戻るパターン
		parent_url = "/".join(page_url.split("/")[:-1])
		full_url = link(target_url[3:], parent_url)
	elif target_url[:2] == "./":
		# 相対アドレス - 省略なし
		full_url = f"{page_url}/{target_url[2:]}"
	else:
		# 相対アドレス - 省略あり
		full_url = f"{page_url}/{target_url}"
	return full_url

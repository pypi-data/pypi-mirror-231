# 相対リンク結合ツール [linklink]
# 【動作確認 / 使用例】

import sys
from sout import sout
from ezpip import load_develop
# 相対リンク結合ツール [linklink]
linklink = load_develop("linklink", "../", develop_flag = True)

# 相対リンクの結合 [linklink]
result = linklink.link(
	target_url = "/hoge3",	# 変換対象のurl (相対・full両方受け付ける)
	page_url = "https://example.com/hoge"	# そのリンクが存在するページのアドレス (base_urlである必要はない)
)
# 結果確認
print(result)	# -> https://example.com/hoge3

# 様々な結合パターン
print(linklink.link("http://example2.com/hoge", "https://example.com/hoge"))	# -> http://example2.com/hoge
print(linklink.link("/hoge3", "https://example.com/"))	# -> https://example.com/hoge3
print(linklink.link("/hoge3", "https://example.com"))	# -> https://example.com/hoge3
print(linklink.link("hoge3/fuga", "https://example.com/hoge"))	# -> https://example.com/hoge/hoge3/fuga
print(linklink.link("hoge3/fuga", "https://example.com/hoge/"))	# -> https://example.com/hoge/hoge3/fuga
print(linklink.link("./hoge3", "https://example.com/hoge/"))	# -> https://example.com/hoge/hoge3
print(linklink.link("../hoge3", "https://example.com/hoge/hoge2"))	# -> https://example.com/hoge/hoge3
print(linklink.link("../../hoge3", "https://example.com/hoge/hoge2"))	# -> https://example.com/hoge3
print(linklink.link("//hoge3.com/fuga", "https://example.com/hoge"))	# -> https://hoge3.com/fuga
print(linklink.link("//hoge3.com/fuga", "wrong://example.com/hoge"))	# -> Exception: [linklink error] invalid page_url format.

from staticmap import StaticMap

# 地図オブジェクトを生成
# 画像の横幅と縦幅と OpenStreetMap 標準タイルレイヤーのタイルURLを指定
map = StaticMap(800, 600, url_template='http://a.tile.openstreetmap.org/{z}/{x}/{y}.png')

# 地図を描画した Pillow の PIL.Image オブジェクトを取得
# ズームレベルと経度・緯度を指定
image = map.render(zoom=17, center=[136.882090, 35.170560])

# 地図画像を保存
image.save('osm.png')

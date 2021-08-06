require &quot;httparty&quot;
 
## 1. 逆ジオコーディング対象となる緯度経度を指定（東京タワーの緯度経度を指定）
lat = 35.65858645
lon = 139.745440057962
 
## 2. OpenStreetMapの逆ジオコーディングAPIへアクセスし、結果を取得
endpointUrl = &quot;http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=#{lat}&amp;lon=#{lon}&amp;zoom=18&amp;addressdetails=1&quot;
response = HTTParty.get(URI.encode(endpointUrl))
 
## 3. 取得した結果を出力
puts response[&quot;reversegeocode&quot;][&quot;result&quot;][&quot;ref&quot;]
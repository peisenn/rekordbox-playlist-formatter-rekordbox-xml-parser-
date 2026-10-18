import sys
import xmltodict

# 支持从命令行参数读取文件名，未提供时默认使用 sen.xml
xml_filename = sys.argv[1] if len(sys.argv) > 1 else 'sen.xml'

try:
    with open(xml_filename, 'rb') as f:
        # 自动跳过 UTF-8 XML 声明前的字节标记
        raw_data = f.read()
        xml_content = raw_data[raw_data.find(b'<DJ_PLAYLISTS'):]
        
    dj_playlists = xmltodict.parse(xml_content)['DJ_PLAYLISTS']
    collection = dj_playlists['COLLECTION']
    tracks = collection['TRACK']

    # 如果只有单首曲目，xmltodict 会返回 dict 而非 list，这里做个兼容
    if isinstance(tracks, dict):
        tracks = [tracks]

    print("\n====\n")

    for t in tracks:
        art = t.get("@Artist", "")
        bpm = t.get("@AverageBpm", "")
        key = t.get("@Tonality", "")
        nam = t.get("@Name", "")

        print(f'{bpm:6s} | {key:6s} | {nam} | {art}')

except FileNotFoundError:
    print(f"Error: Could not find '{xml_filename}'. Please export your Rekordbox XML first.")
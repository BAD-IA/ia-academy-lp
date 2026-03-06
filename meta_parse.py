import json, urllib.request, sys

TOKEN = "EAAVTGnIcHhIBQ4YR0aoH2WFKEMH3HKpWRWty8EndVm9ylGHs3dwtQZCZATQFVs1D4JfCiUPjnuKk622BkFdRa315B8PQMy2vrRVMzWySWf2E9eGb01U8gARE0PZAV3w1phI41cFWRdgyqUetQXXZBjg1AGt9X4FCoRy0fVwNiBJZAVyuAvcob1DbdhqLR2wZDZD"
CAMPAIGN_ID = "120241830733140396"

url = (
    f"https://graph.facebook.com/v21.0/{CAMPAIGN_ID}/insights"
    f"?fields=ad_id,ad_name,impressions,reach,clicks,spend,ctr,cpc,actions,video_avg_time_watched_actions"
    f"&date_preset=maximum&level=ad&access_token={TOKEN}"
)

with urllib.request.urlopen(url) as r:
    data = json.loads(r.read())

for ad in data.get('data', []):
    name = ad.get('ad_name', 'N/A')
    impressions = ad.get('impressions', '0')
    clicks = ad.get('clicks', '0')
    spend = ad.get('spend', '0')
    ctr = ad.get('ctr', '0')
    cpc = ad.get('cpc', '0')

    purchases = 0
    for a in ad.get('actions', []):
        if a.get('action_type') == 'purchase':
            purchases = a.get('value', 0)

    video_time = 'N/A'
    for v in ad.get('video_avg_time_watched_actions', []):
        if v.get('action_type') == 'video_view':
            video_time = str(round(float(v.get('value', 0)))) + 's'

    print('--- ' + name + ' ---')
    print('  Impressoes: ' + impressions + ' | Cliques: ' + clicks + ' | CTR: ' + str(round(float(ctr), 2)) + '%')
    print('  Gasto: R$' + str(round(float(spend), 2)) + ' | CPC: R$' + str(round(float(cpc), 2)))
    print('  Compras: ' + str(purchases) + ' | Video avg: ' + video_time)
    print()

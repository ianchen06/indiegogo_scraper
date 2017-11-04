import os
import requests

for pg in range(101,201):
    response = requests.post(
        'https://www.indiegogo.com/private_api/discover',
        headers={'Accept': 'application/json, '
                 'text/plain, '
                 '*/*',
                 'Accept-Encoding': 'gzip, '
                 'deflate, '
                 'br',
                 'Accept-Language': 'en-US,en;q=0.9',
                 'Connection': 'keep-alive',
                 'Content-Type': 'application/json;charset=UTF-8',
                 'Cookie': 'messagesUtk=b47286d8b0d04a5dbb7fa47acae88d61; '
                 'D_SID=122.116.172.49:hponTvPvMrTS9k73bNjJUlgJod2Xyjpt6EiHPc5OFW0; '
                 'romref=shr-pica; '
                 'romref_referer_host=www.indiegogo.com; '
                 '_gat=1; '
                 '_ga=GA1.2.1180398887.1509527218; '
                 '_gid=GA1.2.655623585.1509527218; '
                 'D_IID=71BD8007-AAE3-3CFD-94FB-4DD8B5721EE0; '
                 'D_UID=E9F3879D-919E-38DA-945B-6271828E2B40; '
                 'D_ZID=D8ED16D5-50D4-34AF-B5CD-85C25794F214; '
                 'D_ZUID=80EEDBC9-8426-3AE1-8411-CC0950152B53; '
                 'D_HID=7E4FEBDB-5A47-3BB4-84A1-F6C76EA26D72; '
                 '_ceg.s=oyqf0p; '
                 '_ceg.u=oyqf0p; '
                 '__stripe_mid=33322804-e5d7-4e65-bff8-1a74f46da468; '
                 '__stripe_sid=f1e60c71-9fbf-42ba-8978-84f0911e0a88; '
                 '__hstc=223492548.a4862d41e56550842273927f4ca5a7ca.1509527219778.1509527219778.1509527219778.1; '
                 '__hssrc=1; '
                 '__hssc=223492548.6.1509527219778; '
                 'hubspotutk=a4862d41e56550842273927f4ca5a7ca; '
                 'locale=en; '
                 'cohort=www.indiegogo.com%7Cdir-XXXX%7Cshr-pica; '
                 'visitor_id=b0e35acfcfa7a32143a4627992f4cd6653d4280fb8fa9fa986d7e82da3a8a419; '
                 'analytics_session_id=a72cf8a4291cea49e18d6d85cb5f5695110216f0e1384a6fcf1ba15118dddc9b; '
                 'recent_project_ids=2246733; '
                 '_session_id=bfa10f7e77f952fb6fb7d647a5121d87',
                 'Origin': 'https://www.indiegogo.com',
                 'Referer': 'https://www.indiegogo.com/explore/all?project_type=all&project_timing=all&sort=trending',
                 'User-Agent': 'Mozilla/5.0 '
                 '(Macintosh; '
                 'Intel '
                 'Mac '
                 'OS '
                 'X '
                 '10_13_0) '
                 'AppleWebKit/537.36 '
                 '(KHTML, '
                 'like '
                 'Gecko) '
                 'Chrome/62.0.3202.75 '
                 'Safari/537.36',
                 'X-CSRF-Token': '7geVwofP141Nzo2Rw5gFWn6KV+3q96R9jE3kplWQ0tve9iJ7YpoBZT3Y7dnfj9t9be3CZFEkGpMv3q2mMAseOw==',
                 'X-Distil-Ajax': 'zwdtbxyeyryawsddxdsvzttxeevwbeu',
                 'X-Locale': 'en'},
        json={'category_main': None,
              'category_top_level': None,
              'page_num': pg,
              'per_page': 12,
              'project_timing': 'all',
              'project_type': "campaign",
              'sort': 'trending'}
    )
    
    discover = response.json()
    urls = [x.get('clickthrough_url')
            for x in discover['response']['discoverables']]
    for url in urls:
        print("[INFO] %s"%url)
        os.system("node igg.js %s" % url)

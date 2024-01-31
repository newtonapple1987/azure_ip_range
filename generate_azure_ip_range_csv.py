import json
import requests as res
import re

latest = res.get("https://azservicetags.azurewebsites.net")
latest = latest.text
match = re.search(r"(Public[^\"]+)\"(https://[^\"]+)", latest)
ip_url = match.group(2)
data = res.get(ip_url).text
data = json.loads(data)

output = open("azure_ip_range.csv", "w")
output.write('"ip","name","id","region","platform","systemService"\n')

for i in data["values"]:
    for  j in i["properties"]["addressPrefixes"]:
        output.write('"')
        output.write('","'.join([ i if len(i)>0 else "0" for i in [j,i["name"],i["id"],i["properties"]["region"],i["properties"]["platform"],i["properties"]["systemService"]]]))
        output.write('"\n')
output.close()

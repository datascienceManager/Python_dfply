# %%
# !pip install pywhatkit
# !pip install six.moves

import urllib.request as ur
import re



# %%
html = ur.urlopen('https://www.youtube.com/results?search_query=BeekeeperofficialTrailer')



videoId = re.findall(r"watch\?v=(\S{11})",html.read().decode())

# print(videoId)
print("https://www.youtube.com/watch?v="+videoId[0])


# %%




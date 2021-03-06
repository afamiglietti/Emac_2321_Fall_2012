import matplotlib.pyplot as plt
import networkx as nx
import re
from urllib import urlopen 

start_url = "news.discovery.com/space/"
url_list = []
second_list = []
write_file = open("test2.txt", 'w')

G = nx.Graph()


def graph_page(begin_url):
    found_urls = []
    G.add_node(begin_url)

    link_match = re.findall(r'(<a href="http://)([\w\.\-]+)([^"]*")', urlopen("http://" + begin_url).read())

    for link in link_match:
        if not(re.search(begin_url, link[1])):
            if not(link[1] in found_urls):
                found_urls.append(link[1])
            G.add_edge(begin_url, link[1])
    return found_urls        


url_list = graph_page(start_url)
for url in G.nodes():
    print url
    try:
        graph_page(url)
    except:
        pass

for node in G.nodes():
    if len(G.neighbors(node)) == 1:
        G.remove_node(node)


for url in G.nodes():
    print url
    try:
        graph_page(url)
    except:
        pass
        
for node in G.nodes():
    if len(G.neighbors(node)) <= 2:
        G.remove_node(node)

nx.draw_spring(G)
plt.show()

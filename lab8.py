from cassandra.cluster import Cluster
if __name__ == "__main__":
    cluster = Cluster(['172.0.0.1'],port=9042)
    session = cluster.connect('store',wait_for_all_pools=True)
    session.execute('USE store')
    rows = session.execute('SELECT * FROM users')
    for row in rows:
        print(row.age,row.name,row.username)
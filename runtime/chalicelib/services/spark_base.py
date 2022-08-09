from typing import Protocol

class SparkJob(Protocol):
    def create_job():
        pass
    def submit_job():
        pass
    def trigger_job():
        pass

class SparkCluster(Protocol):
    def check_connection():
        pass
    def create_cluster():
        pass
    def get_clusters():
        pass
    def get_cluster():
        pass
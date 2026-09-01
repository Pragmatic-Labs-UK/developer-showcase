import sys
import time

class SystemNode:
    def __init__(self, node_id, status):
        self.node_id = node_id
        self.status = status
        self.metrics = {"cpu": 12.4, "memory": 512, "active": True}

    def execute_diagnostic(self):
        print(f"[{time.strftime('%H:%M:%S')}] Initializing node {self.node_id}...")
        for i in range(1, 6):
            time.sleep(0.1)
            print(f"--> Diagnostic cycle {i}/5 complete.")
        return True

    def fetch_telemetry(self):
        return self.metrics

if __name__ == "__main__":
    node = SystemNode("PragmaticLabs-Core", "ONLINE")
    if node.execute_diagnostic():
        print(f"System Status: {node.status}")
        print(f"Telemetry Payload: {node.fetch_telemetry()}")

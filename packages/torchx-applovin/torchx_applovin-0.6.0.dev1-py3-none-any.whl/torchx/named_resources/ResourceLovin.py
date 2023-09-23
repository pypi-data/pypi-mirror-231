#!/usr/bin/env python3

from torchx.specs import Resource

def test_gpu_node_selector() -> Resource:
    capabilities = {
        "node_selector": {
            "node_pool": "biddermlgpu-t4-node-pool"
        }
    }

    return Resource(cpu=8,  gpu=1, memMB=61_000, capabilities=capabilities)

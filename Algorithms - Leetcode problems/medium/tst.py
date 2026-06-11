from pathlib import Path
import scanpy as sc
import os 

print(os.getcwd())

adata = sc.read_h5ad('human_immune_health_atlas_b-plasma.h5ad')

print(adata.shape)
print(adata.obs.head())
print(adata.var.head())
print(adata.X)
"""
print(adata.layers.keys())
print(adata.obs["AIFI_L2"].value_counts())

print(adata.obs["AIFI_L3"].value_counts())
adata.layers["counts"]
"""
print(adata.obs.columns)
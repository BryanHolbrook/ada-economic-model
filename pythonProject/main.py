import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.sankey import Sankey

# Set up the figure
fig, ax = plt.subplots(figsize=(14, 10))
ax.axis('off')

# Title
ax.set_title("Cardano ADA Utility Token Economic Flowchart", fontsize=16, fontweight='bold')

# Define the sankey diagram
sankey = Sankey(ax=ax, unit=None)

# ADA Holders flow
sankey.add(flows=[1, -0.5, -0.2, -0.3],
           labels=['ADA Holders', 'Staking', 'Governance', 'dApp Usage'],
           orientations=[0, 1, 1, 1], facecolor='#1f77b4')

# Stake Pool Operators flow
sankey.add(flows=[0.5, -0.5],
           labels=['Staking', 'Stake Pool Operators'],
           orientations=[-1, -1], prior=0, connect=(1, 0), facecolor='#ff7f0e')

# Validators flow
sankey.add(flows=[0.5, -0.4, -0.1],
           labels=['Stake Pool Operators', 'Validators', 'Rewards Distribution'],
           orientations=[-1, 1, 1], prior=1, connect=(1, 0), facecolor='#2ca02c')

# Governance Participants flow
sankey.add(flows=[0.2, -0.2],
           labels=['Governance', 'Governance Participants'],
           orientations=[-1, -1], prior=0, connect=(2, 0), facecolor='#d62728')

# dApp Users flow
sankey.add(flows=[0.3, -0.3],
           labels=['dApp Usage', 'dApp Users'],
           orientations=[-1, -1], prior=0, connect=(3, 0), facecolor='#9467bd')

# Treasury flow
sankey.add(flows=[0.4, 0.1, -0.5],
           labels=['Treasury', 'Transaction Fees', 'Treasury Funding'],
           orientations=[0, 1, -1], facecolor='#8c564b')

# Complete the Sankey diagram
diagrams = sankey.finish()

# Annotations for system modules
ax.text(-2, 1.2, "Cardano Settlement Layer (CSL)", fontsize=12, fontweight='bold')
ax.text(1.5, 0.8, "Cardano Computation Layer (CCL)", fontsize=12, fontweight='bold')
ax.text(-0.5, -0.5, "Staking Module", fontsize=12, fontweight='bold')
ax.text(2, -1.5, "Governance Module", fontsize=12, fontweight='bold')
ax.text(-2, -1.2, "Treasury", fontsize=12, fontweight='bold')

# Show the flowchart
plt.show()
